## 🛠️ Task: Update Makefile to have commands specific for agents

The monorepo hosts multiple agents. The Makefile should expose targets to launch or test each agent individually as referenced in the migration plan.

Agents will be there own kind of unit with in the system.

There are going to be "shared" services, and there are going to be services specific to an agent...
But not really. no. It should be that the services that I am thinking would be specific simply have ways for the agents who use them to flag their messages as coming from them so they can be routed accordingly.
It's too complicated to seperate this idea of "agents", "Agent specififc services", and "shared services" when there are also suposed to be "shared" libraries.

---

## 🎯 Goals
- `make start:duck` or similar commands
- Reusable patterns for any future agent

---

## 📦 Requirements
- [ ] Define agent-specific PM2 targets
- [ ] Document usage in the root README

---

## 📋 Subtasks
- [ ] Extend current Makefile with per-agent start/stop
- [ ] Provide example for Duck
- [ ] Add placeholder for new agents

---

## 🔗 Related Epics
#devops

---

## ⛓️ Blocked By
- update GitHub Actions to use makefile

## ⛓️ Blocks
Nothing

---

## 🔍 Relevant Links
- [kanban](../boards/kanban.md)
- [MIGRATION_PLAN](../MIGRATION_PLAN.md)
- [write simple ecosystem declaration library for new agents](write%20simple%20ecosystem%20declaration%20library%20for%20new%20agents.md)
#breakdown
