#!/usr/bin/env python3
# ============================================
# storage.py - Save extracted links as RedHawk-style HTML report
# Author: White Devil
# ============================================

import os
from datetime import datetime

OUTPUT_FOLDER = "output/reports"

def save_to_html(target_url, links_dict):
    """
    Save extracted links as a RedHawk-style HTML report.
    links_dict = {
        "href": [...],
        "src": [...],
        "action": [...]
    }
    """
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    filename = target_url.replace("http://", "").replace("https://", "").replace("/", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(OUTPUT_FOLDER, f"{filename}_{timestamp}.html")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        f.write(f"<meta charset='UTF-8'><title>Web VAPT Report - {target_url}</title>\n")
        f.write("""
<style>
body {font-family: Arial, sans-serif; background:#1e1e1e; color:#f5f5f5; padding:20px;}
h2 {color:#00ff7f;}
section {margin-bottom:25px;}
a {color:#1e90ff; text-decoration:none; display:block; margin:2px 0;}
a:hover {text-decoration:underline;}
hr {border-color: #444;}
</style>
""")
        f.write("</head>\n<body>\n")
        f.write(f"<h2>Web VAPT Report - {target_url}</h2>\n")
        total_links = sum(len(v) for v in links_dict.values())
        f.write(f"<p>Total Links Discovered: {total_links}</p>\n<hr>\n")

        # Write sections
        for link_type in ["href", "src", "action"]:
            f.write(f"<section>\n<h3>{link_type.upper()} Links ({len(links_dict.get(link_type, []))})</h3>\n")
            for link in links_dict.get(link_type, []):
                f.write(f"<a href='{link}' target='_blank'>{link}</a>\n")
            f.write("</section>\n<hr>\n")

        f.write("</body>\n</html>")

    print(f"[+] RedHawk-style HTML report saved: {filepath}")


def save(target_url, links_dict):
    """Save all links as HTML report"""
    save_to_html(target_url, links_dict)
