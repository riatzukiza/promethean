## 🛠️ Task: Write board sync script

Create a small tool that pushes updates from our Obsidian kanban board to a GitHub Projects board and can optionally pull remote changes.

---

## 🎯 Goals
- Provide a CLI or GitHub Action for one-way sync
- Keep authentication minimal and configurable
- Prepare groundwork for two-way sync

---

## 📦 Requirements
- [x] Python script using the GitHub API
- [x] Reads `kanban.md` and updates project items
- [x] Supports personal access token configuration

---

## 📋 Subtasks
- [x] Parse kanban board data
- [x] Use endpoints outlined in research
- [x] Handle basic error reporting
- [x] Document usage examples

---

## 🔗 Related Epics
#framework-core

---

## ⛓️ Blocked By
- Research GitHub Projects board API

## ⛓️ Blocks
- Document board sync workflow

---

## 🔍 Relevant Links
- [kanban](../boards/kanban.md)
- [board_sync.py](../../scripts/github_board_sync.py)
- [Board Sync Workflow](../../board_sync.md)

#tags: #agile #task
