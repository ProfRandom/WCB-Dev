# Git Cheat Sheet — WCB Workflow

This sheet captures the essential Git commands for managing the Worldmaking: Crafting and Building (WCB) glossary and notes.

---

## 🔑 Day-to-Day Commands

**Check status of repo**
```bash
git status
```

**Stage a single file**
```bash
git add "Canon Files/Glossary/Master_Glossary_v1.217.md"
```

**Stage everything you’ve changed**
```bash
git add -A
```

**Commit staged changes**
```bash
git commit -m "20250927. Glossary v1.217: Added Monobody Compositions taxonomy"
```

**Push commits to GitHub**
```bash
git push
```

**Tag a glossary milestone**
```bash
git tag glossary-v1.217
git push --tags
```

---

## 🔎 Inspecting Your Repo

**List all tags**
```bash
git tag
```

**Show a specific tag’s commit**
```bash
git show glossary-v1.217
```

**Filter just glossary tags**
```bash
git tag -l "glossary-*"
```

---

## 🛡️ Safety Net

**Undo changes in working files (since last commit)**
```bash
git restore filename.md
```

**Roll back to a specific commit/tag (read-only)**
```bash
git checkout glossary-v1.215
```

**Make a branch from a tag (to experiment safely)**
```bash
git checkout -b test-branch glossary-v1.215
```

---

## 📖 Habit Loop for WCB Sessions

1. Work on `.md` notes.  
2. Generate/update glossary bump.  
3. `git add` → `git commit` → `git tag` → `git push && git push --tags`.  
4. Log a one-liner in `Project_Log.md`.  

---

## 🏷️ Tag Browser

**List tags with commit messages (clean view):**
```bash
git for-each-ref --sort=taggerdate --format '%(refname:short) — %(subject)' refs/tags
```

### Create a Git alias for this:
```bash
git config --global alias.taglog "for-each-ref --sort=taggerdate --format='%(refname:short) — %(subject)' refs/tags"
```
Usage:
```bash
git taglog
```

### Optional Espanso Trigger
Add to your Espanso config (`match` block):
```yaml
matches:
  - trigger: ":git-tags"
    replace: "git taglog"
```
Now typing `:git-tags` will expand to `git taglog` in your shell or notes.
