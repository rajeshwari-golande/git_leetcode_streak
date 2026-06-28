# Git LeetCode Streak

Automatically commit every LeetCode solution to GitHub so your **GitHub contribution graph stays green** while you practice.

This repo is your **solutions archive**. A browser extension watches LeetCode and pushes accepted solutions here via the GitHub API — one commit per solve.

---

## Quick start (≈10 minutes)

### Step 1 — Push this repo to GitHub

1. Create a new repo on GitHub named `git_leetcode_streak` (public or private).
2. In this folder, run:

```powershell
git init
git add .
git commit -m "Initial commit: LeetCode streak repo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/git_leetcode_streak.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2 — Create a GitHub Personal Access Token

1. Open [GitHub → Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens).
2. **Generate new token (classic)**.
3. Name it e.g. `leetcode-streak`.
4. Scope: **Only select repositories** → pick `git_leetcode_streak`.
5. Permission: **Contents → Read and write**.
6. Copy the token (you won't see it again).

### Step 3 — Install the browser extension

**Option A — Leetcode-To-Github (included, recommended)**

Already cloned under `extension/leetcode-to-github/`. Build and load it:

```powershell
.\scripts\setup-extension.ps1
```

Then in Chrome/Edge:

1. Go to `chrome://extensions` (or `edge://extensions`).
2. Enable **Developer mode**.
3. Click **Load unpacked** → select:
   `extension\leetcode-to-github\dist`

**Option B — LeetHub-3.0 (fully automatic, no build)**

Install from the [Chrome Web Store](https://chromewebstore.google.com/detail/leethub/aciombdipochlnkbpcbgdpjffcfdbggi) or [GitHub releases](https://github.com/raphaelheinz/LeetHub-3.0/releases). After install, authorize GitHub and point it at this same repo.

| | Leetcode-To-Github | LeetHub-3.0 |
|---|---|---|
| Trigger | Click **Post to GitHub** after solve | Auto on accepted submission |
| Setup | PAT token | OAuth (one click) |
| Best for | Control over each commit | Hands-free streak |

### Step 4 — Configure the extension

**Leetcode-To-Github settings** (extension icon → Settings):

| Field | Value |
|---|---|
| GitHub Username | your username |
| Repository Name | `git_leetcode_streak` |
| GitHub Token | paste your PAT |

**Recommended templates** (copy from `extension-config.template.json`):

| Setting | Suggested value |
|---|---|
| Default Path | `solutions/<DIFFICULTY>` |
| Default File Name | `<PROBLEM_NO>-<PROBLEM_NAME>.<LANGUAGE>` |
| Default Commit Message | `Solve: <PROBLEM_NO>. <PROBLEM_NAME> (<DIFFICULTY>)` |

### Step 5 — Solve a problem

1. Go to [leetcode.com](https://leetcode.com) and solve any problem.
2. **Leetcode-To-Github:** click **Post to GitHub** → **Commit to GitHub**.
3. **LeetHub:** wait ~4 seconds after "Accepted" (don't edit the editor until sync finishes).

Check your repo on GitHub — you should see a new commit and a green square on your profile for today.

---

## How GitHub streaks work

- GitHub counts **commits** on the default branch (`main`) toward your contribution graph.
- Commits made by the extension via the API are attributed to **your account** (using your token/OAuth).
- **One accepted LeetCode solve = one commit = one contribution day** (multiple commits the same day still count as one green square).
- Miss a day? Solve one problem the next day to keep the streak alive.

---

## Folder layout

```
git_leetcode_streak/
├── solutions/          ← your LeetCode code lands here
├── extension/
│   └── leetcode-to-github/   ← browser extension source
├── scripts/
│   ├── setup-extension.ps1   ← build & load instructions
│   └── init-repo.ps1           ← git init helper
├── extension-config.template.json
└── README.md
```

Example after a few solves:

```
solutions/
├── Easy/
│   ├── 1-two-sum.py
│   └── 20-valid-parentheses.py
├── Medium/
│   └── 3-longest-substring-without-repeating-characters.py
└── Hard/
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Commit doesn't appear on profile | Ensure PAT has **Contents: write**; repo default branch is `main` |
| Extension button missing | Refresh LeetCode; confirm extension is enabled on `leetcode.com` |
| LeetHub sync fails | Wait 4s after submit; use manual sync button next to notes |
| Wrong file path | Re-check templates in extension Settings |
| Token expired | Regenerate PAT and update extension settings |

---

## Other extensions (alternatives)

- [LeetHub-3.0](https://github.com/raphaelheinz/LeetHub-3.0) — automatic sync, Chrome Web Store
- [LeetSync](https://github.com/LeetSync/LeetSync) — OAuth + LeetCode API
- [Code-Ledger](https://github.com/Life-Experimentalist/Code-Ledger) — multi-platform, analytics

All work the same way: commits to **this** repo maintain your streak.

---

## License

Solutions you write are yours. Extension code in `extension/` follows its upstream license (MIT).
