# 📖 Usage Guide - File Integrity Checker

A simple, step-by-step guide for using the File Integrity Checker application.

---

## 🚀 Quick Start (3 Simple Steps)

### Step 1: Run the Application
- **Windows**: Double-click `run.bat` OR open terminal and type `python app_gui.py`
- **Mac/Linux**: Open terminal and type `python3 app_gui.py`

### Step 2: Select a File
- Click the **"Browse File"** button
- Choose any file you want to monitor
- The original hash will be generated automatically

### Step 3: Check Integrity
- Modify the file (or don't modify it)
- Click **"Recheck File"** button
- See the result:
  - ✅ **Green** = File is safe (unchanged)
  - ⚠️ **Red** = File was modified

---

## 🎯 Detailed Usage Instructions

### Scenario 1: Verifying a File is Unchanged

**Use Case**: You want to ensure a file hasn't been tampered with.

1. **Launch the app**
   ```bash
   python app_gui.py
   ```

2. **Select your file**
   - Click "Browse File"
   - Navigate to your file
   - Click "Open"

3. **Save the hash**
   - The original hash is displayed
   - You can copy this hash for future reference
   - Write it down or save to a text file

4. **Wait or do other work**
   - The application keeps the original hash in memory
   - You can close and reopen (but you'll need to re-select)

5. **Verify integrity later**
   - Click "Recheck File"
   - If green: File is unchanged ✅
   - If red: File was modified ⚠️

---

### Scenario 2: Testing the Application

**Use Case**: You want to see how the app detects changes.

1. **Create a test file**
   ```
   Create a new text file called "test.txt"
   Type some content: "This is a test file."
   Save and close it.
   ```

2. **Run the app and select test.txt**
   ```
   Original hash will be generated
   Example: a1b2c3d4e5f6...
   ```

3. **Modify the test file**
   ```
   Open test.txt
   Add one character: "This is a test file.!"
   Save and close
   ```

4. **Recheck in the app**
   ```
   Click "Recheck File"
   Result: ⚠️ File Modified (RED)
   The hash will be completely different!
   ```

5. **Try again without modifying**
   ```
   Click "Clear"
   Select the same file (unchanged)
   Click "Recheck File"
   Result: ✅ File is Safe (GREEN)
   ```

---

### Scenario 3: Monitoring Important Files

**Use Case**: You want to monitor a configuration file or important document.

1. **Select the important file**
   ```
   Example: config.ini, important_document.docx
   ```

2. **Record the hash**
   ```
   Original Hash: 4f3d2a1b9c8e7f6...
   Write this down or screenshot it
   ```

3. **Check periodically**
   ```
   Open the app
   Select the same file
   Click "Recheck"
   Compare with original hash
   ```

4. **Investigate if changed**
   ```
   If red: Check who modified it
   Verify if change was authorized
   Investigate potential tampering
   ```

---

## 🎨 Understanding the Interface

### Main Window Components

```
┌─────────────────────────────────────────┐
│   🔒 File Integrity Checker             │  ← Title Bar
├─────────────────────────────────────────┤
│                                         │
│  📁 Select File                         │  ← File Selection
│  ┌───────────────────────────────────┐ │
│  │ Selected: example.txt             │ │
│  └───────────────────────────────────┘ │
│           [Browse File]                 │  ← Button
│                                         │
│  ℹ️ File Information                    │  ← File Details
│  Name: example.txt                      │
│  Size: 1.5 KB                          │
│  Path: C:/Users/...                    │
│                                         │
│  🔑 Hash Values                         │  ← Hash Display
│  Original Hash:                         │
│  ┌───────────────────────────────────┐ │
│  │ a1b2c3d4e5f6789...                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Current Hash:                          │
│  ┌───────────────────────────────────┐ │
│  │ a1b2c3d4e5f6789...                │ │
│  └───────────────────────────────────┘ │
│                                         │
│    [🔄 Recheck File]  [🗑️ Clear]       │  ← Action Buttons
│                                         │
│        ✅ File is Safe                  │  ← Result (Green/Red)
│                                         │
└─────────────────────────────────────────┘
```

### Button Functions

| Button | Function | When to Use |
|--------|----------|-------------|
| **Browse File** | Select a file to verify | At the start |
| **Recheck File** | Generate new hash and compare | After potential modification |
| **Clear** | Reset all fields | Start over with a new file |

### Status Colors

| Color | Meaning | What to Do |
|-------|---------|------------|
| 🟢 **Green** | File is safe | No action needed |
| 🔴 **Red** | File modified | Investigate the change |
| ⚫ **Gray** | No result yet | Select file and check |

---

## 💡 Tips & Best Practices

### DO's ✅

1. **DO** select the file immediately after opening the app
2. **DO** save or screenshot the original hash
3. **DO** recheck files after important operations
4. **DO** clear and restart for each new file
5. **DO** use for important documents and files
6. **DO** verify backups using this tool
7. **DO** check downloaded files for integrity

### DON'Ts ❌

1. **DON'T** modify files while the app has them selected
2. **DON'T** delete files after selecting them
3. **DON'T** rely solely on file modification dates
4. **DON'T** forget to record important hashes
5. **DON'T** close the app if you need the original hash
6. **DON'T** ignore red warnings - investigate!

---

## 🔧 Troubleshooting

### Problem: "File not found" error

**Solution:**
- Make sure file still exists
- Check file hasn't been moved
- Verify file path is correct
- Re-select the file

### Problem: "Permission denied" error

**Solution:**
- Close any programs using the file
- Check file permissions
- Run app as administrator (if needed)
- Verify you have read access

### Problem: Hashes are same but file looks different

**Solution:**
- Check you're looking at the correct file
- Verify file path matches
- Visual changes may not affect content
- Try reopening the file

### Problem: App doesn't start

**Solution:**
- Verify Python is installed: `python --version`
- Check Tkinter is available: `python -m tkinter`
- Install Python 3.6+ if missing
- Try: `python app_gui.py` in terminal

### Problem: Hash looks wrong or too short

**Solution:**
- SHA256 hashes are always 64 characters
- If truncated, copy from the entry field
- Verify the file was read completely
- Check for errors in the terminal

---

## 📝 Common Questions (FAQ)

### Q1: What is a hash?
**A:** A hash is like a unique fingerprint for a file. Even a tiny change creates a completely different hash.

### Q2: Why SHA256?
**A:** SHA256 is:
- Secure (cryptographically strong)
- Standard (widely used)
- Unique (virtually no collisions)
- Fast (quick computation)

### Q3: Can I verify folders?
**A:** Not in current version. Select individual files. (Folder support planned for future)

### Q4: How long does it take?
**A:** 
- Small files (< 1MB): Instant
- Medium files (1-100MB): Few seconds
- Large files (> 1GB): Up to 30 seconds

### Q5: Does it work offline?
**A:** Yes! No internet needed. Everything is local.

### Q6: Can I use it for security?
**A:** Yes! Perfect for:
- Verifying downloads
- Checking backups
- Detecting tampering
- Ensuring file integrity

### Q7: Will it modify my files?
**A:** No! The app only READS files. It never writes or modifies them.

### Q8: Can I trust the hash?
**A:** Yes! SHA256 is:
- Industry standard
- Used by governments
- Cryptographically secure
- Mathematically proven

---

## 🎓 Learning Examples

### Example 1: Student Assignment Protection

**Scenario:** Protect your assignment from accidental changes.

```
1. Finish your assignment → Save as "final_assignment.docx"
2. Run File Integrity Checker
3. Select "final_assignment.docx"
4. Copy the original hash → Save to "hash_record.txt"
5. Before submission → Recheck file
6. If green → Submit confidently
7. If red → Something changed! Check what happened
```

### Example 2: Software Download Verification

**Scenario:** Verify a downloaded installer is legitimate.

```
1. Download software → Note website's published hash
2. Run File Integrity Checker
3. Select downloaded installer
4. Compare generated hash with website's hash
5. If match → Safe to install
6. If different → Download may be corrupted/tampered
```

### Example 3: Backup Verification

**Scenario:** Ensure backup copy is identical to original.

```
1. Original file → "data.xlsx"
2. Backup file → "data_backup.xlsx"
3. Check original file → Get hash A
4. Clear application
5. Check backup file → Get hash B
6. Compare hash A and hash B
7. If same → Perfect backup
8. If different → Backup may be corrupted
```

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────┐
│     FILE INTEGRITY CHECKER              │
│         Quick Reference                 │
├─────────────────────────────────────────┤
│                                         │
│  START:                                 │
│    python app_gui.py                    │
│                                         │
│  SELECT FILE:                           │
│    Click "Browse File" → Choose file    │
│                                         │
│  VERIFY:                                │
│    Click "Recheck File" → Check result  │
│                                         │
│  RESULTS:                               │
│    ✅ GREEN = Safe (no changes)         │
│    ⚠️ RED = Modified (changed)          │
│                                         │
│  RESET:                                 │
│    Click "Clear" → Start over           │
│                                         │
│  REMEMBER:                              │
│    • Original hash = File fingerprint   │
│    • Any change = Different hash        │
│    • Use for important files           │
│    • Check before/after events         │
│                                         │
└─────────────────────────────────────────┘
```

---

## 📞 Need Help?

- Check the **README.md** for detailed information
- Read the **PROJECT_REPORT.md** for technical details
- Review this **USAGE_GUIDE.md** for instructions
- Create an issue in the repository
- Contact the development team

---

**Happy File Verification! 🔒**

*Remember: A hash is like a digital fingerprint - unique and unchangeable!*
