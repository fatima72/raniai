t = 1
n = 5
arr = [2, 5, 1, 3, 4]

bribe = 0
briben = 0
for i in range(n):
    if(arr[i]-1 > i):
        bribe = arr[i]-(i+1)
    else:
        bribe = 0
    if bribe > 2:
        print("Too chaotic")
        exit()
    briben += bribe
print(briben)
