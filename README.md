# 🕵️ WebLink Hunter

```
██╗    ██╗███████╗██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║     ██║████╗  ██║██║ ██╔╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝██║     ██║██╔██╗ ██║█████╔╝     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██║     ██║██║╚██╗██║██╔═██╗     ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝███████╗██║██║ ╚████║██║  ██╗    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

**🚀 WebLink Hunter** | Version: **1.0**
**🕵️ Author:** Ashish Prajapati | **GitHub:** [https://github.com/DarkDevilSec/](https://github.com/DarkDevilSec/)
**🖥️ Fully CLI-Based** | **HTML Reports**

---

## 🎯 Project Purpose

WebLink Hunter is a CLI-based Web VAPT Link Harvester that helps penetration testers and security researchers identify, extract, and analyze all URLs (`href`, `src`, and form actions) from target web applications. The goal is to simplify web reconnaissance and automate link discovery for vulnerability assessments and reporting.

---

## 🔧 Quick Menu (shown in CLI)

```
[1] Extract all href links
[2] Extract all src links
[3] Extract all form actions
[4] Crawl target and get all (href/src/action)
[0] Exit
```

---

## 📸 Screenshot

Add screenshots to the repo under `screenshots/` and reference them in this README. Example:

```markdown
![WebLink Hunter - Demo]([screenshots/demo.png](https://github.com/DarkDevilSec/WebLink_Hunter/blob/main/poc.png))
```

If you want to host screenshots externally (Imgur, GitHub issues, or GitHub Releases), paste the direct image URL here. Example placeholder link:

`https://raw.githubusercontent.com/<your-username>/weblink-hunter/main/screenshots/demo.png`

---

## ⚡ Features

* 🔗 Extract `href`, `src`, and form action links
* 🌐 Depth-based crawl with same-domain filtering
* 🧹 Normalize & deduplicate URLs
* 📄 Generate clickable HTML reports saved to `output/reports/`
* 🖥️ Fully CLI-driven for automation and scripting

---

## 🛠️ Requirements

* Python 3.8+
* `requests`, `beautifulsoup4`, `colorama`, `lxml`, `tqdm`

---

## 🚀 Installation (setup.sh)

```bash
git clone https://github.com/DarkDevilSec/weblink-hunter.git
cd weblink-hunter
chmod +x setup.sh
./setup.sh
```

Use `./setup.sh --system` to install into the system Python (no virtualenv).

---

## 🎮 Usage

Run the tool:

```bash
python3 main.py
# or if executable
./main.py
```

Then choose an option from the menu and enter the target URL when prompted.

Reports are saved to `output/reports/` as clickable HTML files.

---

## 📂 Repo Layout

```
weblink-hunter/
├── core/
│   ├── crawler.py
│   ├── extractor.py
│   ├── filters.py
│   ├── normalizer.py
│   ├── storage.py
│   └── __init__.py
├── main.py
├── setup.sh
├── requirements.txt
├── output/
│   ├── logs/
│   └── reports/
└── README.md
```

---

## ⚖️ License

MIT — Use responsibly and only on targets you have permission to test.

---

If you want, I can add the actual screenshot file to the project canvas or generate a sample `screenshots/demo.png` placeholder and update the README to point to it.
