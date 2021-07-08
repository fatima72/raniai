

def mergesort(arr,l,r):
    if len(arr)>1:
        m = (l+r-1)//2
        mergesort(arr,l,m)
        mergesort(arr,m,r)
        merge(arr,l,m,r)
        
        


def merge(arr, l, m, r):
    i,j,k = [0,0,0]
    
    while i<m and j<r:
        if(arr[i]<arr[j]):
            arr[k] = arr[i]
            i=+1
        else:
            arr [k] = arr[j]
            j+=1
        
        k+=1
        
    while i<m:
        arr[k] = arr[i]
        i+=1
        k+=1
        
    while j<r:
        arr[k] = arr[j]
        j+=1
        k+=1
        
    arr[:] = arr
    
    
if __name__ == "__main__":
    
    arr  = list(map(int,input().split()))
    mergesort(arr,0,len(arr))
    print(arr)   
    