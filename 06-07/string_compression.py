"""
You are given a string S. 
Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences 
of the character 'C' with (c,X) in the string.
"""

from itertools import groupby

S = input()


print(*[(int(k),len(list(c))) for k, c in groupby(S)])
