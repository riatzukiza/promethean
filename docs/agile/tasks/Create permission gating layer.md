## 🛠️ Task: Create permission gating layer

Introduce a middleware layer that checks whether an action or
information request is allowed before it reaches core services. This
is based on the "Dorian Permission Gate" equations in our math notes.

---

## 🎯 Goals

- Prevent unauthorized commands from propagating through the system
- Allow per-agent rule sets and default fallbacks
- Log gate denials for auditing

---

## 📦 Requirements

- [ ] Implement gate logic as a Python module (`shared/py/permission_gate.py`)
- [ ] Support weight/threshold config via YAML
- [ ] Expose a simple `check_permission(agent, action)` API
- [ ] Document schema expectations in [AGENTS.md](../../AGENTS.md)

---

## 📋 Subtasks

- [ ] Translate the Dorian equation from [symbolic-gravity-models](../../notes/math/symbolic-gravity-models.md)
- [ ] Add unit tests for grant/deny cases
- [ ] Tie into Cephalon’s command router

---

## 🔗 Related Epics

#framework-core

---

## ⛓️ Blocked By

- Requires agreement on permission schema in `AGENTS.md`

## ⛓️ Blocks

- Future multi-user interfaces

---

## 🔍 Relevant Links

- [kanban](../boards/kanban.md)

## ❓ Questions

- What format should permission rules use—YAML or JSON?
- Do we need real-time updates or is a static config sufficient?
#blocked
