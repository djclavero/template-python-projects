# [template-python-projects](https://github.org/djclavero/template-python-projects) 

Template Project for Python using git 

by djclavero@yahoo.com 


## Installation

### Requirements
* Linux/Windows
* Python 2.7 and up

`$ pip install template-python-projects`

## Usage

```python
from video.formats import mp4play

# Call function 
mp4play.test_mp4play()
```

## Create distribution 
```
# Check the package first
$ python setup.py --help-commands
$ python setup.py check

# ¡¡¡ Create distribution !!!!
$ python setup.py sdist

# (Optional) Binary distribution
$ python setup.py bdist --formats=wininst

# (Optional) Develop distribution
$ python setup.py develop
$ python setup.py develop --uninstall 
```

## Upload release 
```
$ twine upload dist/*   # pip install twine (if required)
```

### .pypirc file (c:\Users\David\.pypirc)
```
[pypi]
repository = https://upload.pypi.org/legacy/
username   = djclavero
```

## Control of Versions (Git)
Create local repository:
```
# Create local repository
$ git init 

# Create remote repository 'template-python-projects' in GitHub
```

Configuration:
```
$ git config --global user.name 'djclavero'
$ git config --global user.email djclavero@yahoo.com

# Add remote repository
$ git remote add origin https://github.org/djclavero/template-python-projects 

# Set .gitignore file
$ git config --global core.excludesFile C:\Users\David\.gitignore
```

Upload to remote repository:
```
# Add files and commit
$ git status
$ git add .  
$ git commit -m "init commit"

# Upload to repository
$ git push origin master 
```

### .gitignore file 
```
# ignore bytecode python files
*.pyc
# ignore distribution files
dist/
*.egg-info/
# ignore spyder project files
.spyproject/

DocuTech/
Software/
.ipynb_checkpoints/  # Jypyter
```


## License
[MIT](https://choosealicense.com/licenses/mit/)