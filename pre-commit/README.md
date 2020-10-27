# pre-commit
A good use of check_lines is to be used with pre-commit hooks.

### How to install it on a git repository
 - Install pre-commit :
```sh
pip install pre-commit
```
 - Copy .pre-commit-config.yaml into your repository.
 - Configure your repository with pre-commit :
```sh
pre-commit install
```
---
/!\ Be careful because `pip` may not set your `$PATH` correctly, you must
check in your home directory (~) by calling directly :
```sh
~/bin/pre-commit --version
```
or simply chamge your `$PATH` :
```sh
export $PATH+=/home/ryuki/bin:$PATH
```
It just depends on your need.
