"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
"""
m,n = list(map(int,input().split()))


matrix = []
zero_column = []
for _ in range(m):
    column = list(map(int,input().split()))
    for j in range(n):
        if(column[j]==0):
            column = [0]*n
            zero_column.append(j)
            break
    matrix.append(column)
            

    
for j in zero_column:
    for i in range(m):
        matrix[i][j] = 0
        
print(matrix)

            