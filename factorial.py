def factorial(k):
    if k==0 or k==1:
        return 1
    else:
        return k*factorial(k-1)

print(factorial(4))