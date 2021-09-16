from itertools import permutations
 
def foo(list):
    perms = [''.join(p) for p in permutations(list)]    
    return perms
 
a = ['a','b','c']
list = foo(a)
for combination in list:
    print(combination)
