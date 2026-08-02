from mcp.server.fastmcp import FastMCP
import duckdb
import os

# Create the FastMCP Server
mcp = FastMCP("FlyRank_Data_Warehouse_Agent")

# Constants
REL = "hf://datasets/FlyRank/internship-warehouse"

def get_connection():
    """Initializes DuckDB connection with HuggingFace credentials."""
    hf_token = os.environ.get('HF_TOKEN')
    if not hf_token:
        raise ValueError("HF_TOKEN environment variable not set. Required for warehouse access.")
    
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute(f"CREATE OR REPLACE SECRET hf (TYPE huggingface, TOKEN '{hf_token}');")
    return con

@mcp.tool()
def get_warehouse_schema() -> str:
    """Returns the schema of the remote FlyRank data warehouse."""
    return f"""
    --- FlyRank Data Warehouse (Star Schema) ---
    Location: {REL}
    
    Tables:
    1. dim_clients.parquet: Client metadata (client_hash_id, gsc_data_start)
    2. dim_content.parquet: Page metadata (content_hash_id, url, word_count)
    3. fact_content_daily_performance/**/*.parquet (81.8M rows): Daily metrics
       - client_hash_id, content_hash_id, date, gsc_impressions, gsc_clicks, gsc_avg_position
    """

@mcp.tool()
def execute_sql_query(query: str) -> str:
    """Executes arbitrary DuckDB SQL against the remote warehouse."""
    try:
        con = get_connection()
        # Prevent dangerous queries, though this is a read-only remote dataset
        if any(keyword in query.upper() for keyword in ['DROP', 'DELETE', 'INSERT', 'UPDATE']):
            return "Error: Only SELECT queries are permitted on the Data Warehouse."
            
        df = con.execute(query).df()
        return df.to_string()
    except Exception as e:
        return f"Error executing query: {str(e)}"

@mcp.tool()
def find_decaying_content(client_id: str) -> str:
    """Finds high-traffic content that is decaying for a specific client."""
    try:
        con = get_connection()
        # Query the June 2026 partition specifically for fast retrieval
        query = f"""
        WITH metrics AS (
            SELECT
                content_hash_id,
                SUM(gsc_impressions) as total_imps,
                SUM(gsc_clicks) as total_clicks,
                AVG(gsc_avg_position) as avg_pos
            FROM read_parquet('{REL}/fact_content_daily_performance/month=2026-06/*.parquet')
            WHERE client_hash_id = '{client_id}'
            GROUP BY 1
            HAVING SUM(gsc_impressions) > 1000
        )
        SELECT 
            m.content_hash_id, 
            m.total_imps, 
            m.total_clicks, 
            (m.total_clicks * 100.0 / m.total_imps) as ctr
        FROM metrics m
        WHERE (m.total_clicks * 100.0 / m.total_imps) < 2.0
        ORDER BY m.total_imps DESC
        LIMIT 5
        """
        df = con.execute(query).df()
        
        report = f"--- Decaying Content Report for Client {client_id} ---\n"
        if df.empty:
            report += "No decaying content found matching the criteria.\n"
        else:
            for _, row in df.iterrows():
                report += f"Content ID: {row['content_hash_id']} | Imps: {row['total_imps']} | CTR: {row['ctr']:.2f}%\n"
        return report
        
    except Exception as e:
        return f"Error calculating decay: {str(e)}"

if __name__ == "__main__":
    mcp.run()
