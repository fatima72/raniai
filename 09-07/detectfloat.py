"""
Validate float
Conditions:
Number can start with +, - or . symbol.
Number must contain at least 1 decimal value.
Number must have exactly one . symbol.
No exception while using float(N) on it
"""
import re


def validate(s):
    pattern = re.compile(r'^[+-.]?(\d)(\.\d)?$')

    matches = pattern.match(s)

    if (matches != None):
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    s = input()
    print(validate(s))
