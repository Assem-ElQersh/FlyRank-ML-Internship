# Demo Video Script: Semantic SEO Intelligence Agent (3-5 Minutes)

**Before Recording:**
1. Open your terminal in the `work/` directory.
2. Have `AGENT_README.md` and `mcp_seo_server.py` open in your code editor in the background.
3. Start recording your screen and microphone (using OBS or Loom).

---

### [0:00 - 0:30] Introduction & The Problem
**Action:** Show your code editor with the `AGENT_README.md` file open.
**Script:** 
"Hi everyone, for my AI Fluency track project, I built the Semantic SEO Intelligence Agent using the FastMCP framework. I built this for SEO Managers and Editorial teams who waste hours manually scrolling through spreadsheets of Google Search Console data trying to find which pages need updating. This agent automates the data cleaning, clusters queries by intent, and scores them to find high-ROI opportunities."

### [0:30 - 1:30] Live End-to-End Run
**Action:** Switch to your terminal window. Type `python3 run_agent_demo.py` but don't hit enter yet.
**Script:**
"Instead of just showing you slides, I'm going to run a live end-to-end demo of the agent right now using a Python test harness I built."
*(Hit Enter to run the script)*
"As you can see, the agent is executing its three primary tools. First, it ingested our raw SEO data. Second, it used its NLP clustering tool to group those queries semantically. And finally, it generated the SEO Intelligence Report, instantly flagging our best 'Striking-Distance Opportunities' and catching a content cannibalization alert where two URLs are competing for the exact same intent."

### [1:30 - 2:30] Design Decision (Required Criteria)
**Action:** Switch to the code editor showing `mcp_seo_server.py`, specifically highlighting the `semantic_cluster_queries` function (lines 28-34).
**Script:**
"I want to highlight one specific design decision I made here. For the semantic clustering, I chose to use a lightweight TF-IDF Vectorizer combined with scikit-learn's KMeans, rather than relying on a massive LLM or calling OpenAI's embeddings API. I made this decision because SEO datasets can often be hundreds of thousands of rows long, and doing this locally using traditional ML is significantly faster and costs zero dollars in API fees, making it much more viable for production environments."

### [2:30 - 3:30] Limitations & Guardrails (Required Criteria)
**Action:** Switch back to the `AGENT_README.md` and highlight the Limitations list.
**Script:**
"However, being honest about where this breaks is critical. One major limitation of this v2 agent is the hardcoded scoring thresholds. Currently, the agent flags an opportunity if impressions are strictly over 5,000 and CTR is under 3%. While this works for a generic dataset, it breaks down completely if a client has much lower baseline traffic. In a future iteration, this guardrail needs to be replaced with dynamic percentile calculations based on the specific dataset's distribution."

### [3:30 - 4:00] Outro
**Action:** Briefly show the `run_agent_demo.py` code to prove it works.
**Script:**
"Overall, the agent successfully proves that we can abstract away the manual spreadsheet wrangling and move straight to editorial action. Thanks for watching!"

---
**After Recording:** Stop the recording, upload it as an *Unlisted* video to YouTube, and submit the link along with the `AGENT_README.md` file.
