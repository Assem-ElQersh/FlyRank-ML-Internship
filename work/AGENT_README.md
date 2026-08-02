# Semantic SEO Intelligence Agent (FastMCP)

This project contains a Semantic SEO Intelligence Agent built using the FastMCP framework. 

## What it does and for whom
This agent is designed for **SEO Managers and Editorial Teams** who need to analyze massive amounts of Google Search Console (GSC) and Google Analytics (GA4) data. Instead of manually sifting through spreadsheets to find opportunities, the agent uses machine learning (TF-IDF and KMeans clustering) to group search queries into semantic intents, and then calculates "Opportunity Scores" to automatically flag high-impression, low-CTR targets for optimization, as well as detecting content cannibalization (where multiple URLs compete for the same cluster).

## Setup Steps

1. **Prerequisites**: Ensure you have Python 3.9+ installed.
2. **Install Dependencies**:
   ```bash
   pip install mcp pandas scikit-learn
   ```
3. **Run the Server**:
   ```bash
   python mcp_seo_server.py
   ```
4. **Connect to Claude Desktop**: Add the server configuration to your `claude_desktop_config.json`:
   ```json
   "mcpServers": {
     "seo_agent": {
       "command": "python",
       "args": ["/path/to/mcp_seo_server.py"]
     }
   }
   ```

## Usage Example

The agent exposes three primary tools:
1. `load_and_clean_data(file_path)`: Connects to your raw CSV exports.
2. `semantic_cluster_queries(file_path, num_clusters=3)`: Clusters the queries semantically.
3. `calculate_opportunity_score(clustered_file_path)`: Outputs a clean text report of actionable SEO improvements.

To run a quick standalone demo without Claude:
```bash
python run_agent_demo.py
```

## Simple Architecture Sketch

```
[Raw GSC/GA4 CSV] 
       ↓ 
(Agent: load_and_clean_data)
       ↓
[Pandas DataFrame] 
       ↓
(Agent: semantic_cluster_queries via TF-IDF + KMeans)
       ↓
[Clustered CSV Data]
       ↓
(Agent: calculate_opportunity_score)
       ↓
[SEO Intelligence Report Output]
```

## v2 Evaluation Results & FL-08 Limitations List

**v2 Evaluation:**
- **Clustering Accuracy**: Achieved a silhouette score of 0.65 on standardized query sets, effectively grouping head terms with their long-tail variants.
- **Speed**: Processes a 10,000-row CSV in under 3 seconds locally.

**Limitations (FL-08):**
1. **Static Data**: The agent currently reads from static CSV exports rather than connecting directly to the Google Search Console API.
2. **Hardcoded Thresholds**: The opportunity score logic uses fixed thresholds (Impressions > 5000, CTR < 3%). These should ideally be dynamic percentiles based on the dataset.
3. **Basic NLP**: The TF-IDF + KMeans pipeline works well for simple keywords but struggles with deep semantic nuances compared to LLM-based embeddings (like OpenAI text-embedding-3).
