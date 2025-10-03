# 🧠 Memory Reset Protocol — Worlds by the Numbers

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
   - Example: `Master_Thread_Index_v0.2.md`  
   - This file is the *map of maps*; it points GPT to the current versions of all systems.  

2. **Memory Snapshot (latest version)**  
   - Example: `Memory_Snapshot_v0.1.md`  
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
   - Tell GPT: *“This is the latest save point for WCB. Sync up using these files.”*  

3. **During the New Thread**  
   - Carry forward version numbering (Glossary v1.21, Dashboard v0.3, etc.).  
   - Use “Supersedes vX” notes in each new file.  
   - Archive older versions into Vault `Deprecation` folder.  

---

## 📌 Notes
- Glossary Master Thread is the **control tower**; all decisions and canonical files are tracked there.  
- Other conversations may explore side concepts, but **decisions must be ported back here**.  
- This protocol ensures that even if ChatGPT “forgets,” the project never loses continuity.  

