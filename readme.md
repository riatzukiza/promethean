# Promethean Framework

This repository contains a modular multi‑agent architecture. To start shared infrastructure like speech services, run pm2 with the root configuration:

```bash
pm2 start ecosystem.config.js
```

Then start individual agents, for example Duck, using the agent config:

```bash
pm2 start agents/ecosystem.config.js
```

Set `AGENT_NAME` in your environment before launching agent services to isolate collections and data.
