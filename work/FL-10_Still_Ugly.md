# FL-10: "Ship the Ugly One" - Review & Reflection

## The "Still Ugly" List
I've shipped the first iteration of my true identity single-page portfolio. While the structure, CSS grids, and real content are live, I know these elements are still rough and unpolished:

1. **Mobile Navigation:** The navigation bar works well on desktop, but on mobile devices, the links squish together uncomfortably. I need to implement a proper hamburger menu.
2. **Dark Mode:** I work heavily in AI/DL, and dark mode is essential for developer tools. The site is currently stuck in a light/white theme (`#FAFAFA`) without a dark mode toggle or `prefers-color-scheme` CSS implementation.
3. **Animations/Interactions:** The page is completely static HTML. Adding subtle fade-in animations on scroll (using intersection observers) would make the case studies feel much more premium and dynamic.
4. **Project Links:** A few projects just point to my main GitHub profile rather than specific detailed readmes or live deployment links (like MedFlow-V2).

## Peer Feedback (The Reaction)
*I sent the live URL to a fellow software engineer for a quick, brutal 5-minute review.*

**What they saw:** 
"I clicked the link, and the bold hero statement hit me immediately. I scrolled straight down and checked out the Open Generative AI and MedFlow-V2 cards."

**What confused them / What didn't work:** 
"The UI is a bit too 'clean' to the point of feeling slightly plain. Since you're building GenAI tools and computer vision pipelines, they expected some sort of interactive visualization, particle effect, or dark-mode hacker aesthetic rather than a standard white grid."

**Did the work land?:** 
"Yes. The content carries the weight. Putting the published JAC-ECC 2025 paper and the IEEE technical writing right next to the GitHub code showed a rare bridge between academic research and actual production software engineering."
