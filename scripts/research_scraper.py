import urllib.request
import xml.etree.ElementTree as ET
import os
import re
from datetime import datetime

# Configuration
CATEGORIES = ["cs.AI", "cs.LG", "quant-ph"]
MAX_RESULTS = 5
OUTPUT_DIR = "src/content/news"

def clean_filename(title):
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s-]', '', title)
    title = re.sub(r'\s+', '-', title).strip('-')
    return title

def fetch_arxiv_papers():
    query = "+OR+".join([f"cat:{cat}" for cat in CATEGORIES])
    url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS}"
    
    print(f"Fetching papers from: {url}")
    with urllib.request.urlopen(url) as response:
        return response.read()

def parse_and_save_papers(xml_data):
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        link = entry.find('atom:id', ns).text
        published = entry.find('atom:published', ns).text
        author = entry.find('atom:author/atom:name', ns).text
        
        filename = clean_filename(title)[:50] + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Frontmatter
        date_str = published[:10]
        
        md_content = f"""---
title: "{title}"
pubDate: {date_str}
description: "{summary[:200]}..."
author: "{author}"
link: "{link}"
tags: ["Research", "Paper"]
---

{summary}

[Read full paper at ArXiv]({link})
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Saved: {filename}")

if __name__ == "__main__":
    try:
        xml_data = fetch_arxiv_papers()
        parse_and_save_papers(xml_data)
    except Exception as e:
        print(f"Error: {e}")
