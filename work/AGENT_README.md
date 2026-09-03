# FlyRank Data Warehouse Agent (FastMCP)

This project contains a highly scalable Data Warehouse Agent built using the FastMCP framework and DuckDB. 

## What it does and for whom
This agent is designed for **FlyRank Data Scientists and SEO Engineers**. Rather than analyzing tiny CSV exports, this agent connects directly to the massive remote FlyRank Data Warehouse (81.8 million rows) hosted on Hugging Face using DuckDB's `httpfs` extension. It allows language models to dynamically query the true production Star Schema, instantly identifying content decay across enterprise clients without pulling gigabytes of Parquet files into local memory.

## Setup Steps

1. **Prerequisites**: Ensure you have Python 3.9+ installed.
2. **Install Dependencies**:
   ```bash
   pip install mcp duckdb pandas
   ```
3. **Authentication**: You must export your Hugging Face token to authorize access to the private warehouse:
   ```bash
   export HF_TOKEN="your_huggingface_token"
   ```
4. **Connect to Claude Desktop**: Add the server configuration to your `claude_desktop_config.json`:
   ```json
   "mcpServers": {
     "warehouse_agent": {
       "command": "python",
       "args": ["/path/to/mcp_seo_server.py"],
       "env": {
         "HF_TOKEN": "your_huggingface_token"
       }
     }
   }
   ```

## Usage Example

The agent exposes powerful database tools:
1. `get_warehouse_schema()`: Exposes the exact Parquet schema and locations to the LLM.
2. `execute_sql_query(query)`: Allows the LLM to write and execute its own DuckDB SQL analytics.
3. `find_decaying_content(client_id)`: Runs an optimized aggregation over the 81M-row fact table for a specific client to find high-traffic, low-CTR targets.

To run a quick standalone demo (uses an instant mock fallback if `HF_TOKEN` is not set):
```bash
python run_agent_demo.py
```

## Simple Architecture Sketch

```
[Claude / LLM] 
       ↓ (Tool Call: execute_sql_query)
[FastMCP Server: mcp_seo_server.py] 
       ↓ (DuckDB query execution)
[HTTPFS Network Layer (HF_TOKEN Auth)]
       ↓
[Hugging Face: FlyRank/internship-warehouse]
[81.8 Million Rows of Columnar Parquet Data]
```

## v2 Evaluation Results & FL-08 Limitations List

**v2 Evaluation:**
- **Scale Capability**: Successfully parses the `dim_content` table (519k rows) and the `fact_content_daily_performance` table (81M rows) without OOM exceptions by pushing filtering down to the remote columnar Parquet files.
- **Latency**: Targeted queries (e.g., specific `client_hash_id` filtering) execute in ~10-15 seconds remotely.

**Limitations (FL-08):**
1. **Read-Only**: The agent can only execute `SELECT` statements. It cannot mutate data in the warehouse.
2. **Network Dependency**: Because it queries Hugging Face remotely via HTTPFS, execution time is highly dependent on bandwidth. A timeout could occur on extremely complex JOINs across all 81 million rows.
3. **No Caching Layer**: Queries are re-executed from scratch every time, which wastes bandwidth if the LLM repeatedly asks the same question. Future versions need a local Redis or SQLite cache.

## AI Transparency Framework Note
*I built this FastMCP agent, including the DuckDB httpfs integration and the mcp_seo_server.py logic, utilizing Claude and Antigravity as my AI build partners. I independently verified the SQL aggregation logic, tested the cross-environment compatibility, and verified the output correctness against raw parquet files manually.*
