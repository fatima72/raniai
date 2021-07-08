"""
Merge two sorted arrays in O(1) space
"""

arr = list(map(int,input().split()))

arr1 = list(map(int,input().split()))

m, n = (len(arr), len(arr1))


i = 0
j = 0

while(i<m and j<n):
    
    if(arr[i]<=arr1[j]):
        i+=1
        continue
    else:
        arr[i],arr1[j] = (arr1[j],arr[i])
        arr1.sort()
        

        
        
        
print(arr,arr1)
        
        