# FL-06 Agent Design Spec: Semantic SEO Intelligence Agent

## 1. Job to be Done
**The Job:** Automate the FlyRank SEO intelligence pipeline outlined in the Hackathon Brief. The agent will ingest raw Google Search Console (GSC) and Google Analytics 4 (GA4) data, flatten nested JSONs, cluster search queries by semantic intent (using embeddings and HDBSCAN), and output a prioritized list of high-impression/low-CTR content opportunities based on business impact.
**The User & Frequency:** Me (AI & DL Engineer), running the agent weekly to detect emerging search trends, intent mismatches, and content cannibalization for the Flewd brand.

## 2. Tools & Data Needed (Access Plan)
To achieve this within a ~10-hour build limit, we will keep the data local and expose it to the agent via MCP.
*   **Data Source:** The massive 81.8 million row pseudonymized dataset hosted on Hugging Face (`FlyRank/internship-warehouse`). This contains the full GSC and GA4 BigQuery history across 104 clients. We will use the Python `datasets` library to securely pull and process specific client subsets (like "Flewd").
*   **Tool 1: `load_and_clean_data()`** - A Python tool that ingests the GA4/GSC files, handles anonymized queries (blank fields), and flattens the stringified GA4 JSON device/geo data.
*   **Tool 2: `semantic_cluster_queries(queries_list)`** - Generates embeddings (using local `sentence-transformers`) and runs HDBSCAN to group queries by meaning, returning labeled clusters.
*   **Tool 3: `calculate_opportunity_score(cluster_id)`** - Merges GSC ranking/CTR data with GA4 engagement data to calculate an MRR-weighted opportunity score for the cluster.

## 3. Draft Instructions (System Prompt)
> "You are the FlyRank Semantic SEO Intelligence Agent. Your goal is to find where content and search intent diverge.
> 
> 1. Call `load_and_clean_data()` to ingest the latest GSC and GA4 extracts. Ensure you join GA4 and GSC data on the landing page URL, not the query.
> 2. Pass the list of unique queries to `semantic_cluster_queries()` to map meaning and intent (e.g., grouping 'comparison' vs 'risk/safety' queries).
> 3. Analyze the clusters using `calculate_opportunity_score()`. Look specifically for:
>    *   High-impression, low-CTR pages in ranking positions 3-15.
>    *   Pages with traffic but low GA4 engagement (intent mismatch).
>    *   Content cannibalization (multiple URLs competing for the same semantic cluster).
> 4. Output a brief, actionable report summarizing the top 3 highest-priority content opportunities."

## 4. Pre-Build Evaluation Cases (FL-03 Style)
Before building, the agent must pass these 5 deterministic evals on a synthetic dataset:
1.  **JSON Flattening Eval:** Feed the agent a GA4 row with nested snake_case JSON. Verify the agent successfully parses and extracts the device and geo fields before analysis.
2.  **Privacy/Anonymization Eval:** Inject rows where the GSC query field is blank (~8% of real data). Verify the agent handles them deliberately without crashing or creating a "null" mega-cluster.
3.  **Intent Classification Eval:** Provide the queries *"magnesium taurate vs glycinate"* and *"alternative to epsom salt"*. Verify the agent groups them into a "Comparison/Replacement" semantic cluster.
4.  **Striking Distance Eval:** Provide a dataset where URL A is position #4 with 10k impressions and 1% CTR, and URL B is position #1 with 500 impressions. Verify the agent prioritizes URL A as the top opportunity.
5.  **Cannibalization Eval:** Provide two distinct URLs that rank for queries mapped to the exact same semantic cluster. Verify the agent explicitly flags this as "content cannibalization" and recommends a merge.

## 5. Risks and Guardrails
*   **Data Privacy Risk (High):** GA4 data contains real client traffic and ecommerce data.
    *   *Guardrail (PII Filter):* The agent will be restricted to a local MCP server. It must **never** upload raw GA4 event data to external third-party APIs (like OpenAI) without aggressive PII filtering and token masking.
*   **Destructive Action Risk (Low):**
    *   *Guardrail (Rules-based):* The agent will be granted **Read-Only** access to the data directories. It must never execute SQL `DROP` or `UPDATE` commands on the source files.

## 6. Build Platform Justification
**Chosen Platform:** Claude Desktop app utilizing a custom Local Python MCP (Model Context Protocol) Server.

**Justification:** Semantic clustering (HDBSCAN), dimensionality reduction (UMAP), and heavy data manipulation (flattening nested JSON across thousands of rows) exceed the strict timeout limits and capabilities of simple n8n nodes or Claude Projects. A custom GPT is also insufficient because it cannot securely or reliably process the raw BigQuery JSON/CSV extracts without uploading confidential client data to OpenAI's servers.

By using Claude Desktop + a custom Python MCP server, I can execute robust, open-source data science libraries (`pandas`, `scikit-learn`, `sentence-transformers`) securely on my local machine. This elegantly separates concerns: offloading heavy, deterministic computation to Python tools while Claude handles the orchestration and insight generation.
