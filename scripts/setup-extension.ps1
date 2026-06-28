#Requires -Version 5.1
<#
.SYNOPSIS
  Builds the Leetcode-To-Github browser extension from source.

.DESCRIPTION
  Clones (if missing), installs npm deps, and builds the extension.
  After this script finishes, load extension\leetcode-to-github\dist
  in chrome://extensions (Developer mode → Load unpacked).
#>

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ExtDir = Join-Path $ProjectRoot "extension\leetcode-to-github"
$DistDir = Join-Path $ExtDir "dist"

Write-Host "`n=== Git LeetCode Streak — Extension Setup ===" -ForegroundColor Cyan

if (-not (Test-Path $ExtDir)) {
    Write-Host "Cloning Leetcode-To-Github..." -ForegroundColor Yellow
    $ExtParent = Split-Path $ExtDir -Parent
    New-Item -ItemType Directory -Force -Path $ExtParent | Out-Null
    git clone --depth 1 https://github.com/h-sharda/Leetcode-To-Github.git $ExtDir
}

Set-Location $ExtDir
Write-Host "Installing dependencies..." -ForegroundColor Yellow
npm install --include=dev

Write-Host "Building extension..." -ForegroundColor Yellow
& (Join-Path $ExtDir "node_modules\.bin\tsc.cmd") -b
if ($LASTEXITCODE -ne 0) { throw "TypeScript build failed" }
& (Join-Path $ExtDir "node_modules\.bin\vite.cmd") build
if ($LASTEXITCODE -ne 0) { throw "Vite build failed" }

if (Test-Path $DistDir) {
    Write-Host "`nBuild successful!" -ForegroundColor Green
    Write-Host "Load this folder in your browser:" -ForegroundColor Green
    Write-Host "  $DistDir" -ForegroundColor White
    Write-Host "`nNext steps:" -ForegroundColor Cyan
    Write-Host "  1. Open chrome://extensions (or edge://extensions)"
    Write-Host "  2. Enable Developer mode"
    Write-Host "  3. Click Load unpacked → select the dist folder above"
    Write-Host "  4. Configure GitHub token in extension Settings (see README.md)"
} else {
    throw "dist folder not found after build"
}
