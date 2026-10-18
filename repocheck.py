from pathlib import Path

def find_repos(root):
    root = Path(root)
    repos = []

    for item in root.iterdir():
        if not item.is_dir():
            continue                              # skip files
        if (item / ".git").exists():
            repos.append(item)                    # found a repo, don't look inside it
        else:
            repos.extend(find_repos(item))        # not a repo, so look inside it

    return repos

root = input("Enter the root directory to search for repos (full path): ")
repos = find_repos(root)

print(f"Found {len(repos)} repos in {root}\n")
for repo in repos:
    print(f"  {repo.name}")
