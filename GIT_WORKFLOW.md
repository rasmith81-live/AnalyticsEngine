# Git Workflow - AnalyticsEngine

**Project**: AnalyticsEngine  
**Repositories**: Dual remote setup  
**Date**: November 10, 2025

---

## Repository Configuration

### ✅ Configured Remotes

**Origin (Organization)**:
```
https://github.com/marketnova/AnalyticsEngine.git
```

**Personal (Backup/Fork)**:
```
https://github.com/rasmith81-live/AnalyticsEngine.git
```

---

## Daily Workflow

### 1. Pull Latest Changes

```powershell
# Pull from organization (primary)
git pull origin main
```

### 2. Create Feature Branch

```powershell
# Create and switch to feature branch
git checkout -b feature/your-feature-name

# Example:
git checkout -b feature/metric-tree-component
```

### 3. Make Changes and Commit

```powershell
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add metric tree component with D3.js"

# Or use conventional commits:
# feat: new feature
# fix: bug fix
# docs: documentation
# style: formatting
# refactor: code restructuring
# test: adding tests
# chore: maintenance
```

### 4. Push to Both Repositories

```powershell
# Option A: Push to both manually
git push origin feature/your-feature-name
git push personal feature/your-feature-name

# Option B: Use helper script (for main branch)
.\scripts\git_push_all.ps1
```

---

## Quick Commands

### Push to Both Remotes (Main Branch)

```powershell
# Use the helper script
.\scripts\git_push_all.ps1

# Or manually
git push origin main
git push personal main
```

### Check Remote Status

```powershell
# View configured remotes
git remote -v

# Check branch tracking
git branch -vv

# View remote details
git remote show origin
git remote show personal
```

### Sync Fork with Organization

```powershell
# Fetch from organization
git fetch origin

# Merge into your branch
git merge origin/main

# Push to personal
git push personal main
```

---

## Branch Strategy

### Main Branch
- `main` - Production-ready code
- Always synchronized between both remotes
- Protected (requires PR for organization)

### Feature Branches
- `feature/metric-tree`
- `feature/uml-diagram-viewer`
- `feature/calculation-handlers`
- Push to both remotes for backup

### Naming Convention
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Urgent fixes
- `docs/description` - Documentation
- `refactor/description` - Code improvements

---

## Common Workflows

### Creating a New Feature

```powershell
# 1. Start from main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes and commit
git add .
git commit -m "feat: implement new feature"

# 4. Push to both remotes
git push origin feature/new-feature
git push personal feature/new-feature

# 5. Create PR on GitHub (marketnova/AnalyticsEngine)
```

### Merging Feature to Main

```powershell
# 1. Switch to main
git checkout main

# 2. Pull latest
git pull origin main

# 3. Merge feature (after PR approved)
git merge feature/new-feature

# 4. Push to both remotes
git push origin main
git push personal main

# 5. Delete feature branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
git push personal --delete feature/new-feature
```

### Fixing a Bug

```powershell
# 1. Create bugfix branch
git checkout -b bugfix/fix-calculation-error

# 2. Fix and commit
git add .
git commit -m "fix: correct calculation error in SCOR handler"

# 3. Push to both
git push origin bugfix/fix-calculation-error
git push personal bugfix/fix-calculation-error

# 4. Create PR and merge
```

---

## Keeping Repositories in Sync

### Daily Sync

```powershell
# Morning routine
git checkout main
git pull origin main
git push personal main
```

### After Merging PR

```powershell
# Organization PR merged
git checkout main
git pull origin main

# Sync to personal
git push personal main
```

### Verify Sync Status

```powershell
# Check if remotes are in sync
git fetch origin
git fetch personal

# Compare branches
git log origin/main..personal/main
# (should show nothing if in sync)
```

---

## Troubleshooting

### Remotes Out of Sync

```powershell
# Force sync personal to match origin
git fetch origin
git checkout main
git reset --hard origin/main
git push personal main --force
```

### Merge Conflicts

```powershell
# Pull from origin
git pull origin main

# Resolve conflicts in files
# Edit files, then:
git add .
git commit -m "fix: resolve merge conflicts"

# Push to both
git push origin main
git push personal main
```

### Authentication Issues

```powershell
# Use GitHub CLI
gh auth login

# Or configure Git credential manager
git config --global credential.helper manager-core
```

---

## Automated Workflows

### Git Hooks (Optional)

Create `.git/hooks/pre-push`:

```bash
#!/bin/sh
# Automatically push to both remotes

echo "Pushing to origin..."
git push origin $2

echo "Pushing to personal..."
git push personal $2
```

### GitHub Actions (Optional)

Sync between repositories automatically using GitHub Actions.

---

## Best Practices

### ✅ Do's

- ✅ Always pull before starting work
- ✅ Use descriptive commit messages
- ✅ Push to both remotes regularly
- ✅ Create feature branches for new work
- ✅ Keep main branch clean and stable
- ✅ Review changes before committing

### ❌ Don'ts

- ❌ Don't commit directly to main (use PR)
- ❌ Don't push broken code
- ❌ Don't commit sensitive data (.env files)
- ❌ Don't force push to main
- ❌ Don't leave remotes out of sync

---

## Helper Scripts

### Push to All Remotes

```powershell
.\scripts\git_push_all.ps1
```

### Check Status

```powershell
# View status
git status

# View log
git log --oneline -10

# View remotes
git remote -v
```

---

## Repository URLs

### Organization (Primary)
- **GitHub**: https://github.com/marketnova/AnalyticsEngine
- **Clone**: `git clone https://github.com/marketnova/AnalyticsEngine.git`

### Personal (Backup)
- **GitHub**: https://github.com/rasmith81-live/AnalyticsEngine
- **Clone**: `git clone https://github.com/rasmith81-live/AnalyticsEngine.git`

---

## Current Status

```
✅ Remotes configured: origin + personal
✅ Main branch pushed to both
✅ Repositories synchronized
✅ Helper script created
```

---

## Quick Reference

```powershell
# Daily workflow
git pull origin main                    # Pull latest
git checkout -b feature/name            # Create branch
git add .                               # Stage changes
git commit -m "feat: description"       # Commit
git push origin feature/name            # Push to org
git push personal feature/name          # Push to personal

# Sync main to both
.\scripts\git_push_all.ps1              # Use helper script

# Check status
git remote -v                           # View remotes
git branch -vv                          # View branches
git status                              # Check status
```

---

## Summary

Your AnalyticsEngine project is now configured with:
- ✅ Dual remote setup (organization + personal)
- ✅ Both repositories synchronized
- ✅ Helper script for easy pushing
- ✅ Clear workflow documented

**All changes are now backed up in both repositories!** 🚀
