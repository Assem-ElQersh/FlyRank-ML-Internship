# FL-02: Prompting Fundamentals on Real Tasks v2

**Target Task (from FL-01):** Refactoring messy Jupyter notebooks into clean Python scripts.

---

## Baseline
**Prompt:** "Refactor this jupyter notebook code."
**Excerpt of Output:**
```python
# The AI just spits back the same procedural code, maybe putting it inside one giant function without fixing any of the underlying structural issues or hardcoded variables.
def run_all():
    df = pd.read_csv('local_path.csv')
    ...
```
**Note (What changed / why):** This is the naive baseline. The output is useless because it doesn't know *how* I want it refactored, so it just guesses and wraps the spaghetti code in a single function.

---

## Version 1: Role Assignment
**Prompt:** "Act as a strict Senior Staff Python Engineer. Refactor this jupyter notebook code."
**Excerpt of Output:**
```python
# Output now includes type hints and PEP-8 formatting.
def process_data(filepath: str) -> pd.DataFrame:
    ...
```
**Note (What changed / why):** Added Role Assignment. The output immediately improved in syntax quality—it started using type hints and proper PEP-8 formatting because "Senior Engineers" write typed code.

---

## Version 2: Context and Motivation
**Prompt:** "Act as a strict Senior Staff Python Engineer. Refactor this jupyter notebook code. We need to deploy this script to run automatically in production every night, so it must be modular and reliable."
**Excerpt of Output:**
```python
import logging
logging.basicConfig(level=logging.INFO)

def process_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError as e:
        logging.error(f"Data missing: {e}")
```
**Note (What changed / why):** Added Context and Motivation. The output fundamentally shifted from just "clean code" to "safe code," voluntarily adding `logging` and `try/except` blocks because it understands the context of a nightly production job.

---

## Version 3: Few-Shot Examples
**Prompt:** "Act as a strict Senior Staff Python Engineer. Refactor this jupyter notebook code for a nightly production job. 
Example of bad code: `df = pd.read_csv('data.csv')`
Example of good code: `def load_data(path: Path) -> pd.DataFrame:`"
**Excerpt of Output:**
```python
from pathlib import Path

def load_data(path: Path) -> pd.DataFrame:
    ...
```
**Note (What changed / why):** Added Few-Shot Examples. The output directly adopted the exact `pathlib.Path` syntax from my example instead of using string paths, proving that showing is faster than telling.

---

## Version 4: Output Structure
**Prompt:** "Act as a strict Senior Staff Python Engineer. Refactor this jupyter notebook code for a nightly production job. [Examples provided]. 
Output the exact refactored Python script in a single code block, and follow it with a bulleted Markdown list of the architectural changes you made."
**Excerpt of Output:**
```python
[Full Python Script]
```
* **Architectural Changes:**
* Extracted data loading into a distinct function.
* Replaced hardcoded strings with environment variables.
**Note (What changed / why):** Added Output Structure. The AI stopped burying the code inside long, conversational paragraphs and neatly separated the deliverable from the explanation.

---

## Version 5: Step Decomposition
**Prompt:** "Act as a strict Senior Staff Python Engineer. Refactor this jupyter notebook code for a nightly production job. [Examples]. [Output Structure].
To do this:
1. First, identify all hardcoded variables and extract them to a config dict.
2. Second, isolate data-loading from data-processing.
3. Third, wrap the execution in a `if __name__ == '__main__':` block."
**Excerpt of Output:**
```python
CONFIG = {"data_path": "data.csv"}
...
if __name__ == '__main__':
    main()
```
**Note (What changed / why):** Added Step Decomposition. The output logic became flawless. By forcing the AI to process the refactoring in steps, it didn't miss extracting the hardcoded variables (which it often skipped in earlier versions).

---

## Cross-Model Comparison (Claude vs ChatGPT)
I ran the final Version 5 prompt through both Claude 3.5 Sonnet and ChatGPT (GPT-4o). 
* **Structure:** Claude followed the Output Structure constraint perfectly, giving me exactly one code block and a bulleted list. ChatGPT broke the rule by adding a conversational "Sure, I can help!" intro and a "Let me know if you need anything else!" outro.
* **Accuracy:** Both successfully implemented the `if __name__ == '__main__'` block, but Claude was much better at Step Decomposition. ChatGPT missed extracting a hardcoded integer inside a pandas filter, whereas Claude correctly pulled every hardcoded value into the global `CONFIG` dictionary as instructed in Step 1.
* **Tone:** Claude maintained the "strict Senior Engineer" persona, keeping the text dense and technical. ChatGPT drifted into a friendly customer-service tone. 

---

## Final Reusable Template
**Copy and paste this when refactoring notebooks:**
> Act as a strict Senior Staff Python Engineer. Refactor the following Jupyter notebook code. We need to deploy this script to run automatically in production, so it must be modular and reliable.
>
> Example of what I want to avoid: `df = pd.read_csv('data.csv')`
> Example of what I want to see: `def load_data(path: Path) -> pd.DataFrame:`
>
> Process the refactoring using these steps:
> 1. Identify all hardcoded variables/paths and extract them to a global config dictionary.
> 2. Isolate data-loading logic from data-processing logic into separate functions.
> 3. Wrap the execution in an `if __name__ == '__main__':` block.
>
> **Output format constraints:** Provide the refactored script in exactly one continuous code block. Below the code block, provide a bulleted list of the architectural changes you made. Do not include conversational filler.
> 
> **[INSERT JUPYTER NOTEBOOK CODE HERE]**
