# "Where It Breaks" Audit & Triage

I actively audited both the static portfolio HTML and the dynamic MCP Agent Server (`mcp_seo_server.py`) with empty inputs, garbage data, and edge-case testing.

## Fixed Immediately (Fix-Nows)

1. **CRITICAL: SQL Injection Vulnerability in Agent** 
   - *How it broke:* When testing the MCP server (`find_decaying_content`), submitting garbage input like `'; DROP TABLE...` directly injected it into the SQL string `f"WHERE client_hash_id = '{client_id}'"`.
   - *Fix applied:* Refactored the Python server to use DuckDB's parameterized query execution (`con.execute(query, [client_id])`), completely sanitizing the input.

2. **Dead Image Links in Portfolio**
   - *How it broke:* The portfolio was hardcoding images to `https://assemelqersh.com/...` which is an inactive domain, causing images to timeout and break the layout visually.
   - *Fix applied:* Swapped the dead domain links with reliable, permanent high-quality placeholders from Unsplash.

3. **Missing SEO & Social Previews** 
   - *How it broke:* The site lacked `<meta>` descriptions and OpenGraph tags. Links shared on LinkedIn would appear as a generic blank box, destroying findability.
   - *Fix applied:* Added comprehensive `<meta>` tags and OpenGraph tags to the `<head>`.

## Known Limitations (To Fix Later)

1. **Dangerous Agent Capability (`execute_sql_query`)** 
   - *Where it breaks:* The `execute_sql_query` tool in the MCP server allows the LLM to run arbitrary SQL. While I blocked `DROP/DELETE`, DuckDB can still be tricked into reading local files (e.g., `read_csv('/etc/passwd')`) or scraping environment variables.
   - *Limitation noted:* This tool is dangerous if exposed to a public-facing LLM. It needs a strict read-only sandbox or removal before production deployment.

2. **Mobile Navigation Overcrowding** 
   - *Where it breaks:* If the screen width drops below 400px, the desktop-style `<nav>` links just flex-wrap onto multiple lines, taking up too much vertical screen real estate.
   - *Limitation noted:* Need to implement a CSS media query and JavaScript toggle for a proper hamburger menu for narrow screens.

3. **No Dark Mode** 
   - *Where it breaks:* The site is stuck in Light Mode (`#FAFAFA`).
   - *Limitation noted:* Will require a CSS refactor using CSS variables (e.g., `var(--bg-primary)`) and a `prefers-color-scheme` media query to implement true dark mode.
