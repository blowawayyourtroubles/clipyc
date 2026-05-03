# CLIPYC (CLI Python Checklist)

CLIPYC is a command-line program for users comfortable working in the terminal.
Create tasks, assign priorities, organize by due date, and keep track of
what's done — all from the command line, with support for JSON and CSV formats.

## Features

- Add tasks with a title, priority level, and optional due date
- Mark tasks as done or pending
- List tasks filtered by status or sorted by priority / due date
- Export and import your checklist in JSON or CSV format

## Usage

```bash
python lista.py add "Estudiar APIs" --priority high --due 2025-06-01
python lista.py list --sort priority
python lista.py list --sort due_date
python lista.py list --filter done
python lista.py done 3
python lista.py export --format csv
```

## Priority Levels

Tasks support three priority levels: `high`, `medium`, `low`

## File Formats

- **JSON** — default storage format
- **CSV** — available for export/import, useful for opening in spreadsheets
