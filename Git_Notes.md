# 1. Git and GitHub

- Revised some GitHub Essentials
- Branching Strategies - Feature, Release, Hotfix
- Collaboration Methods- Fork, Shared Repo
- Issue tracker, Shared Goals, PR Templates
- Opening and Reviewing a PR, Naming Conventions
- Best Practices
- Squash, Amend, CI/CD, LFS
- Cherry Pick, Git Hooks

### Best Practices

- Descriptive Commit Messages - Imperative mood
- Branch Naming Conventions
- Clean Commit History
- Use of .gitignore
- Pull to avoid Conflicts
- Use Feature Flags Instead of Long-Lived Feature Branches
- Avoid Pushing env and config files
- Use Git Hooks for Automation - Common hooks --> pre-commit, pre-push, pre-receive and commit-msg
- Keep Your Repositories Small - git lfs track "\*.zip" --> For Large Files
- Regularly Review and Clean Up

**Examples:**

```
git checkout -b feature/user-authentication
# Work on feature, commit changes
git push origin feature/user-authentication

# To modify recent commits
git commit --amend

# Squash last 3 commits into one
git rebase -i HEAD~3

# Pull to avoid Conflicts
git pull --rebase origin main
git push origin feature-branch

# Removing a Leaked Secret
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch .env' --prune-empty --tag-name-filter cat -- --all

# Pre-Commit Hook to Run Tests
#!/bin/sh
npm test || exit 1

# Using Git LFS for Large Files
git lfs track "*.zip"

# Deleting Merged Branches
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# Cherry Pick
git cherry-pick code
```
