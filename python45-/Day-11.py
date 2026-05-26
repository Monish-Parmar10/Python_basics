# def list_update(lst):
#     upd_list =[]
#     for element in lst:
#         element **=2
#         upd_lis


# def scope_test():
#     print("where is the var",x)

# x = 123
# scope_test()
# print(x)

#var shadowing

# def mult(x):
#     var = 7
#     return x * var

# var = 3
# print(mult(7))
'''global '''
# def globe():
#     global var
#     var = 2
#     print("here is my var",var)

# globe()
# var = 1
# print(var)

# var = 2
# print(var)




# def rtn_var():
#     global var
#     var = 5
#     return var
# # print(rtn_var())
# print(var)



'''here the function which got the argument will be change not the original var'''
# def my_fn(n):
#     print("i got ",n)
#     n +=1
#     print("i want",n)

# var = 1
# my_fn(var) 
# print(var) # O/P 1



# def my_function(my_lst1):
#     print("print 1",my_lst1)
#     print("print 2",my_lst2)
#     my_lst1.append(10)
#     print("print 3:",my_lst1)
#     print("print 3:",my_lst2)
    
# my_lst2 = [2,3]
# my_function(my_lst2)
# print(my_lst2)


# def my_function(my_lst1):
#     print("print 1",my_lst1)
#     print("print 2",my_lst2)
#     del my_lst1[0] #del mutation 
#     print("print 3:",my_lst1)
#     print("print 3:",my_lst2)
    
# my_lst2 = [2,3]
# my_function(my_lst2)
# print("print 5",my_lst2)



'''function arrgument 5'''
# def countDown(num):
#     print(num)
#     if num ==0:
#      return num 
#     else:
#         countDown(num -1)

# countDown(5)
# print(countDown(5))


# def countDown(num):
#     print(num)
#     if num ==0:
#      return num 
#     else:
#         print("go in rec:",num)
#         countDown(num -1)
#         print("out of rec:",num)
# print("startting")
# countDown(5)
# print(countDown(5))
# print("end")


# '''check'''
# def countDown(num):
#     print(num)
#     if num ==0:
#      return 
#     else:
#         countDown(num)

# countDown(5)

# def factorial(num):
#     print(num)
#     factorial num -1

# factorial(5) 


# '''correct'''
# def fact(num):
#     print(num)
#     if num <=0:
#      return 1
#     else:
#         return num * fact(num-1) 
             

# print(fact(5))
'''touples '''

my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

print(len(t1))
