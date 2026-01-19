$dest = "c:\Users\xiao\.gemini\antigravity\scratch\odoo19\custom_addons\sz_shouzheng_homepage\static\src\img\clients"
New-Item -ItemType Directory -Force -Path $dest

# Vilary (Official)
Try {
    Write-Host "Downloading Vilary Official..."
    Invoke-WebRequest -Uri "http://www.wllxcl.com/templates/wll/images/logo.png" -OutFile "$dest\client_vilary.png" -UserAgent "Mozilla/5.0" -ErrorAction Stop
    Write-Host "Vilary Success."
} Catch {
    Write-Host "Vilary Failed: $_"
}

# Emdoor (Official)
Try {
    Write-Host "Downloading Emdoor Official..."
    Invoke-WebRequest -Uri "https://img.emdoor.net/wstmart/home/view/default/svg/logo.svg" -OutFile "$dest\client_emdoor.svg" -UserAgent "Mozilla/5.0" -ErrorAction Stop
    Write-Host "Emdoor Success."
} Catch {
    Write-Host "Emdoor Failed: $_"
}
