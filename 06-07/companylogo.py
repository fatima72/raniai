"""
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""


s = input()

Dict={}
for x in sorted(s):
    Dict[x]=Dict.get(x,0)+1   

Dict_keys=sorted(Dict, key=Dict.get, reverse=True)  

for key in Dict_keys[:3]:
    print(key,Dict[key])