# FL-01: AI Workflow Audit and Tool Setup

## Part 1: AI Workflow Audit (12 Recurring Tasks)

| Recurring Task | Classification | Rationale |
| :--- | :--- | :--- |
| **1. Deciding final ML model architecture for production** | **Just Me** | AI doesn't know my specific business constraints, compute limits, or deployment costs. |
| **2. Final code review before deploying to production** | **Just Me** | Accountability and safety fall 100% on me; AI can miss subtle business logic errors. |
| **3. Writing Python boilerplate and setup scripts** | **Fully Automate** | It's repetitive, zero-value work that doesn't require deep thinking. |
| **4. Generating regex patterns for NLP text cleaning** | **Fully Automate** | AI is objectively faster and more accurate at writing regex from natural language than I am. |
| **5. Debugging cryptic PyTorch/TensorFlow errors** | **Delegate to AI with review** | It parses stack traces instantly, but I must review the fix so it doesn't just mask the root cause. |
| **6. Refactoring messy Jupyter notebooks into clean scripts** | **Delegate to AI with review** | Great at extracting functions, but I must ensure the data flow logic remains intact. |
| **7. Writing SQL/DuckDB queries for data extraction** | **Delegate to AI with review** | Fast at generating the syntax, but I need to double-check the JOINs and grain logic. |
| **8. Writing docstrings and code comments** | **Delegate to AI with review** | It understands the code structure, but I just need to verify the context is accurate. |
| **9. Brainstorming system architecture for a new CV pipeline** | **Collaborate with AI** | Excellent for bouncing ideas and finding edge cases I haven't considered. |
| **10. Reading/Synthesizing new ML/DL research papers** | **Collaborate with AI** | I use it to summarize the core math, but I read the methodology myself to verify. |
| **11. Drafting emails to recruiters or hiring managers** | **Collaborate with AI** | Good for breaking writer's block, but I rewrite it to sound like my actual voice. |
| **12. Structuring my portfolio and resume narrative** | **Collaborate with AI** | Acts as an interviewer to help me find the sharpest angle for my "Jack of all trades" skills. |

---

## Part 2: Three Target Tasks (For FL-02 to FL-04)

These three tasks are selected for deeper AI integration over the next 3 weeks.

**1. Refactoring messy Jupyter notebooks into clean Python scripts**
* **What "Done Well" means:** The AI generates a `.py` script that runs without errors, strictly follows PEP-8 formatting, and extracts the notebook's core logic into modular, reusable functions without hallucinating new data pipelines.

**2. Brainstorming system architecture for new pipelines**
* **What "Done Well" means:** The AI acts as a Senior Staff Engineer and provides 3 distinct viable architectural options, detailing the specific pros and cons of each regarding latency, compute cost, and scalability.

**3. Reading/Synthesizing new ML/DL research papers**
* **What "Done Well" means:** The AI reads a PDF paper and outputs a highly dense summary: the core contribution, the dataset used, the baseline they beat, and 2 potential ways to apply it to my current projects, all in under 5 bullet points.

