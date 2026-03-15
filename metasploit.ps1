[CmdletBinding()]
Param(
    $DownloadURL = "https://windows.metasploit.com/metasploitframework-latest.msi",
    $DownloadLocation = "$env:APPDATA\Metasploit",
    $InstallLocation = "C:\Tools\Metasploit", # Disarankan membuat subfolder spesifik
    $LogLocation = "$env:APPDATA\Metasploit\install.log"
)

# 1. Tambahkan pengecualian Windows Defender (Wajib untuk Metasploit)
# Ini mencegah Defender menghapus file saat proses download maupun instalasi
Write-Host "[*] Menambahkan pengecualian Windows Defender..." -ForegroundColor Yellow
Add-MpPreference -ExclusionPath $DownloadLocation -ErrorAction SilentlyContinue
Add-MpPreference -ExclusionPath $InstallLocation -ErrorAction SilentlyContinue

# 2. Buat direktori jika belum ada
If(! (Test-Path $DownloadLocation) ){
    New-Item -Path $DownloadLocation -ItemType Directory | Out-Null
}

If(! (Test-Path $InstallLocation) ){
    New-Item -Path $InstallLocation -ItemType Directory | Out-Null
}

$Installer = "$DownloadLocation\metasploit.msi"

# 3. Unduh file MSI
Write-Host "[*] Mengunduh Metasploit Framework. Harap tunggu..." -ForegroundColor Cyan
Invoke-WebRequest -UseBasicParsing -Uri $DownloadURL -OutFile $Installer

# 4. Instalasi menggunakan msiexec
# /i = install, /qn = quiet (tanpa UI)
Write-Host "[*] Menginstal Metasploit secara silent..." -ForegroundColor Cyan
$MsiArgs = "/i `"$Installer`" /qn /log `"$LogLocation`" INSTALLLOCATION=`"$InstallLocation`""

# Gunakan Start-Process agar script menunggu proses instalasi selesai (-Wait)
Start-Process -FilePath "msiexec.exe" -ArgumentList $MsiArgs -Wait -NoNewWindow

Write-Host "[+] Instalasi Metasploit selesai!" -ForegroundColor Green