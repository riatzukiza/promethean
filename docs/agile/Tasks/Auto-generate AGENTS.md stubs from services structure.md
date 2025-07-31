## 🛠️ Task: Auto-generate AGENTS.md stubs from services structure

Build a small script that scans `services/` and produces initial `AGENTS.md` files for each service. These stubs should include minimal metadata and links back to implementation files.

---

## 🎯 Goals

- Ensure every service has a corresponding documentation stub
- Keep docs up to date as services are added or removed
- Provide a foundation for more detailed service docs

---

## 📦 Requirements

- [ ] Script can be run via `npm run build:docs` or similar
- [ ] Output files go to `docs/services/<service>/AGENTS.md`
- [ ] Include service description, path, and tags

---

## 📋 Subtasks

- [ ] Enumerate existing services
- [ ] Generate stub for each service
- [ ] Add instructions to `docs/vault-config-readme.md`

---

## 🔗 Related Epics

#framework-core

---

## ⛓️ Blocked By

Nothing

## ⛓️ Blocks

Nothing

---

## 🔍 Relevant Links

- [vault config readme](../../vault-config-readme.md)
- [kanban](../boards/kanban.md)
#incoming
