#!/usr/bin/env python3
# ============================================
# filters.py - Filter and deduplicate URLs
# Author: White Devil
# ============================================

from urllib.parse import urlparse

def remove_duplicates(url_list):
    """Return a sorted list with duplicates removed"""
    return sorted(list(set(url_list)))

def filter_same_domain(base_url, url_list):
    """Keep only URLs that belong to the same domain as base_url"""
    base_domain = urlparse(base_url).netloc
    filtered = [url for url in url_list if urlparse(url).netloc == base_domain]
    return filtered

def filter_by_extension(url_list, extensions=None):
    """
    Optional filter to include only URLs with certain extensions
    Example: extensions=['.php','.html']
    """
    if not extensions:
        return url_list
    filtered = [url for url in url_list if any(url.lower().endswith(ext) for ext in extensions)]
    return filtered
