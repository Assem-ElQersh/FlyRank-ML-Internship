# FL-08: Ship an Automation Workflow v2

## Workflow: The ArXiv Paper Distiller
**Type:** Source-Grounded Study Notes
**Objective:** Reduce the time it takes a Senior Deep Learning Engineer to evaluate if a newly published ArXiv paper is worth implementing in production.

### Step Diagram (The Pipeline)
1. **Gather & Ground (NotebookLM):** Download the ArXiv PDF and upload it to a dedicated NotebookLM instance. This strictly grounds the extraction to the paper's text, preventing hallucinations.
2. **Critique & Synthesize (Claude Project):** Paste the NotebookLM output into a specialized Claude prompt that acts as a cynical Staff Engineer, hunting for flaws in the methodology.
3. **Format & Archive:** Save the output into a clean Markdown template in my personal knowledge base (Obsidian) for future reference.

### The Prompts / Configuration
**Step 1: NotebookLM Prompt**
> "Generate a comprehensive technical briefing document. Extract the core architecture change, the exact datasets used for evaluation, and summarize the primary benchmark results."

**Step 2: Claude 'Staff Engineer' Prompt**
> "Act as a ruthless Staff ML Engineer. Review the following paper summary. Tell me:
> 1) What is the core mathematical or architectural novelty?
> 2) Why might their evaluation metrics be flawed, cherry-picked, or over-indexed?
> 3) Would this architecture realistically scale in our production pipeline at Mecha ML, considering inference latency? 
> Be extremely concise and skeptical. [Paste NotebookLM Output]"

---

## The 5 Real Runs (Inputs & Outputs)

### Run 1: LoRA: Low-Rank Adaptation of Large Language Models (Hu et al.)
* **Output Extract:** "Novelty: Freezing pre-trained weights and injecting trainable rank decomposition matrices. Flaw: Authors test on older benchmarks; doesn't account for extreme inference batching constraints. Verdict: Yes, adopt immediately for fine-tuning our internal LLMs—latency impact is negligible."

### Run 2: Direct Preference Optimization (Rafailov et al.)
* **Output Extract:** "Novelty: Bypassing the reward model in RLHF by optimizing the language model directly on preference data. Flaw: Highly sensitive to the quality of the preference dataset; garbage-in-garbage-out is amplified. Verdict: High potential, but requires us to heavily clean our human-annotated preference logs first."

### Run 3: Mamba: Linear-Time Sequence Modeling (Gu et al.)
* **Output Extract:** "Novelty: Selective State Space Models (SSMs) replacing self-attention for linear scaling. Flaw: Hardware-aware parallel scan is complex to implement efficiently on non-standard hardware. Verdict: Monitor closely, but wait for better PyTorch/CUDA kernel support before ripping out our Transformers."

### Run 4: KAN: Kolmogorov-Arnold Networks (Liu et al.)
* **Output Extract:** "Novelty: Replacing fixed activation functions on nodes with learnable activations on edges. Flaw: Extremely slow to train compared to MLPs; currently tested on toy datasets (MNIST/PDEs). Verdict: Do NOT deploy to production. Purely academic novelty at this stage."

### Run 5: YOLOv10: Real-Time End-to-End Object Detection (Wang et al.)
* **Output Extract:** "Novelty: NMS-free training using consistent dual assignments. Flaw: The accuracy gains at the smallest model scales (YOLOv10-N) are marginal compared to YOLOv8. Verdict: Test in our edge-device pipeline—eliminating NMS latency is a huge win for our real-time video feeds."

---

## Time Accounting & ROI
* **Manual Approach:** Reading and extracting technical notes from a dense ML paper takes me ~2 hours per paper. For 5 papers: **10 hours.**
* **Setup Cost:** Setting up the NotebookLM instance and refining the Claude prompt took **20 minutes**.
* **Workflow Execution:** Downloading the PDF, uploading, prompting, and formatting takes ~5 minutes per paper. For 5 papers: **25 minutes**.
* **Total Time Saved:** **9 hours and 15 minutes** (a 92% reduction in time-to-insight).

## Known Failure Points & Required Human Review
1. **Math Hallucinations:** NotebookLM occasionally struggles to correctly parse complex mathematical formulas or Greek symbols from PDFs. A human must manually verify the equations in the original PDF if the architecture relies on them.
2. **Latency Blindness:** Claude does not know our exact hardware specifications at Mecha ML. It might greenlight an architecture that technically works but exceeds our strict 50ms inference latency budget. 
3. **The 'Cherry-Picked Table' Problem:** The workflow summarizes the results the authors *chose* to highlight. A human must still physically look at the benchmark tables in the PDF to see if the authors conveniently omitted specific baselines (like skipping a comparison to an optimized ResNet).
