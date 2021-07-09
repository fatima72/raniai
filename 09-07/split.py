"""
Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s
It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.

"""
import re

s = "100,000,000.000"
pattern = re.compile(r'[,.]')

print(re.split(pattern, s))
