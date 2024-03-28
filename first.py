# # # '''a=int(input("enter value :"))
# # # if a==2:
# # #     print("result is true")
# # # elif a>2:
# # #      print(result is greater)
# # # elif a==0:
# # #     pass
# # # else:
# # #     print("result is false")
# # # b="hello"
# # # print(b)
# # # c=str(3)
# # # print(c)
# # # d=int(5.0)
# # # print(d)
# # # e=float(3)
# # # print(e)

# # # print(type(a))
# # # x,y,z="orange",2,3.0
# # # print(x)
# # # print(y)
# # # print(z)

# # # x=y=z=3
# # # print(x)
# # # print(y)
# # # print(z)

# # # x="aweosome"

# # # def myfunc():
# # #     global y
# # #     y="hi"
# # #     print("python is "+ x)
    
# # # myfunc()
# # # print(y)

# # # a=10
# # # print("hello "+str(10))

# # # import random
# # # print(random.randrange(4,9))

# # # for x in "banana":
# # #     print(x)
# # # print(len("hello"))

# # # print("h" in "hello")
# # # print("h" not in "hello")

# # # b="hello ,world!"
# # # print(b[2:7])

# # # print(b[-5:-2])
# # # print(b.upper())
# # # print(b.lower())
# # # print(b.strip())
# # # print(b.replace("h","j"))

# # # print(b.split(" ,"))

# # # age=72

# # # txt="my name is "

# # # print(txt.format(age))
# # # txt2="heloo \"everyone\""
# # # print(txt2)
# # # i=0
# # # while i<6:
# # #      i+=1
# # #      if i==3:
# # #        continue
# # #      print(i)
     
# # # num=[1,2,3]
# # # for i in num:
# # #     print(i)
    
# # # for i in range(2,6,2):
# # #     print(i)
# # #     if i==2:
# # #         break
# # # else:
# # #     print("final")

# # # print("first")   
# # # for i in range(4):
# # #     for j in range(i+1):
# # #         pass
# # #     print(j*"*")
    
# # # print("second")
# # # print()
# # # for i in range(4,0,-1):
# # #     for j in range(i+1):
# # #         pass
# # #     print(j*"*")'''
    
# # # mylist=["apple","banana","cherry"]
# # # # print(type(mylist))
# # # # thislist=list(("apple","banana"))
# # # # print(thislist)
# # # # print(mylist[1:3])
# # # # if "apple" in mylist:
# # # #     print("yes")
# # # # mylist[1]="mango"
# # # # mylist[2:3]=["kivi","guvava"]
# # # # print(mylist)
# # # # mylist.insert(2,"watermelon")
# # # # print(mylist)
# # # # mylist.append("pineapple")
# # # # mylist.extend(thislist)
# # # # print(mylist)
# # # # mylist.remove("apple")
# # # # print(mylist)
# # # # mylist.pop(6)
# # # # del mylist[1]
# # # # print(mylist)
# # # # #del thislist
# # # # thislist.clear()
# # # # print(thislist)

# # # # for x in mylist:
# # # #     print(x)
# # # # for i in range(len(mylist)):
# # # #     print(mylist[i])
# # # #i=0
# # # # while i<len(mylist):
# # # #     print(mylist[i])
# # # #     i=i+1

# # # # new=[]
# # # # for x in mylist:
# # # #     if "a" in x:
# # # #         new.append(x)
# # # # print(new)

# # # # new2=[x for x in mylist if "a" in x]
# # # # print(new2)

# # # # newlist=[x for x in range(10) if x<5]
# # # # print(newlist)

# # # # list1=["a","b","c"]
# # # # newl1=[x.upper() for x in list1 ]
# # # # print(newl1)

# # # # newl2=["hello" for x in list1]
# # # # print(newl2)

# # # # newl3=[x if x!="banana" else "orange" for x in mylist]
# # # # print(newl3)

# # # # mylist.sort()
# # # # print(mylist)
# # # # mylist.sort(reverse=True)
# # # # print(mylist)

# # # # this=[100,60,70,45,34]
# # # # def myfunc(n):
# # # #     return abs(n-50)
# # # # this.sort(key=myfunc())
# # # # print(this)

# # # # this2=this.copy()
# # # # this2=list(this)

# # # mytuple=("apple","mango","orange")
# # # this=("apple")
# # # print(type(this))#string
# # # this=("apple",)
# # # print(type(this))#tuple

# # # thistup=tuple(("cherry",))
# # # print(type(thistup))

# # # y=list(mytuple)
# # # y[1]="kiwi"
# # # y.append("banana")
# # # #y.remove("apple")
# # # mytuple=tuple(y)

# # # mytuple+=thistup
# # # #del mytuple
# # # print(mytuple)

# # tup=(1,2,3,4,5)
# # # # (a,b,c)=tup
# # # # print(a)
# # # # print(b)
# # # # print(c)
# # # (a,*b,c)=tup
# # # print(a)
# # # print(b)
# # # print(c)
# # tup=tup*2
# # i=0
# # while i < len(tup):
# #     print(tup[i])
# #     i=i+1
# set1={1,2,3}
# # thisset.add(4)
# set2={0,5,6,7,3}
# # thisset.update(thisset2)
# # mylist=["hello"]
# # thisset.update(mylist)

# # thisset.remove(1)
# # #thisset.remove(5) 
# # thisset.discard(1)
# # print(thisset)

# # # thisset.clear()
# # del thisset
# # print(thisset)
# # set3=set1.union(set2)
# # set2.intersection_update(set1)
# # print(set2)
# # set3=set1.intersection(set2)
# # print(set3)

# # set2.symmetric_difference_update(set1)
# # print(set2)
# # set3=set1.symmetric_difference(set2)
# # print(set3)

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # print(thisdict)

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964,
# #   "year": 2020
# # }
# # print(thisdict)

# # thisdict = dict(name = "John", age = 36, country = "Norway")
# # print(thisdict)

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # x = thisdict["model"]




# # def my_fun(*kids):
# #     print(kids[2])


# # my_fun(2,"hello",4)

# # def my_fun2(**kid):
# #     print(kid["lname"])
    
# # my_fun2(fname="hi",lname="hello")

# # def minus(a,b):
# #     return b-a

# # result1=minus(a=5,b=6)
# # print(result1)
# # result2=minus(b=6,a=5)
# # print(result2)

# # def my_function(x,/):      #positional only
# #   print(x)

# # my_function(3)

# # def my_function(*, x):     #keyword only
# #   print(x)

# # my_function(x = 3)

# # def my_fun3(a,b,/,*,c,d):
# #     print(a+b+c+d)

# # my_fun3(5,6,c=9,d=7)

# # def my_function(food):     #pass list
# #   for x in food:
# #     print(x)

# # fruits = ["apple", "banana", "cherry"]

# # my_function(fruits)

# # def f(x):  #
# #      x+1
# #      if x==99:
# #          return x

# # print(f(0))
# # print(f(99))

# # def sum_prod(x,y):
# #     return(x+y,x*y)

# # print(sum_prod(5,6))
# # s,p=sum_prod(5,6)
# # print(s,p)

# # def square(x):
# #    '''hello world'''
# #    return(x**2)

# # square(9)
# # print(square.__doc__)

# # a=input("enter name : ")
# # print("your name is : "+a)

# # a=int(input("enter first value : "))
# # b=int(input("enter second value : "))
# # print(a+b)

square =lambda x: x**2


def evaluate(fun,x):
    return fun(x+1)

print(evaluate(square,5))