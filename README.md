# NETIX.AI documentation

Public documentation for NETIX.AI integrations.

- [NETIX.AI connector for Claude](https://netix-ai-oss.github.io/documentation/)
- [Brochures and guides](https://www.netix.ai/brochures-and-guides)
- [Connector guide source](docs/claude-connector.md)

## Update the guide

Edit `docs/claude-connector.md`, then regenerate the static site:

```sh
uv run --with markdown-it-py==4.0.0 python scripts/build_docs.py
```

Commit the Markdown source and generated `docs/index.html` together. GitHub Pages
publishes the `docs/` directory from `main`. The site has no JavaScript, analytics,
cookies or authentication.

Never add reviewer passwords, tokens, customer records or internal deployment
configuration to this public repository.
