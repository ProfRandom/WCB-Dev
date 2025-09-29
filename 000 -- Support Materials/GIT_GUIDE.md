# 🌐 WCB Git Style Guide

This guide defines how to use **commits** and **tags** to keep the Worlds by Numbers (WCB) project consistent, searchable, and easy to time-travel.

---

## 1. Commit Messages

### Format
```
YYYYMMDD.HHMM — [scope]: [short, meaningful description]
```

- **YYYYMMDD.HHMM** → Timestamp for easy chronological search.  
- **[scope]** → Area of change (Glossary, Symbols, Dashboard, Draft, Fiction, etc.).  
- **[description]** → What changed and why it matters.  

### Examples
```
20250927.1844 — Glossary: Prior to switching to official stellar temperature scales
20250927.1920 — Fiction: Destiny loses left hand in Ch12
20250928.0815 — Dashboard: Obliquity block flipped green
```

### Why
- Clear commit history = no “what did I do that day?” guesswork.  
- Future you can search with:
```
git log --grep "stellar temperature"
```

---

## 2. Tags

Tags mark **milestones** in project history. Unlike branches, tags never move.  

### Types of Tags
```
glossary-v1.22   → Doubles and Moons terms merged
glossary-v1.23   → Switched to official stellar temperature scales
ch12-pre-amput   → Chapter 12 before Destiny loses left hand
ch10-sushi       → Chapter 10, Fred eats sushi
```

### Creating a Tag
```
git tag -a <tag-name> -m "<tag message>"
git push origin <tag-name>
```

**Example**
```
git tag -a glossary-v1.23 -m "Glossary switched to official stellar temperature scales"
git push origin glossary-v1.23
```

### Listing Tags
```
git tag
```

### Checking Out a Tag
```
git checkout <tag-name>
```

---

## 3. Workflow Summary

1. **Commit regularly**
   - Small, clear changes with timestamp + scope.  
   - Commit messages explain *why*, not just *what*.  

2. **Tag milestones**
   - When glossary versions bump.  
   - When a major fiction draft event occurs.  
   - When dashboard coverage flips a block to green.  

3. **Search easily**
   - `git log --grep "keyword"` → find relevant commits.  
   - `git checkout <tag>` → jump to any milestone.  

---

## 4. Scopes Reference

Use these common scopes for consistency:  
```
Glossary   → Master Glossary updates
Symbols    → Symbols Index changes
Dashboard  → Coverage Dashboard updates
Draft      → Draft worldbuilding notes
Fiction    → Novel/short story chapters
Repo       → Git workflow, housekeeping, file structure
```

---

✨ With this system, Git becomes your **time machine**: every canon bump, experiment, or story draft is preserved, searchable, and recoverable forever.


|