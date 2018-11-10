# Tutorial Conda 

Conda basic commands 

by djclavero@yahoo.com 

---

Links:

[Anaconda 3](https://www.anaconda.com/download/)

[Conda documentation](https://conda.io/docs/user-guide/getting-started.html)

---


## Managing Conda

### Versions

```
# Check versions for Conda, Python and Pypi
$ conda  --version
$ python --version
$ pip    --version

# Update versions for Conda, Python and Pypi
$ conda update conda
$ conda update python
$ pip install --upgrade pip
```

### Packages

```
# conda
$ conda install <package>
$ conda update  <package>
$ conda remove  <package>

# pip
$ pip install   <package>
$ pip install   --upgrade <package>
$ pip uninstall <package>

# List packages
$ conda list
```

## Create enviroment

Create enviroment basics:

```
$ conda create -n myenv

# Install and list packages in myenv
$ conda install -n myenv <package>
$ conda list -n myenv
```

Create enviroment with a specific version of python:

```
# Enviroment with Python 3
$ conda search python
$ conda create -n py37 python='3.7.0'

# Create env with all packets of anaconda
$ conda create -n py37 python='3.7.0' anaconda
```

Create enviroment with a specific package:

```
# Create env 'science' with a the package 'scipy'
$ conda create  -n science python
$ conda install -n science scipy
```

Clone enviroment:

```
# Make file with list of all packages
$ conda list --explicit  >  spec-file.txt

# Clone enviroment from file
$ conda create  -n myenv  --file 'spec-file.txt'

# Install all listed packages from file in my env
$ conda install -n myenv  --file 'spec-file.txt' 
```

### Activate enviroment

```
# List enviroments (default env is 'base')
$ conda env list
    base *
    myenv

# Activate env 'myenv'
$ conda activate myenv

# Deactivate (back to env 'base')
$ conda deactivate

# Delete env 'myenv'
$ conda remove -n myenv all
```

## Local packages

Installing local packages:

```
# conda
$ conda install --offline C:\example-package.tar.gz 

# pip
$ pip install C:\example-package.tar.gz

# python
$ python setup.py install
```

Installing via Web:

```
# Start Web Server
$ python -m SimpleHTTPServer 9000

# Install package
$ pip install --extra-index-url = http://127.0.0.1:9000/example-package.tar.gz
```

Accesing local packages appending the directory project to the path:

```python
import sys
sys.path.append('C:\\Users\\David\\Workspace\\template-python-projects')
```

Accesing local packages by copy of the project to the path:

```python
import sys
# print the path 
print(sys.path)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)