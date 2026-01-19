import requests
from bs4 import BeautifulSoup
import re
import os

url = "https://mass-power.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all images with 'logo' in src, alt, or class
    images = soup.find_all('img')
    candidates = []
    
    for img in images:
        src = img.get('src')
        if not src:
            continue
        
        # Resolve relative URLs
        if not src.startswith('http'):
            if src.startswith('/'):
                src = "https://mass-power.com" + src
            else:
                src = "https://mass-power.com/" + src
                
        # Check for 'logo' keyword
        if 'logo' in src.lower() or 'logo' in str(img.get('id', '')).lower() or 'logo' in str(img.get('class', '')).lower():
            candidates.append(src)
            print(f"Found candidate: {src}")

    # Start downloading the first likely candidate
    if candidates:
        logo_url = candidates[0]
        print(f"Attempting to download: {logo_url}")
        
        img_resp = requests.get(logo_url, headers=headers, timeout=10)
        img_resp.raise_for_status()
        
        ext = logo_url.split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = "png" # Default fallback
        
        save_path = f"c:\\Users\\xiao\\.gemini\\antigravity\\scratch\\odoo19\\custom_addons\\sz_shouzheng_homepage\\static\\src\\img\\clients\\client_masspower.{ext}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, 'wb') as f:
            f.write(img_resp.content)
        print(f"Successfully saved to {save_path}")
    else:
        print("No logo candidates found.")

except Exception as e:
    print(f"Error: {e}")
