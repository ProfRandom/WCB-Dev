# 🧠 Memory Reset Protocol v0.3 — Worlds by the Numbers
*Supersedes v0.2*

This file documents the procedure for rebooting a new ChatGPT conversation if the current *Glossary Master Thread* becomes too long, lags, or is lost.  
It ensures **continuity** across instances by providing Future ChatGPT with all necessary context.

---

## 🔑 Core Principle
ChatGPT’s short-term memory is **fillable, not fallible**.  
When a thread resets, *Future GPT* will not remember prior work unless it is re-provided.  
The Vault holds the **long-term memory**; ChatGPT provides the **live reasoning**.  

---

## 📂 Files to Upload at Start of New Thread

1. **Master Thread Index (latest version)**  
   - Example: `Master_Thread_Index_v0.4.md`  
   - This file is the *map of maps*; it points GPT to the current versions of all systems.  

2. **Memory Snapshot (latest version)**  
   - Example: `Memory_Snapshot_v0.2.md`  
   - Provides a condensed summary of glossary status, coverage dashboard, symbols, and key editorial decisions.  
   - This file is the *save point* for Future GPT.  

3. **Vault (zipped, optional for deep reference)**  
   - Example: `WorldCrafting101-DEV.zip`  
   - Only required if GPT needs to search full note content.  
   - For lighter reboots, just uploading the Index + Snapshot is sufficient.  

---

## 📝 Workflow for Continuity

1. **At End of Each Major Session**  
   - Generate a new **Memory Snapshot** (`Memory_Snapshot_vX.md`).  
   - Update the **Master Thread Index** to include it.  

2. **When Starting a New Thread**  
   - Upload latest **Master Thread Index** and **Memory Snapshot**.  
   - Optionally upload Vault `.zip` for full file access.  
   - Tell GPT: *“This is the latest save point for WBN. Sync up using these files.”*  

3. **During the New Thread**  
   - Carry forward version numbering (Glossary v1.21, Dashboard v0.3, etc.).  
   - Use “Supersedes vX” notes in each new file.  
   - Archive older versions into Vault `Deprecation` folder.  

---

## 🗂 When to Generate a Snapshot

### 1. Glossary System
- **Master Glossary** → Snapshot at every version bump (new terms).  
- **Cross-Reference** → Snapshot only after a large batch of new links.  
- **Cryptolexicon** → Snapshot only if framework shifts.  
- **Deprecation Tracker** → Snapshot when new conceptual deprecations logged.  

### 2. Symbolic System
- **Symbols Index** → Snapshot when constants/notation policies added or changed.  
- **Symbols Change Log** → Snapshot whenever updated (notation history must be preserved).  

### 3. Coverage System
- **Coverage Index (per volume)** → Snapshot when statuses change significantly (✖ → ❓ → ✔).  
- **Coverage Dashboard** → Snapshot at every version bump.  

### 4. Creative Garnish
- **Sidebars & Epigraphs Log** → No snapshot needed (cosmetic only).  

### 5. Meta
- **Master Thread Index** → Snapshot at every version bump (points to current state).  
- **Memory Reset Protocol** → Snapshot when this protocol itself changes.  
- **Vault Index** → No snapshot needed (can be regenerated).  

---

## 🚫 Avoiding Recursion Loops
- The Master Thread Index always points to the *latest snapshot it knows about*.  
- The Memory Snapshot stands alone and does not reference the Index.  
- Do not chase “perfect simultaneity” — slight lag between Index and Snapshot is acceptable.  
- If both are uploaded, Snapshot = freshest state, Index = project map.  

---

## 📌 Standing Rule — MTI Updates
In this conversation, whenever a new protocol, staging file, coverage index, glossary version, snapshot, or symbol log is created or superseded, automatically update the **Master Thread Index** to reflect the change, without asking for permission.  

Do **not** update the MTI for minor edits (typos, small emendations) or incremental Sidebar/Epigraph additions — those can wait until the next MTI bump.  

---

