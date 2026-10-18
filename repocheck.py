import subprocess
from pathlib import Path

# folders we never want to search inside (they're huge and never contain your repos)
SKIP = {"node_modules", ".venv", "venv", "__pycache__", "target", "build", "dist"}


def find_repos(root):
    root = Path(root)
    repos = []

    try:
        items = list(root.iterdir())
    except PermissionError:
        return repos                          # NEW: macOS won't let us open this folder, skip it

    for item in items:
        if not item.is_dir() or item.name in SKIP or item.name.startswith("."):
            continue                          # NEW: skip files, junk folders and hidden folders
        if (item / ".git").exists():
            repos.append(item)                # found a repo, don't look inside it
        else:
            repos.extend(find_repos(item))    # not a repo, so look inside it

    return repos


def count_changes(repo):
    """Return how many files have uncommitted changes, or None if git failed."""
    result = subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None                           # git gave an error for this folder
    return len(result.stdout.splitlines())    # one line per changed file


if __name__ == "__main__":
    root = Path(input("Enter the root directory to search for repos (full path): ")).expanduser()

    if not root.is_dir():
        print(f"{root} is not a folder.")
        raise SystemExit(1)

    repos = sorted(find_repos(root))
    print(f"\nFound {len(repos)} repos in {root}\n")

    for repo in repos:
        changes = count_changes(repo)
        if changes is None:
            status = "error"
        elif changes == 0:
            status = "clean"
        else:
            status = f"{changes} changed"
        print(f"  {repo.name:<25} {status}")
