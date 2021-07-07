"""
You are given a positive integer n. Print a numerical triangle of height n-1
"""
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)
