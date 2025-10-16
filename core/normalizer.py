#!/usr/bin/env python3
# ============================================
# normalizer.py - Normalize URLs
# Author: White Devil
# ============================================

from urllib.parse import urljoin, urlparse, urlunparse, parse_qs, urlencode

def normalize_url(base_url, link):
    """
    Convert relative URLs to absolute, remove fragments,
    and normalize query parameters (sorted).
    """
    absolute = urljoin(base_url, link)
    parsed = urlparse(absolute)

    # Sort query params
    query_dict = parse_qs(parsed.query)
    sorted_query = urlencode(sorted(query_dict.items()), doseq=True)

    # Remove fragments
    normalized = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        sorted_query,
        ""  # fragment removed
    ))

    return normalized
