"""
In a list of one to n elements, one digit is missing, other is extra
Find them
"""


arr = [2,2,3,4]
n = 4

temp = [i for i in range(1,n+1)]

for num in temp:
    if num in arr:
        arr.remove(num)
    else:
        print("Missing",num)


print("Extra", arr[0])
