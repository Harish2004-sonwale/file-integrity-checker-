# 🔒 File Integrity Checker (Hash Verifier )

A Python-based application that verifies file integrity using SHA256 hash generation. Detects file modifications, corruption, or tampering with an intuitive GUI interface.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Algorithm & Flowchart](#-algorithm--flowchart)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

The **File Integrity Checker** is a cybersecurity tool designed to:
- Generate unique SHA256 hash values for any file
- Store original hash for comparison
- Detect modifications, corruption, or tampering
- Provide visual feedback on file integrity status

This project demonstrates fundamental concepts in:
- **Cryptographic Hashing** (SHA256)
- **File Integrity Verification**
- **GUI Development** (Tkinter)
- **Cybersecurity Principles**

---

## ✨ Features

- ✅ **SHA256 Hash Generation** - Secure cryptographic hashing
- ✅ **Real-time Verification** - Instant file integrity checking
- ✅ **User-Friendly GUI** - Intuitive Tkinter interface
- ✅ **File Information Display** - Shows name, size, and path
- ✅ **Visual Status Indicators** - Color-coded results
- ✅ **Cross-Platform** - Works on Windows, Linux, and macOS
- ✅ **Large File Support** - Efficient chunked reading
- ✅ **Error Handling** - Robust error management

---

## 🛠 Technologies Used

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **Hashing** | hashlib (SHA256) |
| **GUI Framework** | Tkinter |
| **OS Support** | Windows / Linux / macOS |
| **Optional Extension** | Flask (for web version) |

### Key Python Modules:
- `hashlib` - Cryptographic hashing
- `tkinter` - GUI development
- `os` - File system operations

---

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### Steps

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd file-integrity-checker
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **Check Tkinter Installation**
   ```bash
   python -m tkinter
   ```
   A small window should appear. If not, install Tkinter:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **Fedora**: `sudo dnf install python3-tkinter`
   - **macOS**: Included with Python
   - **Windows**: Included with Python

---

## 🚀 How to Run

### Method 1: Using Python Command

```bash
python app_gui.py
```

### Method 2: Double-Click (Windows)

1. Right-click `app_gui.py`
2. Select "Open with" → Python

### Method 3: Create Executable (Optional)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed app_gui.py
```

The executable will be in the `dist` folder.

---

## 📖 Usage Guide

### Step-by-Step Instructions

1. **Launch the Application**
   ```bash
   python app_gui.py
   ```

2. **Select a File**
   - Click the **"Browse File"** button
   - Choose any file from your system
   - Original SHA256 hash is automatically generated

3. **View File Information**
   - File name, size, and path are displayed
   - Original hash is shown in the first field

4. **Modify the File (Testing)**
   - Open the file in a text editor
   - Make any change and save
   - Return to the application

5. **Recheck File Integrity**
   - Click **"Recheck File"** button
   - New hash is generated and compared
   - Result is displayed:
     - ✅ **Green** = File is safe (no changes)
     - ⚠️ **Red** = File modified (integrity compromised)

6. **Clear and Start Over**
   - Click **"Clear"** button to reset

---

## 📁 Project Structure

```
file-integrity-checker/
│
├── hash_generator.py      # Backend logic (hash generation & comparison)
├── app_gui.py            # Frontend GUI (Tkinter interface)
├── README.md             # Project documentation
├── PROJECT_REPORT.md     # Detailed project report
└── requirements.txt      # Python dependencies (optional)
```

### File Descriptions

- **hash_generator.py**
  - `generate_file_hash(file_path)` - Generates SHA256 hash
  - `compare_hashes(original, new)` - Compares two hashes
  - `get_file_info(file_path)` - Retrieves file metadata

- **app_gui.py**
  - Complete GUI implementation
  - File selection and display
  - Hash generation and comparison
  - Result visualization

---

## 🔄 Algorithm & Flowchart

### Algorithm

```
1. START
2. Initialize GUI application
3. DISPLAY file selection button
4. User clicks "Browse File"
5. SELECT file from system
6. READ file in 4096-byte chunks
7. GENERATE SHA256 hash → Store as original_hash
8. DISPLAY original_hash to user
9. User modifies file (optional)
10. User clicks "Recheck File"
11. GENERATE new SHA256 hash → Store as new_hash
12. COMPARE original_hash with new_hash
13. IF hashes match:
       DISPLAY "✅ File is Safe" (Green)
    ELSE:
       DISPLAY "⚠️ File Modified" (Red)
14. User clicks "Clear" to reset (optional)
15. REPEAT from step 4 or EXIT
16. END
```

### Flowchart

```
                    [START]
                       |
                       v
              [Initialize GUI]
                       |
                       v
              [Display "Browse" Button]
                       |
                       v
           [User Selects File] <------------+
                       |                     |
                       v                     |
         [Read File in Chunks]               |
                       |                     |
                       v                     |
        [Generate SHA256 Hash]               |
                       |                     |
                       v                     |
       [Store as original_hash]              |
                       |                     |
                       v                     |
        [Display Hash & Info]                |
                       |                     |
                       v                     |
       [Wait for User Action]                |
                       |                     |
         +-------------+--------------+      |
         |             |              |      |
         v             v              v      |
    [Recheck]      [Clear]        [Exit]    |
         |             |              |      |
         v             |              v      |
  [Generate new_hash]  |          [CLOSE]   |
         |             |                     |
         v             |                     |
  [Compare Hashes]     |                     |
         |             |                     |
    +----+----+        |                     |
    |         |        |                     |
    v         v        |                     |
[Match]  [Different]   |                     |
    |         |        |                     |
    v         v        |                     |
[Safe]  [Modified]     |                     |
    |         |        |                     |
    +----+----+        |                     |
         |             |                     |
         v             v                     |
    [Display Result]   [Reset All]           |
         |             |                     |
         +-------------+---------------------+
```

---

## 📸 Screenshots


![screenshot1](https://github.com/user-attachments/assets/732b7a1e-622f-4ece-a230-f87bdac385fb)


![scrrenshot 2 ](https://github.com/user-attachments/assets/eecc2641-11a3-49a0-a569-80b44a486fee)

![scrrenshot 3](https://github.com/user-attachments/assets/305d96ef-2be8-43fd-b8cd-3db0c1289e13)

### Main Interface
- Clean and modern UI design
- Color-coded status indicators
- Clear hash display fields

### Features Demonstrated
1. **File Selection** - Browse and select any file
2. **Hash Display** - View original and current hashes
3. **Integrity Check** - Visual verification results
4. **File Information** - Detailed file metadata

---

## 🚀 Future Enhancements

- [ ] **Web Version** - Flask-based web interface
- [ ] **Database Integration** - Store hash history
- [ ] **Multiple File Support** - Batch verification
- [ ] **Hash Export** - Save hashes to file
- [ ] **Additional Algorithms** - MD5, SHA1, SHA512
- [ ] **Scheduling** - Automatic periodic checks
- [ ] **Email Alerts** - Notification on tampering
- [ ] **Checksum Verification** - Verify against known checksums
- [ ] **Dark Mode** - Theme customization
- [ ] **Drag & Drop** - Enhanced file selection

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Harish C Sonwale**
- Project: File Integrity Checker
- Technology: Python + Tkinter
- Purpose: Cybersecurity Demonstration

---

## 🙏 Acknowledgments

- Python Software Foundation for Python
- Tkinter for GUI framework
- hashlib for cryptographic functions
- Open-source community

---

## 🎓 Educational Use

This project is designed for:
- **Learning** cryptographic hashing
- **Understanding** file integrity concepts
- **Demonstrating** GUI development
- **Exploring** cybersecurity principles

Perfect for:
- College projects
- Cybersecurity courses
- Python programming practice
- Portfolio demonstration
