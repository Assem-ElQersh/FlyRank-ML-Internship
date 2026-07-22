# The Prompt Ladder

## Baseline (Version 0)
**Prompt:** "Write python code to find declining pages in my dataset."

**Excerpt of Output:**
```python
import pandas as pd
df = pd.read_csv('data.csv')
declining_pages = df[df['status'] == 'declining']
print(declining_pages)
```

**Notes:**
* **What changed in the prompt:** (Baseline, nothing changed yet).
* **What improved in the output:** N/A.
* **What still failed:** It hallucinated a filename (`data.csv`) and hallucinated a column name (`status`). If I run this, it will immediately crash.
* **What to try next:** Add real context about what the dataset actually looks like.

---

## Version 1: Add Real Context
**Prompt:** "I have a dataset of 30,000 SEO pages. The dataset contains historical impression data and trend flags. Write python code to find declining pages."

**Excerpt of Output:**
```python
import pandas as pd
df = pd.read_csv('seo_pages.csv')
declining_pages = df[df['trend'] == 'declining']
print(f"Found {len(declining_pages)} declining pages")
```

**Notes:**
* **What changed in the prompt:** Added real context (30,000 SEO pages, historical impressions).
* **What improved in the output:** The AI actually recognized it was an SEO context and added a nice print statement to show the count of pages.
* **What still failed:** It's still guessing the exact column names (`trend` instead of the actual `trend_direction`). The code still won't run on my real data.
* **What to try next:** Specify the exact column names and expected values.

---

## Version 2: Add Real Context (Column Names)
**Prompt:** "I have a dataset of 30,000 SEO pages. The specific columns I care about are `content_id`, `impressions_90d`, and `trend_direction`. Write a python script to filter for declining pages where `trend_direction` is 'down'."

**Excerpt of Output:**
```python
import pandas as pd
df = pd.read_csv('dataset.csv')
declining_pages = df[df['trend_direction'] == 'down']
print(declining_pages[['content_id', 'impressions_90d']])
```

**Notes:**
* **What changed in the prompt:** Specified the exact output format/columns to look for.
* **What improved in the output:** The code is now actually runnable on my specific dataset! It successfully filters using the correct logic.
* **What still failed:** It just prints a massive, unsorted list of thousands of pages. An editor can't do anything with a random list.
* **What to try next:** Add a clearer goal (ranking them by importance).

---

## Version 3: Add a Clearer Goal (Ranking)
**Prompt:** "I have a dataset of 30,000 SEO pages. The specific columns I care about are `content_id`, `impressions_90d`, and `trend_direction`. Write a python script to filter for pages where `trend_direction` is 'down', and rank them by `impressions_90d` descending."

**Excerpt of Output:**
```python
import pandas as pd
df = pd.read_csv('dataset.csv')
declining = df[df['trend_direction'] == 'down']
ranked = declining.sort_values(by='impressions_90d', ascending=False)
print(ranked.head(50))
```

**Notes:**
* **What changed in the prompt:** Added a clear goal to rank by impressions descending.
* **What improved in the output:** The output is finally actionable. It sorts the pages so the highest-impact declining pages are at the top.
* **What still failed:** The code is just a loose, procedural script. It's not reusable or modular for a production pipeline. 
* **What to try next:** Add a constraint to make it "cleaner." Let's tell it to do it in exactly one line of code to make it efficient.

---

## Version 4: Add Constraint (The "It Got Worse" Moment)
**Prompt:** "I have a dataset of 30,000 SEO pages. The specific columns I care about are `content_id`, `impressions_90d`, and `trend_direction`. Write a python script to filter for pages where `trend_direction` is 'down', and rank them by `impressions_90d` descending. Constraint: Do this in exactly one line of pandas code."

**Excerpt of Output:**
```python
ranked_pages = pd.read_csv('dataset.csv')[pd.read_csv('dataset.csv')['trend_direction'] == 'down'].sort_values(by='impressions_90d', ascending=False)
```

**Notes:**
* **What changed in the prompt:** Added a rigid constraint (exactly one line of code).
* **What improved in the output:** Absolutely nothing.
* **What still failed:** This made the code *worse*. By forcing a one-liner, the AI wrote an incredibly unreadable, inefficient chain that actually reads the CSV twice. This was a bad constraint.
* **What to try next:** Drop the silly constraint, and instead add quality criteria (role-playing as a Senior Engineer to write production code).

---

## Version 5: Add Quality Criteria
**Prompt:** "Act as a Senior ML Engineer. I have a dataset of 30,000 SEO pages. The specific columns are `content_id`, `impressions_90d`, and `trend_direction`. Write a clean, production-ready Python function with docstrings and type hints that filters for pages where `trend_direction` is 'down', ranks them by `impressions_90d` descending, and returns the top 50 results."

**Excerpt of Output:**
```python
import pandas as pd

def get_top_declining_opportunities(df: pd.DataFrame, top_n: int = 50) -> pd.DataFrame:
    """
    Filters a dataframe for declining pages and ranks them by 90-day impressions.
    
    Args:
        df: DataFrame containing 'content_id', 'impressions_90d', and 'trend_direction'.
        top_n: Number of top results to return.
        
    Returns:
        DataFrame of the top_n declining pages, sorted by impressions descending.
    """
    if not all(col in df.columns for col in ['content_id', 'impressions_90d', 'trend_direction']):
        raise ValueError("Missing required columns in dataset.")
        
    declining = df[df['trend_direction'] == 'down'].copy()
    ranked = declining.sort_values(by='impressions_90d', ascending=False)
    
    return ranked.head(top_n)
```

**Notes:**
* **What changed in the prompt:** Added quality criteria (Senior ML engineer, production-ready, docstrings, type hints).
* **What improved in the output:** Night and day difference. It went from a loose script to a robust, modular function. It even added error handling to check if the columns exist before running!
* **What still failed:** Nothing. This is ready to be merged into a pipeline.
* **What to try next:** Save this as a reusable prompt.

---

# Final Reusable Prompt
**Copy and paste this when you need data filtering scripts:**
> "Act as a Senior ML Engineer. I have a dataset containing [INSERT DESCRIPTION]. The specific columns I need to use are [INSERT EXACT COLUMNS]. Write a clean, production-ready Python function with docstrings, type hints, and basic error handling that achieves the following goal: [INSERT EXACT GOAL AND SORTING LOGIC]. Return the top [N] results."
