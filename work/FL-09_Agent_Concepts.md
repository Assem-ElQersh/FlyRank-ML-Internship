# FL-09: Agent Concepts and MCP Basics

## 1. Workflow vs. Agent

In the current AI landscape, the word "agent" is frequently abused by marketing departments to describe any system that uses an LLM. However, from an engineering perspective, there is a rigid line between a workflow and an agent, defined by **who controls the routing**.

**A Workflow** is a deterministic, predefined sequence of operations. The path is hardcoded by a human developer. Even if an LLM is used at individual nodes (e.g., to summarize text or extract entities), the transition from Step A to Step B is controlled by code or manual human intervention. If a step fails, the system stops or follows a pre-programmed error handler.

**An Agent** is an autonomous system where the LLM itself acts as the routing engine. Instead of following a hardcoded path, an agent is given a high-level goal, a set of available tools, and an environment. The LLM dynamically decides which tools to invoke, reads the output of those tools, evaluates if it is closer to the goal, and iterates until the objective is achieved. 

**Classifying my FL-08 ArXiv Paper Distiller:**
My ArXiv Paper Distiller is strictly a **Workflow**, not an agent. I defined the exact sequence of events. I manually downloaded the PDF, I uploaded it to NotebookLM, I copied the output, and I pasted it into a specialized Claude prompt. The LLMs were used purely as functional nodes within a pipeline I orchestrated. The LLM had no autonomy to decide its next step or seek out new tools.

---

## 2. What is the Model Context Protocol (MCP)?

The Model Context Protocol (MCP) is an open standard introduced to solve the fragmentation of AI tool integrations. Historically, if you wanted an LLM to read your local files, query your database, and search the web, you had to write custom, fragile API integrations for each specific LLM provider. 

MCP acts as the "USB-C port for AI applications." It provides a universal, standardized architecture that separates the AI model (the Client) from the tools and data (the Server). Once an MCP Server is built for a specific tool (like a PostgreSQL database or a Slack workspace), *any* MCP-compatible AI client (like Claude Desktop, Cursor, or specialized agent frameworks) can instantly plug into it and use it.

MCP standardizes three core primitives:
1. **Tools:** Executable functions the AI can call (e.g., `execute_sql_query`, `write_file`). The AI decides when and how to use these based on the user's prompt.
2. **Resources:** Static or dynamic data the AI can read (e.g., a local configuration file, an API endpoint response). This allows the AI to pull context on demand.
3. **Prompts:** Pre-defined templates provided by the server to help users format their requests optimally for the connected tools.

---

## 3. Upgrading the "ArXiv Paper Distiller" into an Agent

To upgrade my static FL-08 workflow into a true autonomous agent using MCP, I would need to remove the human orchestrator entirely and replace them with an LLM empowered by tools.

Currently, the workflow requires me to manually source the paper, upload it, and save the output. 

To make it an agent, I would deploy three specific MCP servers:
1. **An ArXiv API MCP Server:** Providing a `search_arxiv` and `download_pdf` tool.
2. **A PDF Parsing MCP Server:** Providing an `extract_text_from_pdf` tool.
3. **A Local Filesystem MCP Server:** Providing a `write_markdown_file` tool hooked up to my local Obsidian directory.

With these MCP servers connected to an agentic client, my input changes from manual clicking to a single, high-level command: 
> *"Review the top 5 papers published on ArXiv today under the 'cs.LG' (Machine Learning) category. For each, extract the core architectural novelty and potential flaws, and save a formatted markdown summary directly into my local Obsidian 'Daily ArXiv' folder."*

**The Agentic Loop:**
The LLM would autonomously:
1. Invoke the `search_arxiv` tool to get today's papers.
2. Loop through the results and invoke the `download_pdf` and `extract_text_from_pdf` tools for each.
3. Encounter a parsing error on a heavy mathematical paper, autonomously realize the text is garbled, and perhaps invoke a vision tool to read the PDF as an image instead (error recovery).
4. Synthesize the findings using its internal reasoning capabilities.
5. Invoke the `write_markdown_file` tool to save the final artifacts.

In this upgraded system, the LLM controls the routing, the error handling, and the tool execution. That is the threshold where a workflow becomes an agent.

---

## 4. MCP Proof of Execution (Deliverable)

*(**Note to Self:** Paste screenshots below showing Claude Desktop connected to a local MCP server (e.g., the local filesystem or SQLite server) executing 3 tool calls that chat alone could not do: e.g., reading a local file, creating a new directory, and writing a file).*

[ PASTE SCREENSHOT 1 HERE - Tool Call: Reading Local File ]

[ PASTE SCREENSHOT 2 HERE - Tool Call: Executing Query / Fetching Live Data ]

[ PASTE SCREENSHOT 3 HERE - Tool Call: Writing Local File ]
