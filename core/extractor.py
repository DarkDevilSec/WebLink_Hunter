#!/usr/bin/env python3
# ============================================
# extractor.py - Extract href, src, and form actions
# Author: White Devil
# ============================================

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore, Style

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def fetch_html(target_url):
    """Fetch HTML content of the given target"""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; WebVAPTLinkHarvester/1.0)"}
        response = requests.get(target_url, headers=headers, timeout=10, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print(f"{Fore.RED}[!] Failed to fetch page (Status: {response.status_code})")
            return ""
    except Exception as e:
        print(f"{Fore.RED}[!] Error fetching page: {e}")
        return ""


def extract_links(target_url, link_type="href"):
    """Extract specific type of links (href, src, or form action)"""
    html = fetch_html(target_url)
    if not html:
        return []

    soup = BeautifulSoup(html, "lxml")
    links = set()

    if link_type == "href":
        for tag in soup.find_all("a", href=True):
            full_link = urljoin(target_url, tag["href"])
            links.add(full_link)

    elif link_type == "src":
        for tag in soup.find_all(src=True):
            full_link = urljoin(target_url, tag["src"])
            links.add(full_link)

    elif link_type == "action":
        for tag in soup.find_all("form", action=True):
            full_link = urljoin(target_url, tag["action"])
            links.add(full_link)

    print(f"{Fore.GREEN}[+] Found {len(links)} {link_type} links")
    return sorted(links)


def extract_all(target_url):
    """Extract all href, src, and form actions together"""
    html = fetch_html(target_url)
    if not html:
        return []

    soup = BeautifulSoup(html, "lxml")
    all_links = set()

    for tag in soup.find_all(["a", "img", "script", "form", "link"]):
        if tag.name == "a" and tag.get("href"):
            all_links.add(urljoin(target_url, tag["href"]))
        elif tag.name in ["img", "script", "link"] and tag.get("src"):
            all_links.add(urljoin(target_url, tag["src"]))
        elif tag.name == "form" and tag.get("action"):
            all_links.add(urljoin(target_url, tag["action"]))

    print(f"{Fore.GREEN}[+] Total links discovered: {len(all_links)}")
    return sorted(all_links)
