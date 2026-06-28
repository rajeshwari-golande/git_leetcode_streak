#Requires -Version 5.1
<#
.SYNOPSIS
  Initializes git for the git_leetcode_streak repo.

.DESCRIPTION
  Runs git init, first commit, and prints commands to connect GitHub remote.
#>

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $ProjectRoot

Write-Host "`n=== Git LeetCode Streak — Repo Init ===" -ForegroundColor Cyan

if (-not (Test-Path (Join-Path $ProjectRoot ".git"))) {
    git init
    git add .
    git commit -m "Initial commit: LeetCode streak repo"
    git branch -M main
    Write-Host "Local git repo initialized on branch main." -ForegroundColor Green
} else {
    Write-Host "Git repo already exists — skipping init." -ForegroundColor Yellow
}

Write-Host "`n--- Connect to GitHub ---" -ForegroundColor Cyan
Write-Host @"

1. Create a new repo on GitHub: https://github.com/new
   Name: git_leetcode_streak

2. Run these commands (replace YOUR_USERNAME):

   git remote add origin https://github.com/YOUR_USERNAME/git_leetcode_streak.git
   git push -u origin main

3. Create a GitHub PAT with Contents: Read and write on this repo.
   https://github.com/settings/tokens

4. Run: .\scripts\setup-extension.ps1
   Then configure the extension with your username, repo name, and token.

"@ -ForegroundColor White
