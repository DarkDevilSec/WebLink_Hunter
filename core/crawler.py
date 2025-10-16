#!/usr/bin/env python3
# ============================================
# crawler.py - Depth-based crawler for Web VAPT (HTML report ready)
# Author: White Devil
# ============================================

import time
from collections import deque
from urllib.parse import urlparse
from core import extractor, storage, normalizer, filters
from colorama import Fore, Style

visited_urls = set()

def is_same_domain(base_url, target_url):
    """Check if target_url belongs to the same domain"""
    return urlparse(base_url).netloc == urlparse(target_url).netloc

def crawl(target_url, max_depth=2):
    """
    Crawl target URL up to max_depth
    Returns dict of all discovered URLs categorized by type
    """
    discovered = {
        "href": set(),
        "src": set(),
        "action": set()
    }

    queue = deque()
    queue.append((target_url, 0))

    print(f"{Fore.CYAN}[+] Starting crawl: {target_url} (max depth: {max_depth})\n")

    while queue:
        current_url, depth = queue.popleft()
        if current_url in visited_urls or depth > max_depth:
            continue

        print(f"{Fore.YELLOW}[>] Crawling ({depth}): {current_url}{Style.RESET_ALL}")
        visited_urls.add(current_url)

        try:
            # Extract all links from current page
            href_links = extractor.extract_links(current_url, "href")
            src_links = extractor.extract_links(current_url, "src")
            action_links = extractor.extract_links(current_url, "action")
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to extract links from {current_url}: {e}")
            continue

        # Normalize & filter same-domain links
        for link in href_links:
            norm = normalizer.normalize_url(target_url, link)
            if is_same_domain(target_url, norm):
                discovered["href"].add(norm)
                if norm not in visited_urls:
                    queue.append((norm, depth + 1))

        for link in src_links:
            norm = normalizer.normalize_url(target_url, link)
            if is_same_domain(target_url, norm):
                discovered["src"].add(norm)

        for link in action_links:
            norm = normalizer.normalize_url(target_url, link)
            if is_same_domain(target_url, norm):
                discovered["action"].add(norm)

        time.sleep(0.5)

    # Deduplicate final lists
    for k in discovered:
        discovered[k] = filters.remove_duplicates(list(discovered[k]))

    total_links = sum(len(v) for v in discovered.values())
    print(f"\n{Fore.GREEN}[+] Crawling finished. Total discovered URLs: {total_links}{Style.RESET_ALL}")

    # Save results as HTML report
    storage.save(target_url, discovered)
    return discovered
