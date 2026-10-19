"""Render the public connector guide as a dependency-light static documentation site."""

from html import escape
from pathlib import Path
import re

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "docs/claude-connector.md").read_text()
renderer = MarkdownIt("commonmark", {"html": False}).enable("table")
tokens = renderer.parse(source)
navigation = []
for index, token in enumerate(tokens):
    if token.type != "heading_open":
        continue
    title = tokens[index + 1].content
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    token.attrSet("id", slug)
    if token.tag == "h2":
        navigation.append(f'<a href="#{slug}">{escape(title)}</a>')
content = renderer.renderer.render(tokens, renderer.options, {})
page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Connect Claude to NETIX.AI: OAuth setup, tools, examples, data handling and troubleshooting.">
  <title>NETIX.AI connector for Claude · Documentation</title>
  <link rel="stylesheet" href="style.css">
  <link rel="canonical" href="https://netix-ai-oss.github.io/documentation/">
</head>
<body>
  <a class="skip" href="#guide">Skip to guide</a>
  <header>
    <a class="brand" href="https://www.netix.ai">NETIX<span>.AI</span></a>
    <span class="section-label">Documentation</span>
    <a class="brochures" href="https://www.netix.ai/brochures-and-guides">Brochures &amp; guides ↗</a>
  </header>
  <div class="layout">
    <aside aria-label="Guide navigation">
      <p class="eyebrow">Claude connector</p>
      <nav aria-label="On this page">NAVIGATION</nav>
      <a class="source" href="https://github.com/NETIX-AI-OSS/documentation">View on GitHub ↗</a>
    </aside>
    <main id="guide">CONTENT</main>
  </div>
  <footer>NETIX.AI · <a href="mailto:support@netix.ai">Support</a> · <a href="https://www.netix.ai/privacy-policy">Privacy policy</a></footer>
</body>
</html>
'''
page = page.replace("NAVIGATION", "\n".join(navigation)).replace("CONTENT", content)
(ROOT / "docs/index.html").write_text(page)
print(f"Built docs/index.html: {len(tokens)} Markdown tokens, {len(navigation)} sections")
