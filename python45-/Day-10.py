'''functions  1st built in function 2nd pre- define modules  3nd user defie function 3rd'''

# def message(): #it was written here but it will execute where we call it  

#     print("enter your val:")

# message()
# a = int(input())

# message()
# b= int(input())

# message()
# c = int(input())



# def message():
#  list =[1,2,3,4,5]
#  print("list->",list)

# # message = 1
# message()
# print("here we go")
# print(message)

# print("we are here")
# message()



'''function return'''

# def message():
#     print("enter a val")
#     temp = int(input())
#     return temp # if not using return then it will print none value because it return nothing 
# '''go check naming convention'''
# print("S1")
# a = message()

# print("S2")
# b = message()

# print("S3")
# c= message()

    
# print("a",a)
# print("b",b)
# print("c",c)

'''wrong '''
# def hi():
#     print("hii")
# hi(5)

'''parameterized function'''
# def noob(n): #def a function
#     print("hello",n) # body of the function

# name = input("enter your name") #
# noob(name) # calling the function

# def noob(number):
#     print("enter a num",number)

# number = 1234
# noob(1)
# print(number)

'''parameter shadowing'''

# def message(what , number):
#     print("enter",what,"enter_num",number)

# message("telephone",11)
# message(11,"telephone")
# message("price",5)
# message("number","number")

# def introduction(first_name,last_name):
#     print("my first name is",first_name,last_name)
    
# introduction("luke","skywalker")
# introduction("jesse","quick")
# introduction("clark","kent")
# '''keyword argument'''
# introduction(first_name= "james",last_name="bond")
# introduction(first_name= "herry",last_name="elon")




'''sum'''

# def sum(a,b,c):
#     print(a,"+",b,"+",c,"=",a+b+c)

# sum(1,2,3)
# sum(c = 1,a=2,b=3)
# sum(3,c=1,b=2)
# sum(3,a=3,b=2)



# '''T / F'''
# def happy_new_year(wishes = True):
#     print("three")
#     print("two")
#     print("one")
#     if not wishes:
#         return
#     print("happy new year")

# happy_new_year(True)


'''rtn not wrk'''
# def boring_function():
#     print("'BOREDOM MODE' ON ")
# print("the lesson is interesting")
# boring_function()
# print("the lesson is boring")



'''none''' #explisit forcefully did 

# def checkMyvar(variable):
#     if variable == 10:
#         print("variable is 10")
#         return 10
#     else:
#         print("varible is not that expected")
# print(checkMyvar(5)) 

'''function list'''
# def list_sum(lst):
#     s=0
#     for element in lst:
#         s = s+element
#     return s
# print(list_sum(3))


def  doc_Strange(n):
    doc_lst =[]
    
    for i in range(0,n):
        #  doc_lst.insert(0,i+1)
        doc_lst.append(i+1)

    return doc_lst
print(doc_Strange(5))




# camel and snamecage