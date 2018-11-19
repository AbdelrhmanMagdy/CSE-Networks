## CRC implementation (CSE-2019) Ain-Shams University

**How to use:**
- download the files from the repository.
- open each file through the terminal and pass the args as stdin as follow.

### Samples:

```
$ python3 generator.py 1101011111 10011
11010111110010
10011
$ python3 verifier.py 11010111110010 10011
msg is correct!
$ python3 alter.py 11010111110010 1
10010111110010
$ python3 verifier.py 10010111110010 10011
wrong msg!
$ python3 generator.py 11010111111
args: msg g
$ python3 verifier.py 
args: packet g
$ python3 alter.py
args: packet index
$ python3 alter.py 1011 5
index out of range!
```
