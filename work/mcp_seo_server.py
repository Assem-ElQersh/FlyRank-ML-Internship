from mcp.server.fastmcp import FastMCP
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Create the FastMCP Server
mcp = FastMCP("Semantic_SEO_Intelligence_Agent")

@mcp.tool()
def load_and_clean_data(file_path: str) -> str:
    """Ingests raw GSC/GA4 SEO data and returns a summary of the columns and rows."""
    try:
        df = pd.read_csv(file_path)
        return f"Successfully loaded {len(df)} rows from {file_path}. Available columns: {list(df.columns)}."
    except Exception as e:
        return f"Error loading data: {str(e)}"

@mcp.tool()
def semantic_cluster_queries(file_path: str, num_clusters: int = 3) -> str:
    """Uses NLP (TF-IDF + KMeans) to cluster search queries into semantic intents."""
    try:
        df = pd.read_csv(file_path)
        if 'query' not in df.columns:
            return "Error: 'query' column missing from dataset."
            
        queries = df['query'].fillna("").tolist()
        
        # Lightweight MVP clustering using scikit-learn
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(queries)
        
        kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
        df['semantic_cluster'] = kmeans.fit_predict(X)
        
        # Save clustered data
        output_path = file_path.replace('.csv', '_clustered.csv')
        df.to_csv(output_path, index=False)
        
        return f"Success. Grouped queries into {num_clusters} semantic clusters and saved to {output_path}. You can now score the clusters."
    except Exception as e:
        return f"Error clustering: {str(e)}"

@mcp.tool()
def calculate_opportunity_score(clustered_file_path: str) -> str:
    """Finds high-impression, low-CTR content and flags cannibalization."""
    try:
        df = pd.read_csv(clustered_file_path)
        
        # Scoring logic: High impressions, CTR < 3%, position between 3 and 15
        opps = df[(df['impressions'] > 5000) & (df['ctr'] < 0.03) & (df['position'] >= 3)]
        opps = opps.sort_values(by='impressions', ascending=False)
        
        # Cannibalization check: Multiple URLs in the same cluster
        cannibalization = df.groupby('semantic_cluster')['url'].nunique()
        cannibalized_clusters = cannibalization[cannibalization > 1].index.tolist()
        
        report = "--- SEO Intelligence Report ---\n\n"
        
        report += "1. Top Striking-Distance Opportunities (High Impression, Low CTR):\n"
        for _, row in opps.iterrows():
            report += f"   - Query: '{row['query']}' | URL: {row['url']} | Impressions: {row['impressions']} | CTR: {row['ctr']*100}%\n"
            
        report += "\n2. Content Cannibalization Alerts:\n"
        for c_id in cannibalized_clusters:
            competing_urls = df[df['semantic_cluster'] == c_id]['url'].unique()
            report += f"   - Cluster {c_id} has multiple competing URLs: {', '.join(competing_urls)}\n"
            
        return report
    except Exception as e:
        return f"Error calculating score: {str(e)}"

if __name__ == "__main__":
    mcp.run()
