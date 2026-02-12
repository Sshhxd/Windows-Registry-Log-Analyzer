# Windows Registry Log Analyzer - v1.0 (2026-02-12)

---

# 📌 Project Overview

### This project is a simple Python-based log analyzer that parses Windows registry activity logs and detects registry key creation events.

The script scans a log file (`log.txt`) and:

 - Identifies registry keys being accessed
 - Tracks "Creating or opening the key" events
 - Counts how many times a specific key is created/opened
 - Checks output length constraints (useful for formatting or log validation)

## 🎯 Purpose

### Registry monitoring is an important aspect of:

 - Malware analysis
 - Digital forensics
 - Incident response
 - System auditing

It simulates a small part of what security analysts and forensic investigators do when analyzing registry activity logs.

---

## 🛡 Security Relevance

### Frequent registry key creation/opening can indicate:

 - Malware persistence attempts-
 - Registry-based privilege escalation
 - Configuration tampering
 - Automated scripts interacting with system components

This tool can serve as a foundation for:

 - Registry anomaly detection
 - Forensic timeline reconstruction
 - SIEM preprocessing scripts

---

## 🛠 How It Works

 1. Reads a structured log file.
 2. Detects registry key references (`Key:` lines).
 3. Identifies "Creating or opening the key" events.
 4. Correlates timestamp with the active registry key.
 5. Counts repeated events.
 6. Validates output length (format control logic).

## 🧪 Example Output
```
Longer than 95 characters : 100
2026-02-11 17:48:35.846 -> HKEY_CURRENT_USER\Software\Classes\VSCode.zsh\shell\open\command (5 times)
Shorter than 95 characters : 87
2026-02-11 17:48:35.846 -> HKEY_CURRENT_USER\Software\Classes\VSCodeSourceFile (3 times)
Longer than 95 characters : 99
2026-02-11 17:48:35.846 -> HKEY_CURRENT_USER\Software\Classes\VSCodeSourceFile\DefaultIcon (8 times)
Longer than 95 characters : 98
2026-02-11 17:48:35.846 -> HKEY_CURRENT_USER\Software\Classes\VSCodeSourceFile\shell\open (5 times)
Longer than 95 characters : 111
2026-02-11 17:48:35.846 -> HKEY_CURRENT_USER\Software\Classes\Applications\Code.exe\shell\open\command (2 times)
```

## 🚀 How to Run

1. Make sure you add the path to your log file here: `file_path = r""`

2. Install python or open the control panel and type:
```
python Log_Analyzer_Tool.py
```

---

# 📈 Future Improvements

 - Regex-based parsing instead of split()
 - Structured timestamp parsing (datetime module)
 - Improve key tracking reliability
 - Suspicious frequency threshold alerts
 - CSV/JSON export
 - Add anomaly detection
 - Create a GUI or CLI tool version
 - Integration with SIEM tools
 - Refactor into modular functions
 - Add unit tests

# 
