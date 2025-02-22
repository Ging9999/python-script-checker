# **Whitespace Payload Detector**

A Python tool that checks Python files in a GitHub repository for excessive white spaces, which could be indicative of hidden malicious payloads or obfuscated code. Excessive whitespace can sometimes be used to conceal harmful code, and this tool helps identify such suspicious patterns.

## **Overview**

This script scans Python files in a specified GitHub repository and detects lines with an unusually high number of leading spaces. Excessive whitespace can be a potential indicator of obfuscation or attempts to hide malicious payloads within the code.

### **Key Features**
- Scans all Python files (`.py`) in a GitHub repository.
- Detects lines with excessive white spaces (threshold can be customized).
- Outputs the file name, line number, number of spaces, and the affected line for each suspicious line.
- Helps in identifying potential malicious payloads hidden through whitespace obfuscation.

## **How it Works**

1. **GitHub API Integration**: The script uses the GitHub API to list all files in the repository.
2. **Filter Python Files**: It filters out all non-Python files (`.py` files).
3. **Whitespace Detection**: For each Python file, it checks each line for leading white spaces that exceed a set threshold.
4. **Output**: The script prints a report with the file name, line number, and the number of spaces on each line that has excessive whitespace.

### **Why Check for Excessive Whitespace?**

Attackers may hide malicious code by leveraging obfuscation techniques such as adding excessive whitespace. These payloads can be difficult to spot at first glance, and they can be used to bypass certain detection methods. This tool helps to flag such potential obfuscation.

## **Installation**

To use this tool, you need Python 3.x installed, along with the `requests` library to interact with the GitHub API.


