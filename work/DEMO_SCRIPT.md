# Demo Video Script: FlyRank Data Warehouse Agent (3-5 Minutes)

**Before Recording:**
1. Open your terminal in the `work/` directory.
2. Have `AGENT_README.md` and `mcp_seo_server.py` open in your code editor.
3. Start recording your screen and microphone (using OBS or Loom).
*(Note: If you don't export your HF_TOKEN, `run_agent_demo.py` will instantly run in mock mode so you aren't waiting on the video for the 81M rows to process remotely).*

---

### [0:00 - 0:30] Introduction & The Problem
**Action:** Show your code editor with the `AGENT_README.md` file open.
**Script:** 
"Hi everyone, for my AI Fluency track project, I built a production-grade Data Warehouse Agent using FastMCP and DuckDB. I built this for FlyRank Data Scientists who want to use LLMs to analyze our massive 81-million-row production dataset. Instead of using naive, tiny CSV exports, this agent securely connects to our remote Hugging Face Parquet warehouse via HTTPFS, allowing the LLM to execute raw SQL against the entire Star Schema without running out of memory."

### [0:30 - 1:30] Live End-to-End Run
**Action:** Switch to your terminal window. Type `python3 run_agent_demo.py` but don't hit enter yet.
**Script:**
"I'm going to run a live end-to-end demo of the agent right now using a Python test harness I built."
*(Hit Enter to run the script)*
"As you can see, the agent is exposing the true warehouse schema to the LLM. Then, it triggers the `find_decaying_content` tool for a specific client. Under the hood, DuckDB is remotely aggregating the June 2026 partition over HTTP, instantly pulling out the top 5 high-impression, low-CTR decaying URLs out of millions of records."

### [1:30 - 2:30] Design Decision (Required Criteria)
**Action:** Switch to the code editor showing `mcp_seo_server.py`, specifically highlighting the DuckDB HTTPFS connection setup.
**Script:**
"I want to highlight a critical design decision here. I chose to use DuckDB with the `httpfs` extension rather than downloading the dataset locally or using Pandas. This decision was mandatory because the raw dataset is gigabytes of columnar Parquet data. By using DuckDB, the execution engine pushes the `WHERE` clauses down over the network, so it only pulls the specific client's bytes into memory. It turns an impossible Big Data problem into a fast, agentic workflow."

### [2:30 - 3:30] Limitations & Guardrails (Required Criteria)
**Action:** Switch back to the `AGENT_README.md` and highlight the Limitations list.
**Script:**
"However, being honest about where this breaks is critical. One major limitation of this v2 agent is that it lacks a caching layer. Every time the LLM calls a tool, it makes a fresh HTTP request to Hugging Face. If the LLM makes a mistake and loops, or repeatedly asks the same question, it will waste significant network bandwidth and latency. In v3, I plan to introduce a local Redis or SQLite cache so repeat queries resolve in milliseconds."

### [3:30 - 4:00] Outro
**Action:** Briefly show the `run_agent_demo.py` code to prove it works.
**Script:**
"Overall, this agent bridges the gap between massive production data warehouses and LLMs. Thanks for watching!"

---
**After Recording:** Stop the recording, upload it as an *Unlisted* video to YouTube, and submit the link along with the `AGENT_README.md` file.
