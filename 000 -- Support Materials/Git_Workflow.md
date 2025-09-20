# 📝 Git Workflow Cheat Sheet — Worlds by the Numbers

This file provides a quick reference for using Git with the WBN Vault.  
Keep this in the repo so **Future You** (or collaborators) can sync, commit, and push without friction.  

---

## 📂 Starting a Session
1. Open the Vault folder in **Terminal**:  
   - In Finder → right-click folder → *Services* → **New Terminal at Folder**.  
   - Or open VS Code at the repo root and use its integrated terminal.

2. Pull latest changes from GitHub (in case edits happened elsewhere):  
   ```bash
   git pull
   ```

---

## ✍️ During a Session
- Work normally in Obsidian or your editor.  
- Save new/edited `.md` files in the repo.  

---

## ✅ Ending a Session (Commit & Push)
Always commit at the end of a writing/editing session:

```bash
git add -A
git commit -m "Session summary (e.g., Glossary v1.21 – 24 new terms)"
git push
```

That’s it — changes are now backed up to GitHub.  

---

## 📌 Commit Message Conventions
Keep messages short but clear. Suggested prefixes:  
- `[Glossary] vX.YY update – N new terms`  
- `[Coverage] Dashboard vX – status updated`  
- `[Symbols] Index vX – added constants`  
- `[Meta] Snapshot vX – save point`  

Examples:  
```bash
git commit -m "[Glossary] v1.21 – 24 new terms"
git commit -m "[Coverage] v0.3 – added Vol.0"
git commit -m "[Symbols] v0.2 – constants + time units"
```

---

## 🔍 Checking Status
To see what’s changed but not yet committed:  
```bash
git status
```

To view recent commit history (compact):  
```bash
git log --oneline --graph
```

---

## 🚫 What to Ignore (via .gitignore)
The repo should track Markdown **only** as source.  
Ignore:  
- Exports (`*.pdf`, `*.zip`, `*.docx`, `*.epub`)  
- Graphics (`*.png`, `*.jpg`, `*.webp`, `.afdesign`)  
- Spreadsheets (`*.xlsx`, `*.xltx`)  
- Obsidian system files (`.obsidian/`)  

---

## 🚀 Best Practice Ritual
- **Start of session:** `git pull`  
- **End of session:** `git add -A && git commit -m "Session summary" && git push`  

If you do nothing else, just follow this ritual — and GitHub will always have your latest WBN work.  

---
