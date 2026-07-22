# Voice Card
**Rigorous, technical, practical, no-nonsense, execution-focused.**

---

# Case Study 1: Content Opportunity Scoring Model

**The Problem:**
Content teams waste thousands of hours manually guessing which declining pages to update to regain traffic. The existing hand-written rule was incredibly brittle and only accurately identified declining pages 24% of the time. The business needed a way to predictably point editors to the highest-ROI work.

**What I Did (And Decided):**
Instead of just running a generic classification model, I framed this as a supervised scoring task. I cleaned 30,000 rows of trailing 90-day analytics data and trained a Random Forest model. My core architectural decision was picking the right metric: I optimized specifically for **Precision@50** instead of overall accuracy. Why? Because the content team only has the bandwidth to update 50 pages a month; they don't care about the accuracy of page #14,000 in the queue. I also stripped out product-defined flags to prevent data leakage and ensure the model was learning reality, not circular logic.

**The Outcome:**
The deployed model achieved a Precision@50 of 74%—more than 3x better than the baseline rule. When this pipeline tells an editor to spend 4 hours refreshing a page, it's virtually guaranteed that the page actually needed it.

---

# About The Builder (Bio)
I am an AI Specialist and the Head of Deep Learning at Mecha ML. I bridge the gap between academic research and production engineering. With deep expertise across Computer Vision, NLP, and Medical Imaging, I don't just understand the theoretical math behind state-of-the-art models—I know how to architect, optimize, and deploy them to solve immediate, high-stakes business problems. I am a Kaggle Expert who thrives on bringing order to messy datasets and shipping robust AI pipelines.

---

# The Action (Contact / CTA)
Whether you need rigorous AI research or a deployed production pipeline, I can build it. Stop endlessly planning your AI features. Email me to build them. [Contact Assem](mailto:assemelqersh@gmail.com) | [View GitHub](https://github.com/Assem-ElQersh)

---

# The "Before / After" AI Edit
**Generic AI Draft:** "I leveraged cutting-edge machine learning algorithms to synergize data streams and optimize content delivery."
**My Edited Version:** "I trained a Random Forest model to score 30,000 pages and tell editors exactly which 50 to fix first."
