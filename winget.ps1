# Memastikan TLS 1.2 digunakan untuk koneksi ke PSGallery
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Pengecekan Hak Akses Administrator
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "Script ini membutuhkan hak akses Administrator. Silakan buka PowerShell sebagai Administrator (Run as Administrator) dan jalankan kembali."
    exit
}

$progressPreference = 'silentlyContinue'

Write-Host "Installing PackageProvider NuGet..." -ForegroundColor Cyan
Install-PackageProvider -Name NuGet -Force | Out-Null

Write-Host "Installing WinGet PowerShell module from PSGallery..." -ForegroundColor Cyan
Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery -AllowClobber | Out-Null

Write-Host "Using Repair-WinGetPackageManager cmdlet to bootstrap WinGet..." -ForegroundColor Cyan
Repair-WinGetPackageManager -AllUsers

Write-Host "Done! WinGet is ready to use." -ForegroundColor Green