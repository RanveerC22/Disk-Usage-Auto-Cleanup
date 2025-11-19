# Disk-Usage-Auto-Cleanup

## 1. Navigation
- [Reason for Creation](#2-reason-for-creation)
- [Feature Overview](#3-feature-overview)
- [Prerequisites](#4-prerequisites)
- [Installation and Execution](#5-installation-and-execution)
- [What It Does](#6-what-it-does)
- [Limitations](#7-limitations)
- [Output](#8-output)

---

## 2. Reason for Creation

I created this script because I often faced **disk space issues** on my Linux build agents.  
Every time the disk filled up, I had to **SSH into the agent manually**, search for unused folders, and delete them — which was **time-consuming and repetitive**.

To automate this, I wrote a Python script and integrated it into my **CI/CD build step**, so the cleanup happens automatically without manual intervention.

### Short Summary of the Project
A Python script that checks filesystem usage and automatically deletes a target directory when disk space usage exceeds 70%. It prints disk space before and after cleanup, and takes no action if usage is below the threshold.

---

## 3. Feature Overview
- Checks filesystem usage on Linux.
- Deletes the specified directory only if usage exceeds 70%.
- Prints "Disk Space BEFORE Deletion" and "Disk Space AFTER Deletion".
- Skips deletion when usage is normal.
- Lightweight script suitable for CI/CD automation.
- Helps prevent server build failures due to insufficient disk space.

---

## 4. Prerequisites

1. Python 3 Installed  
   If Python is not installed, download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. dzdo/sudo Access  
   The agent user must have dzdo privileges to run the script with elevated permissions.

3. Linux Environment  
   This script is intended to run on a Linux build agent or server.
