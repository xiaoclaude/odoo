$dest = "c:\Users\xiao\.gemini\antigravity\scratch\odoo19\custom_addons\sz_shouzheng_homepage\static\src\img\clients"
Try {
    Write-Host "Retry Emdoor..."
    Invoke-WebRequest -Uri "https://img.emdoor.net/wstmart/home/view/default/svg/logo.svg" -OutFile "$dest\client_emdoor.svg" -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -Headers @{Referer="https://www.emdoor.net/"} -ErrorAction Stop
    Write-Host "Emdoor Success."
} Catch {
    Write-Host "Emdoor Failed: $_"
}
