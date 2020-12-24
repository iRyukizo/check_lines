# check_lines
A little python script to check lines in your **C** files.

### Must have:
 - Following programs:
```
ctags
python3
```
---
### How to use:
```sh
check_lines [options] [files]
```
Examples:
```sh
[ryuki@apollo11 Project]$ check_lines main.c
main.c:49:18: warning: This function is too long: 34 lines [expected 25 lines].
int main(void)
    ^
[ryuki@apollo11 Project]$ check_lines -l 20 --remaining main.c
-- remaining lines --
File: main.c
  Function: main         (5:4):	        -14 lines
  Function: print_stuff (10:5):          10 lines
[ryuki@apollo11 Project]$ check_lines -f main.c other.c
-- functions counter --
  Total of all     functions:	 14
  Total of static  functions:	 2
  Total of normal  functions:	 9
File: main.c
  Total   functions:	 2
  Static  functions:	 0
  Normal  functions:	 2
File: other.c
  Total   functions:	 12
  Static  functions:	 5
  Normal  functions:	 7
```
---
### How to install:
```sh
pip install check-lines
```
See: https://pypi.org/project/check-lines/
