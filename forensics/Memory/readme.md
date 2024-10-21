# BUET CTF 2024 Preli - Memory Forensics Challenges
## Max Attampts: 5
## Tags: Forensics,Memory
## 🔍 Challenge 1: The Evil PID  
- **Difficulty**: Easy  
- **Points**: 100-150 (Dynamic)  
- **Author**: (0xf4h1m)

### 📜 Scenario:
Mr. Sawvik was searching for a software crack and downloaded a program that triggered suspicious popups. It seems like a malicious process may be running in the background. Your task is to analyze the memory dump and identify the **Process ID**, **name of the malicious file**, and **start time of execution**.

### 📝 Note:
All memory forensics challenges use the same memory dump file. 
**Attachment**: (memdump.7z)[https://terabox.com/s/1u3c-2Sx8WROErvIo77oH4g]

**Author**: [Oxf4h1m](https://fb.com/fa11m)
- **Flag Format**: `BUETCTF{pid_evil.bin_dd/mm/yyyy_HH:MM:SS}`

### 🚩 Flag:
`BUETCTF{6348_Runtimebroker.exe_04/10/2024_11:06:52}`

### Solution
using pslist commmand you will get `Runtimebroke.` in  ps list wit pid 6348 (others are RuntimBroker.exe, b in capital latter). then use pstree module to find full path. 

---

## 🔍 Challenge 2: The Evil Location  
- **Difficulty**: Medium  
- **Points**: 100-150 (Dynamic)
- **Author**: (0xf4h1m)

### 📜 Scenario:
The malicious software has been identified, but can you determine the **full path** of where the malware was stored on the system? 

### 📝 Note:
All memory forensics challenges use the same memory dump file.

- **Flag Format**: `BUETCTF{D:\path\to\bin}`

### 🚩 Flag:
`BUETCTF{C:\Users\HP\Downloads\photoshop_2024_crack\Runtimebroker.exe}`

---

## 🔍 Challenge 3: The URL  
- **Difficulty**: Medium  
- **Points**: 100-150 (Dynamic)
- **Author**: (0xf4h1m)

### 📜 Scenario:
Track down the **URL** from which Mr. Sawvik downloaded the malicious software. 

### 📝 Note:
All memory forensics challenges use the same memory dump file.

- **Flag Format**: `BUETCTF{url}`

### 🚩 Flag:
`BUETCTF{https://oshi.at/Hrhf/photoshop_2024_crack.rar}`

---

## 🔍 Challenge 4: DEEP Analysis  
- **Difficulty**: Medium  
- **Points**: 100-150 (dynamic)  
- **Author**: (0xf4h1m)

### 📜 Scenario:
Deep dive into the Malware Analysis and identify the **SSDEEP hash** and the **malware's virus family**. This will help in identifying and classifying the malicious software.

### 📝 Note:
All memory forensics challenges use the same memory dump file.

- **Flag Format**: `BUETCTF{ssdeep_name}`

### 🚩 Flag:
`BUETCTF{98304:6NSsKe9h98C2xYotccpl3dfE8QNfr8PNnB/CY4cMV+pwfkGPmYPyVQHNSqoqJrt5:e8KtWc9hwpBaY4v2Gk+GnFE5uUEhz_lummastealer}`
`BUETCTF{98304:6NSsKe9h98C2xYotccpl3dfE8QNfr8PNnB/CY4cMV+pwfkGPmYPyVQHNSqoqJrt5:e8KtWc9hwpBaY4v2Gk+GnFE5uUEhz_LummaStealer}`

### Solution: 
download rar from previous flag. and extract and upload to virus total
---



## 🎁 Bonus Challenge 1: Hidden Flag 1  
- **Difficulty**: Easy 
- **Points**: 100  
- **Author**: (0xf4h1m)

### 📜 Scenario:
There are some hidden flags scattered throughout the memory dump. Analyze the memory and user activity to uncover the **first hidden flag**.

### 📝 Note:
All memory forensics challenges use the same memory dump file.

- **Flag Format**: `BUETCTF{Str1ng}`

### 🚩 Flag:
`BUETCTF{H1dd3n_1n_th3_cl1pb04rd_4w41t1ng_y0ur_p4st3}`

---

## 🎁 Bonus Challenge 2: Hidden Flag 2  
- **Difficulty**: Medium-Hard  
- **Points**: 100-200 (dynamic)  
- **Author**: (0xf4h1m)

### 📜 Scenario:
The second hidden flag is buried even deeper in the memory dump. Explore user activity and unravel the clues to retrieve the **second flag**.

### 📝 Note:
All memory forensics challenges use the same memory dump file.

- **Flag Format**: `BUETCTF{Str1ng}`

### 🚩 Flag:
`BUETCTF{Y0ur_br41n_1s_th3_k3y_t0_s0lv1ng_th3_h4rd3st_c0d3s_b3_th3_h3r0_0f_th3_cyb3r_w0rld_!}`

### Solution

Run 
`python2 vol.py -f memory.raw  --profile=Win10x64_19041 chromehistory` 

you will get pastebin link in hisory, in pastebin you will get a link of google docs.  flag is hidden in the footer of doc.  

---

