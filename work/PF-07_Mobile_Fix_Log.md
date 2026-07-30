# PF-07: Mobile Fix Log

## Audit Findings
- **Mobile Navigation:** The CSS media query was hiding all navigation links (`display: none`) on mobile devices, making the site unusable.
- **Layout Spills:** The Hero `h1` font size and `padding` were too large, pushing content off-screen. The profile image had a hardcoded width of `250px` which spilled on very small screens.
- **Accessibility & UX:** Buttons lacked sufficient tap-target padding for comfortable thumb use.
- **Performance:** Images below the fold lacked lazy loading, blocking the initial page render.

## Implemented Fixes
1. **Responsive Navigation:** Rewrote the `@media (max-width: 768px)` block to stack the navigation logo and flex-wrap the links, ensuring they remain visible and usable.
2. **Viewport Scaling:** Reduced the mobile `h1` font size to `2.25rem` and hero padding to `4rem 5%`.
3. **Image Constraints:** Updated the profile image to use `max-width: 100%; aspect-ratio: 1/1` to prevent horizontal scrolling on mobile.
4. **Enhanced Tap Targets:** Increased button padding (`1rem 1.5rem`) on mobile screens to meet minimum a11y touch standards.
5. **Lazy Loading:** Added `loading="lazy"` attributes to the `index.html` `<img>` tags below the fold to improve LCP (Largest Contentful Paint) speeds.
