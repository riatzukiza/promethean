## 🛠️ Task: Set up Makefile for Python + JS build test dev

A unified Makefile (or equivalent script) will streamline development. It should bootstrap dependencies, start services, run tests and clean artifacts.

---

## 🎯 Goals
- Provide a quick `setup` target for all services
- Allow starting and stopping each service individually
- Offer a single command to run tests across languages
- Keep the workflow cross platform when possible

---

## 📦 Requirements
- [x] `setup` installs dependencies for all services
- [x] `start` and `stop` manage processes via PM2
- [x] `start:<service>` and `stop:<service>` for granular control
- [x] `test` aggregates Python and JS test suites
- [x] `clean` removes build artifacts

---

## 📋 Subtasks
- [x] Inventory current service start commands
- [x] Draft initial Makefile structure
- [x] Integrate PM2 ecosystem config
- [x] Document usage in the root `README.md`

---

## 🔗 Related Epics
#cicd #buildtools #devtools #devops

---

## ⛓️ Blocked By
Nothing

## ⛓️ Blocks
- Future CI automation

---

## 🔍 Relevant Links
- [kanban](../boards/kanban.md)

#tags: #agile #task
