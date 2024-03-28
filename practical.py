import numpy as np
import random
arr=np.array([[0,0,0],[0,0,0]])
for i in range(2):
    for j in range(2):
        arr[i][j]=np.random.randint(0,100) 
print(arr) 

for i in range(2):
    for j in range(2):
        if(arr[i][j]%2==0):
           arr[i][j]=arr[i][j]*arr[i][j]
   
print(arr)

def sum(a):
   for i in range(2):
      s=0
      for j in range(2):
          s=s+a[i][j]
      print("sum of row ",i+1 ,"is", s)
          
sum(arr)

arr1=arr.flatten()
print(arr1)

