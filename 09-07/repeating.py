
import re
S = input()
pattern = re.compile(r'(\w)\1')

print(S[pattern.search(S).span()[0]])
