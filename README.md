# check_lines
A little python script to check lines in your c files.

### Must have:
 - Following packages:
```
ctags
python3
```
---
### How to use:
```sh
./check_lines.py [files]
```
Examples:
```sh
[ryuki@apollo11]~ ./check_lines.py main.c
main.c:49:18: warning: This function is too long: 34 lines [expected 25 lines].
int main(void)
    ^
```
---
### You may want to do:
```sh
ln -s check_lines/check_lines.py /usr/bin/check_lines
```
In that case just run :
```sh
./install.sh
```
