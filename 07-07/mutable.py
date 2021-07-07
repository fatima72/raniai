"""
You are given an immutable string, and you want to make changes to it.
"""

s = input()
index, character = input().split()
index = int(index)

print(s[:int(index)] + character + s[int(index)+1:])