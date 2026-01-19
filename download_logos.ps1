$clients = @{
    "client_catl.svg" = "https://www.catl.com/en/template/1/en/_files/svg/logo.svg"
    "client_deepoon.png" = "https://www.dpvr.com/wp-content/uploads/2022/05/cropped-dpvr-logo-black-600x172.png"
    "client_goldlok.svg" = "https://www.xn--fjq5py34j65v.com/assets/logo-CBPI-jzC.svg"
    "client_cgn.jpg" = "https://www.cgnpc.com.cn/cgn/xhtml/images/mb_top_logo.jpg"
    "client_chengxin.png" = "https://omo-oss-image.thefastimg.com/portal-saas/new2023112319092677311/cms/image/bf68e10e-9fb6-4398-a309-10b7be6a66e3.png"
}

$dest = "c:\Users\xiao\.gemini\antigravity\scratch\odoo19\custom_addons\sz_shouzheng_homepage\static\src\img"

foreach ($key in $clients.Keys) {
    Try {
        Write-Host "Downloading $key..."
        Invoke-WebRequest -Uri $clients[$key] -OutFile "$dest\$key" -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -ErrorAction Stop
        Write-Host "Success."
    } Catch {
        Write-Host "Failed to download $key : $_"
    }
}
