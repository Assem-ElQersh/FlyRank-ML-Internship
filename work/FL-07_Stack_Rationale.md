# FL-07: Stack Rationale

## The Constraints Provided to AI
1. **Cost:** 100% Free.
2. **Skill Level:** Senior AI / Deep Learning Engineer (Python heavy, minimal frontend framework desire).
3. **Portfolio Needs:** A single-page scrolling layout (Hero, FlyRank Case Study, Kaggle Experience, About/CTA).
4. **Display Needs:** Static text, high-res screenshots of dataframes, and external links to GitHub repos. No dynamic data, no backend database required.

## The Three Options Generated
1. **The Simplest (Vanilla HTML/CSS):** Build with raw HTML and CSS. Host on Netlify. No backend. *Trade-off:* Doesn't scale cleanly if I want to add 20 pages later (lots of copy/pasting).
2. **The Middle-Ground (Astro):** Build using the Astro framework where case studies are written in Markdown. Host on Vercel. No backend. *Trade-off:* Minor learning curve to learn Astro's file routing.
3. **The Most Powerful (Next.js / React):** Build a full React web app. Host on Vercel. Has backend API capabilities. *Trade-off:* Massive overkill. Too much configuration and framework maintenance for a static portfolio.

## My Final Rationale

**Chosen Stack:** Vanilla HTML & CSS hosted on Netlify.

**Why I chose it (and rejected the others):**
As a Head of Deep Learning, my value is in building rigorous ML pipelines, not React components. While Next.js (Option 3) is powerful, it is massive overkill for a single-page site and introduces framework maintenance that I simply don't want to deal with. Astro (Option 2) is a great tool for content-heavy blogs, but my content map is a single scrolling page. 

By choosing the absolute simplest stack (Vanilla HTML/CSS), I eliminate all technical debt. I can easily embed my DuckDB screenshots, style my Identity Kit with plain CSS, and guarantee I finish the build in two weeks. Most importantly: I know exactly how to maintain it, because there are no dependencies to update. It gets out of the way and lets my engineering work speak for itself.
