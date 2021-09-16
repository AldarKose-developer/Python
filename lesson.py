# def foo(list):
#     new_list = []
#     end_list = []
#     for i in range (len(list)):
#         for j in range(len(list)):
#             if(i != j):
#                 new_list[i]=''.join(list)
                
# def foo(list):
#     index = -1  
#     for j in range(len(list)):
#         for i in range(len(list)):
#             if(i != index):
#                 print(list[i], end = '')
#         if index == -1:
#             print(" ")
#         else:
#             print(list[index] + ' ')
#         index += 1
        

# a = ['a','b','c']
# foo(a)

from itertools import permutations
 
def foo(list):
    perms = [''.join(p) for p in permutations(list)]    
    return perms
 
a = ['a','b','c']
list = foo(a)
for combination in list:
    print(combination)
