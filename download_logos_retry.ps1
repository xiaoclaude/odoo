$dest = "c:\Users\xiao\.gemini\antigravity\scratch\odoo19\custom_addons\sz_shouzheng_homepage\static\src\img"

# Retry CGN
Try {
    Write-Host "Downloading CGN..."
    Invoke-WebRequest -Uri "https://www.cgnpc.com.cn/cgn/xhtml/images/mb_top_logo.jpg" -OutFile "$dest\client_cgn.jpg" -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -Headers @{Referer="https://www.cgnpc.com.cn/"} -ErrorAction Stop
    Write-Host "CGN Success."
} Catch {
    Write-Host "CGN Failed: $_"
}

# Retry Chengxin
Try {
    Write-Host "Downloading Chengxin..."
    Invoke-WebRequest -Uri "https://omo-oss-image.thefastimg.com/portal-saas/new2023112319092677311/cms/image/bf68e10e-9fb6-4398-a309-10b7be6a66e3.png" -OutFile "$dest\client_chengxin.png" -UserAgent "Mozilla/5.0" -Headers @{Referer="http://www.cxzyjt.cn/"} -ErrorAction Stop
    Write-Host "Chengxin Success."
} Catch {
    Write-Host "Chengxin Failed: $_"
}
