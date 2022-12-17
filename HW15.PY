from random import randint
a = [randint(0,10) for _ in range(10)]
print(a)
 
b = [randint(0,10) for _ in range(10)]
print(b)
 
print(len(set(a)-set(b)))
 
print(sorted(set(a)&set(b)))