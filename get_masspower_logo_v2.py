import requests
from bs4 import BeautifulSoup
import re
import os

url = "https://mass-power.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    print(f"Fetching {url}...")
    response = requests.get(url, headers=headers, timeout=15)
    print(f"Status: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    candidates = []
    
    # Strategy 1: Look for images in header/nav
    header = soup.find('header') or soup.find('nav')
    if header:
        imgs = header.find_all('img')
        for img in imgs:
            src = img.get('src')
            if src: candidates.append(src)
            
    # Strategy 2: Look for 'logo' keyword in src/class/id again (double check)
    all_imgs = soup.find_all('img')
    for img in all_imgs:
        src = img.get('src')
        if not src: continue
        if 'logo' in src.lower() or 'brand' in src.lower():
            candidates.append(src)
            
    # Strategy 3: Look for images in 'top' div
    top_div = soup.find('div', class_=re.compile('top|header', re.I))
    if top_div:
        for img in top_div.find_all('img'):
            if img.get('src'): candidates.append(img.get('src'))

    # Deduplicate
    candidates = list(set(candidates))
    
    final_url = None
    for src in candidates:
        # Resolve URL
        if not src.startswith('http'):
            if src.startswith('/'):
                full_url = "https://mass-power.com" + src
            else:
                full_url = "https://mass-power.com/" + src
        else:
            full_url = src
            
        print(f"Checking candidate: {full_url}")
        # Simple filter: reject obvious content images based on size or name if possible, 
        # but for now just take the first plausible one.
        final_url = full_url
        break # Take the first one found in header/logo search
        
    if final_url:
        print(f"Downloading: {final_url}")
        img_resp = requests.get(final_url, headers=headers, timeout=10)
        img_resp.raise_for_status()
        
        # Determine extension
        ext = "png"
        if ".svg" in final_url.lower(): ext = "svg"
        elif ".jpg" in final_url.lower() or ".jpeg" in final_url.lower(): ext = "jpg"
        
        save_path = f"c:\\Users\\xiao\\.gemini\\antigravity\\scratch\\odoo19\\custom_addons\\sz_shouzheng_homepage\\static\\src\\img\\clients\\client_masspower.{ext}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, 'wb') as f:
            f.write(img_resp.content)
        print(f"Successfully saved to {save_path}")
    else:
        print("Still no logo found.")

except Exception as e:
    print(f"Error: {e}")
