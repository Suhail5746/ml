import numpy as np
# # list=[1,2,3]
# # arr=np.array(list)
# # print(type(arr))

# # arr=np.array([[1,2,3],[4,5,6]])   #2d array
# # print(arr)

# # arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
# # print(arr)
# # print(arr.ndim)
# # print(arr[0,1,2])
# # print(arr[0:2,0:1,0:1])

# # arr=np.arange(1,6)
# # print(arr)

# # arr=np.arange(1,10,2)
# # print(arr)

# # arr=np.linspace(0,10,5)  # 5 equi distance point b/w 0 & 10
# # print(arr)

# # arr=np.ones((3,4))
# # print(arr)

# # arr=np.zeros((2,3))
# # print()

# # arr=np.full((3,3),3.14)
# # print(arr)

# # x=np.random.rand(5,2)   #b/w 0 & 1
# # print(x)

# # print(x.transpose())
# # print(x.mean())

# # print(x.astype(int))

# # arr=np.random.uniform(3,5,size=(5,2))
# # print(arr)

# arr2=np.ones((3,3))
# arr1=np.ones(3)
# arr3=np.ones((3,3,3))


# def function(arr):
#   print(f"Dimension :{arr.ndim}")
#   print(f"Shape :{arr.shape}")
#   print(f"Size :{arr.size}")


# print(f" for 1-d array")
# function(arr1)
# print()
# print(f" for 2-d array ")
# function(arr2)
# print()
# print(f"for 3-d array")
# function(arr3)

# print(np.array_equal(arr1,arr2))

# arr=np.ones((3,4))

# arr_s=arr[2:,:]
# print(arr_s.shape)
# arr_s[0][0]=3
# print(arr)

# arr=np.array([1,2,3,4],dtype='S')
# print(arr)

# print(arr.dtype)

# arr=np.arange(1,5)

# newarr=arr.astype(int)
# print(newarr)


# x=np.ones(4)

# y=x+1
# print(y)
# print(x-y)
# print(x==y)
# print(x*y)
# print(x**y)
# print(x/y)

# cost=np.array([20,15,25])
# sales=np.array([[2,3,1],[6,3,3],[5,3,5]])

# total=np.zeros((3,3))

# for col in range(sales.shape[1]):
#     total[:,col]=sales[:,col]*cost
    
# print(total)

# cost=np.array(cost).reshape(3,1)

# #cost=np.repeat(cost).reshape(3,1)
# print(cost*sales)

# a=np.ones((3,2))
# b=np.ones((3,2,1))

# try:
#     print(f"The shape of a+b is: {(a+b).shape}")
# except:
#     print(f" ERROR : arr not broadcast compible")

x=np.full((4,3),3.14)
print(x.reshape(6,2))

print(x.reshape(2,-1))

arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
x[0]=9
y[1]=8

print(arr)