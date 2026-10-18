<div align="center">

# 🔍 repocheck

**The git status of every repo you own, in one command.**

![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue?logo=python&logoColor=white)
![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow)

</div>

---

Got a folder full of projects and no idea which ones have uncommitted work?
`repocheck` scans a directory, finds every git repo inside it (however deeply
nested), and tells you which are **clean** and which **need attention**.

No more `cd`-ing into twenty folders to run `git status`.

## ✨ Features

- **Finds repos automatically**: point it at a folder and it digs through subfolders for you
- **One-glance summary**: `clean`, `N changed`, or `error` for every repo
- **Fast and tidy**: skips `node_modules`, virtualenvs, build output and hidden folders
- **Safe**: read-only, it only ever runs `git status`
- **Zero dependencies**: just Python and git

## 🚀 Quick start

```bash
git clone https://github.com/xandertaylorx/repocheck.git
cd repocheck
python3 repocheck.py
```

When prompted, enter the folder that holds your projects (`~` works):

```
Enter the root directory to search for repos (full path): ~/Developer
```

## 📋 Example output

```
Found 4 repos in /Users/you/Developer

  guesstheamount            clean
  jarvis                    3 changed
  stride-learn              clean
  taskr                     1 changed
```

| Status        | Meaning                                              |
| ------------- | ---------------------------------------------------- |
| `clean`       | Nothing to commit                                    |
| `N changed`   | `N` files are modified, staged or untracked          |
| `error`       | git couldn't read the repo (corrupt, or no access)   |

## ⚙️ How it works

1. **Walk** the folder you give it, looking for a `.git` directory.
2. **Skip** junk it never needs to enter: `node_modules`, `.venv`, `venv`,
   `__pycache__`, `target`, `build`, `dist`, and any hidden folder.
3. **Stop** at each repo found (it doesn't search inside a repo for more).
4. **Run** `git status --porcelain` in each one and count the changed files.

Folders macOS won't let it open are skipped quietly instead of crashing the scan.

## 📦 Requirements

- Python 3.7 or newer
- `git` available on your `PATH`

## 🗺️ Roadmap

- [ ] Take the folder as an argument: `repocheck ~/Developer`
- [ ] Show unpushed and unpulled commits
- [ ] Coloured table output
- [ ] Install with `pip`

Ideas and pull requests are welcome.

## 📄 Licence

[MIT](LICENSE)
