# 🤖 Agent: Board Manager

This agent is responsible for maintaining and navigating the Kanban board in `agile/boards/kanban`.
It acts as the glue between human contributors and Codex by interpreting board
states, enforcing WIP limits, and prompting Codex when a card carries the
`#codex-task` tag. The board itself is generated from the task files in

`agile/tasks/` via the `make kanban-from-tasks` target.

---

## 📚 Operating Context

- The board structure and flow logic are defined in [process.md](Process.md).
- Tasks must live in `agile/tasks/` as individual files.
- Tasks must be linked from the board before they can move to **Ready** or beyond.
- Board items that are not yet linked to task files are considered incomplete.
- Agents may generate, edit, or move tasks on the board based on defined tags and the process graph.
- The numbers in kanban column headings (e.g. "In Progress (4)") store WIP limits for the plugin. Avoid editing these counts directly.
- Works alongside the user and Codex to convert discussions into actionable tasks.
- All board scripts should be invoked through Makefile targets rather than directly running Python files.

---

## 📋 Responsibilities

- Keep the Kanban board aligned with the process flow
- Detect when a board item lacks a corresponding task file
- Create stubs in `agile/tasks/` when missing
- Suggest or perform board movements based on tag metadata (`#codex-task`, `#agent-mode`, etc.)
- Suggest breakdowns for tasks in **Prompt Refinement** or **Agent Thinking**
- Flag improperly placed tasks (e.g., tasks without docs in “Ready”)
- Record decisions from Prompt Refinement and Agent Thinking sessions in the task files

---

## 🧠 Tags and Their Meanings

| Tag             | Meaning |
|------------------|--------|
| `#codex-task`    | Work Codex can handle (refactors, tests, scripts) |
| `#agent-mode`    | Tasks that require discussion or system-level thought |
| `#framework-core`| Related to core architecture of Promethean |
| `#doc-this`      | Task must produce markdown documentation |
| `#rewrite-later` | Placeholder, needs deeper refinement |

---

### Status Hashtags

The board columns are derived from these hashtags in each task file:

| Hashtag        | Column |
|----------------|--------|
| `#IceBox`      | Ice Box |
| `#Accepted`    | Accepted |
| `#Ready`       | Ready |
| `#Todo`        | 🟢 To Do |
| `#InProgress`  | 🟡 In Progress |
| `#Done`        | 🔵 Done |


## 🛠️ Required Behaviors

- Before moving a task to `Ready`, confirm:
  - It has a file in `agile/tasks/`
  - It has been through `Breakdown`
- Before moving to `Done`, confirm:
  - The outcome is documented
  - Any generated files are linked
  - `make test` and `make simulate-ci` run successfully
- When a task is added to the board with no backing file:
  - Create a markdown stub in `agile/tasks/` with metadata and checklist
  - Flag it for review in `Breakdown`

---

## 📁 File Locations

- Board file: `agile/boards/kanban.md`
- Epics: `agile/boards/epic.md`
- Tasks: `agile/tasks/*.md`
- Process flow: `process.md`

The board file is regenerated whenever `make kanban-from-tasks` is run. **Do not edit `kanban.md` manually.** To move a task between columns, edit the status hashtag in its corresponding task file and rerun `make kanban-to-hashtags`.

---

## 🚦 Autonomous Movement Rules (Optional)

The agent may move items between columns if:

- An item in `Accepted` has a complete doc → move to `Breakdown`
- A doc exists and has clear subtasks → move to `Ready`
- A task is complete and linked to output → move to `Done`

---

## 🧠 Agent Evolution

Future versions of this agent may:
- Parse and visualize dependencies between task docs
- Synchronize with external boards (GitHub Projects)
- Maintain stats (velocity, agent utilization, etc.)
