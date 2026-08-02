# "Where It Breaks" Portfolio Audit

## Fixed Immediately (Fix-Nows)
1. **Missing SEO & Social Previews**: The site lacked `<meta>` descriptions and OpenGraph tags, meaning links shared on LinkedIn or Twitter would appear as generic blank links. **Fix applied**: Added comprehensive description, OG:title, OG:description, and OG:image tags to the `<head>`.
2. **Missing Favicon**: The browser tab icon was the default globe, which hurts professional credibility. **Fix applied**: Injected a clean, lightweight SVG favicon.
3. **No Graduate Proof**: The site didn't link back to FlyRank verification. **Fix applied**: Installed the FlyRank AI Fluency Graduate badge in the footer linking to the official verification page.

## Known Limitations (To Fix Later)
1. **Mobile Navigation Overcrowding**: If the screen width drops below 400px, the desktop-style `<nav>` links squish together. **Limitation noted**: Need to implement a CSS media query and JavaScript toggle for a proper hamburger menu.
2. **Missing Empty/Error States**: The portfolio is entirely static. If a user disables CSS or an image fails to load, the layout might break unexpectedly. **Limitation noted**: Need to add proper fallback fonts and `alt` text to all external resources.
3. **No Dark Mode**: As noted in my "Still Ugly" reflection, the site is stuck in Light Mode (`#FAFAFA`). **Limitation noted**: Will require a CSS refactor using CSS variables (e.g., `var(--bg-primary)`) and a `prefers-color-scheme` media query to implement true dark mode.
