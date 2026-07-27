# PF-04: DNS Walkthrough

## 1. What is a CNAME Record?
A **CNAME (Canonical Name) record** is a type of DNS record that maps an alias name to a true, canonical domain name. Instead of pointing directly to an IP address (like an A record does), a CNAME points to another domain name. 

Think of it like a forwarding address. If someone tries to visit the subdomain, the CNAME record tells the internet: *"I don't have the IP address, but go ask this other domain—they know where the server is."*

## 2. My Specific CNAME Values
When my FlyRank subdomain is provisioned at the end of the capstone, the DNS record will be configured as follows:
- **Type:** CNAME
- **Name (Host):** `assemelqersh` (which resolves to `assemelqersh.flyrank.ai`)
- **Value (Target):** `assemelqersh.netlify.app`

This means any traffic hitting my official FlyRank URL will be seamlessly routed to my Netlify servers.

## 3. The Journey of a Web Request
When someone types `https://assemelqersh.flyrank.ai` into their browser, an invisible, split-second process occurs before the page loads:

1. **The Request:** The user hits enter. The browser doesn't know what IP address `assemelqersh.flyrank.ai` lives at, so it asks the operating system, which then asks a **DNS Resolver** (usually operated by the user's ISP or Google/Cloudflare).
2. **Querying the Nameservers:** The Resolver acts as a detective. It asks the Root server, which directs it to the `.ai` TLD server, which finally directs it to the **Nameserver** authoritative for `flyrank.ai`.
3. **The Record Response:** The `flyrank.ai` nameserver checks its records. It finds the **CNAME record** we created and responds to the Resolver: *"Ah, `assemelqersh.flyrank.ai` is just an alias. The real destination is `assemelqersh.netlify.app`."*
4. **The Final Lookup:** The Resolver then does a quick second lookup for `assemelqersh.netlify.app`, gets the actual Netlify IP address (A record), and hands it back to the browser.
5. **The Connection:** The browser connects to the Netlify IP address. Because I will have added `assemelqersh.flyrank.ai` as a custom domain in my Netlify settings, Netlify recognizes the incoming request, attaches the free SSL certificate for HTTPS, and serves my HTML/CSS files to the user.

## 4. Capstone Checklist
When the subdomain is granted, I will complete the connection by:
- [ ] Logging into Netlify -> Domain Management.
- [ ] Clicking "Add custom domain" and entering `assemelqersh.flyrank.ai`.
- [ ] Waiting for DNS propagation (since Ops has already set the CNAME).
- [ ] Verifying the SSL/TLS certificate padlock is active.
