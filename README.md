# CTFlearn
### 1003.py
https://ctflearn.com/challenge/1003
This challenge was a reversing challenge.  An ELF executable was provided.  When executed, if no arguments were provided on the command line, it displayed usage.  If one argument was provided, then it would check if the argument was the flag.  If "-v" was provided as the second argument, then the ELF file would output debug messages about the first argument, which allowed me to brute force the algorithm.

I used Ghidra to review the assembly and also the decompiled code and python to brute force the chars in the kernel string.

![alt text](https://github.com/jaemsz/CTFlearn/blob/main/image.jpg?raw=true)
