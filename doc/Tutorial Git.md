# Tutorial Git 

Basic commands for git (Distributed Version Control System)

by djclavero@yahoo.com 


## Basics git

### Version

```
git --version
git help <command>
```

### Clone repository

```
# GitHub
git clone https://github.com/djclavero/template-python-projects.git

# Bitbucket
$ git clone https://djclavero@bitbucket.org/djclavero/template-python-projects.git

# Checking 
$ git remote -v
$ git remote show origin
```

### Create local repository

```
# Go inside the project folder
$ git init

# Checking a hidden directory .git was created
$ dir /A 

# Add remote repository
$ git remote add origin http://github.com/djclavero/template-python-projects

# Delete the local repository by deleting the project directory
# Delete the remote repository in the Web
```

### Configuration

```
$ git config --global user.name 'djclavero'
$ git config --global user.email djclavero@yahoo.com

# Checking
$ git config user.name
$ git config user.email

# Configuration
$ git config --list
$ git config --list --global    # all projects
$ git config --list --styem     # system
$ git config --list --local     # current project

# Using the Editor
$ git config core.editor
$ git config core.editor 'C:\Program Files\Sublime Text 3\sublime_text.exe'

$ git config -e --global
```

### Basic commands

```
# git status
$ git status
$ git status -s

# git diff
$ git diff -r HEAD <file>
$ git diff --staged
$ git diff <hash1> <hash2>  # at least 5-hex chars)
$ git diff <branch1>..<branch2>

# git add
$ git add <file>        # staging file
$ git reset HEAD <file> # unstage file  (git checkout -- <file>)

$ git add .             # add all files
$ git checkout -- .     # undo all file (git reset)

# Delete file
$ git rm <file>
$ git rm *

# Rename file
$ git mv old_name new_name
```

### Commit 

```
$ git commit -m "here a description message"
```

### Upload to repository

```
# git push
$ git push origin master

$ git push -f origin master     # flag --force
```

### Download from repository

```
# git fetch (git pull is like git fetch + git merge)
$ git fetch origin
```

## Project history

git log:

```
$ git log

# Last n commits
$ git log -5

# Short log
$ git shortlog -s

# Graph (--oneline reduce hash to 7 chars)
$ git log --oneline --graph
```

git show:

```
# Show commits (just required 4 chars of the hash)
$ git show <commit id>
```

Restore old version:

```
# Go to previous commit
$ git checkout <commit id>

# Come back to latest changes
$ git checkout master

# Restore old file
$ git checkout <commit id> <file>
```

Get the GIT ID of any object (commit, annotated tag, tree, blob):

```
# Get SHA-1 hast of a file (40-hex chars)
git hash-object <file>
```

### Tags

```
# List tags
$ git tag

# Create lightweight tag
$ git tag mytag
$ git show mytag
$ git checkout mytag

# Create annotate tag (p.e. Versions)
$ git tag -a -m "includes feature 1" v1.1
$ git show v1.1
$ git checkout v1.1  

# Delete tag 
$ git tag -d v1.1

# Upload tag to repository
$ git push origin v1.1
$ git push origin --tags  # all tags
```

## Branches

### Create branch

Short-lived branches: TOPIC (feature, bug fix, config changes, etc.)

Long-lived  branches: MASTER, DEVELOP and RELEASE

```
# List branches (at least exists 'master' branch)
$ git branch
$ git branch -vv

# Create branch
$ git branch featureX

# Switch branch
$ git checkout featureX

# Delete local branch
$ git branch -D featureX

# Delete remote branch
$ git push origin --delete featureX 

# To fix a bug create branch from previous version
$ git checkout -b <new_branch> <old_version_tag>
```

### Merge

```
# Fast-Forward Merge (linear history)
$ git checkout master
$ git merge featureX
$ git branch -d featureX

# Merge Commit (multiple branches)
$ git checkout master
$ git merge --no-ff featureX
$ git branch -d featureX
```

## Tips

Returning to an old revision:

```
# Rewind your HEAD branch to the specific version
$ git reset --hard <commit id>      
```

Reset the HEAD to n commits back:

`$ git reset --hard HEAD~1  # Previous commit`

Restoring a version in a new local branch:

`$ git checkout -b old-project-state <hash>   # New branch: old-project-state`


## License
[MIT](https://choosealicense.com/licenses/mit/)