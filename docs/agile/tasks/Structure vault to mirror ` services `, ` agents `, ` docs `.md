## 🛠️ Task: Document-Driven Development for Service Scripts

We are following a **document-driven development** process.  
This means **each program file must have a corresponding documentation file** that fully describes its behavior, purpose, and relationships—*before or alongside implementation*.

Our documentation structure should **mirror the code structure** one-to-one.  
These docs should be so complete and precise that any developer (or LLM) could rebuild the system from documentation alone.

---

## 🎯 Goals

- Every program file has a corresponding documentation file
- Each document fully describes:
  - The script's purpose
  - Its internal logic and structure
  - Its role in the larger system
- Documents include **bi-directional links** to relevant dependencies and dependents
- Enables better AI pair programming, onboarding, and debugging

---

## 📦 Requirements

- [ ] Folder structure for docs matches `services/`, `shared/`, etc.
- [ ] Every source file has a `README.md`, `DOC.md`, or `.note.md` style doc
- [ ] Docs are written in Obsidian-compatible markdown
- [ ] Links to dependencies and dependents use [wiki-style](wiki-style.md) links
- [ ] Documents include commentary on design intent, not just implementation
- [ ] Each file should follow the [file.doc.template](../../templates/file.doc.template.md) structure.

---

## 📋 Subtasks

- [ ] Create matching folder structure in `docs/` or `notes/` (or use vault-wide)
- [ ] For each existing script:
  - [ ] Create corresponding markdown file
  - [ ] Describe its internal logic clearly
  - [ ] Explain its role in the larger system
  - [ ] Link to:
    - [ ] Files it *depends on*
    - [ ] Files that *depend on it*
- [ ] Add tags for epics, services, and layers (e.g. #cephalon, #layer1)

---

## 🔗 Related Epics

#cicd #buildtools #devtools #devops  
#documentation #knowledge-graph #docdrivendev

---

## ⛓️ Blocked By

Nothing

## ⛓️ Blocks

- Automated documentation generation
- LLM prompt generation from doc tree
- CI/CD config templating

---

## 🔍 Relevant Links

- [promethean-doc-structure](promethean-doc-structure.md)
- [project-file-structure](project-file-structure.md)
- [doc-template](doc-template.md)
- [docdrivendev-principles](docdrivendev-principles.md)
