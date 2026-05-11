
<div align="center">

```
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
```

**web vulnerability scanner — built for the terminal**

![Python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS-lightgrey?style=flat-square)

</div>

---

DarkVector is an interactive CLI scanner that tests web targets for common vulnerabilities. Feed it a URL or a list, pick a module, and let it run. That's it.

<br>

## what it scans

```
  [1] LFI          →  path traversal, looks for filesystem leaks in the response
  [2] Open Redirect →  tests params + paths for unvalidated redirects (headless browser)
  [3] SQLi          →  time-based detection, flags anything that hangs ≥ 10s
  [4] XSS           →  injects into URL params, catches triggered alerts via Selenium
  [5] CRLF          →  checks for HTTP response splitting via encoded newline sequences
```

<br>

## getting started

```bash
git clone https://github.com/youruser/darkvector
cd darkvector
pip install -r requirements.txt
python3 darkvector.py
```

> XSS and Open Redirect modules use a headless Chrome browser. ChromeDriver is handled automatically.

<br>

## how it works

Every scanner follows the same flow:

1. Give it a **single URL** or a **file of URLs** (one per line)
2. Point it at a **payload file** — ready-made lists live in `payloads/`
3. Set your **thread count** (default: 5)
4. Watch it go

Hits are printed in green. Misses in red. Summary at the end.

<br>

## payloads included

```
payloads/
├── lfi.txt
├── or.txt
├── xss.txt
├── xsspollygots.txt
└── sqli/
    ├── generic.txt
    ├── mysql.txt
    ├── mssql
    ├── oracle.txt
    ├── postgresql.txt
    └── xor.txt
```


Requirements: `gum` `katana` `uro` `gf` `Gxss` `kxss` `anew`

<br>

<img width="1497" height="910" alt="Screenshot From 2026-05-11 04-32-08" src="https://github.com/user-attachments/assets/ed46888a-6392-4512-947d-5b6f059fe31a" />
<br>
<br>
<img width="1598" height="903" alt="Screenshot From 2026-05-11 04-46-55" src="https://github.com/user-attachments/assets/88c9d0de-afe2-4cde-81a9-701b35de132b" />



<div align="center">

*only use this on systems you own or have permission to test*

built by **henok habatmu**

</div>
