'''overview'''
# # x= 5
# x=20.0
# # x="naman"
# x = ['three','four','five'] list
# x= ("div","body","header") touple
# x= 1j complex
# x= range(6)
# x= {"name":"monish","age":36}
# x= {"apple","banana","cherry"}
# x=frozenset({"apple","banana","cherry"})
# bytes = b"hello"
# x = memoryview(bytes(5))

''' Arithmetic operrator + - * / // '''

# x = 10
# print(bin(5))
# print(5<<1)

'''x = 1 print(x:=3) assin value '''

# print(x ==1)
# print(x==2)

# print(x != 1)
# print(x !=2)

# print(x >y & x<y)
# print(x >y or x<y)
# print(not(x >y or x<y)) #reverrt 
# x= 3
# y=3
# print(x is y) 
# print(x is not  y)



# x =["maruti","BMW"]
# y =["maruti","BMW"]  #same DT but primary data type that's why address diffrent as compare to x 
# z=x

# print(x is y)
# print(x is z)
# print(x is not y)



# member ship operator or identity membership

''' in     /     not in'''

# y = ["maruti"]
# x = "maruti"
# print(x in y)

'''bitwise  normal multiplication'''
# or ... & ... XOR ... ^ .... left and right shif....

 

''' input/output'''

# name = input("enter ur name")
# print("hlo I'm",name)

# print("enter ur age to check ur old or not")

# age = input("enter your age")
# if(age>39):
#     print("ur age is :",age,"you are old")
# else:
#     print("u ar not that mmuch old")



x = input("enter a value1 or sum:")
y = input("enter value2 for sum:")
z = int(x) + int(y)   # type casting   (try without type casting or without defining datatype then )
#concat
z = x+y
print("sum:",z)
print(x+y)
print(type(z))


x = int(input("enter val 1:"))
y = int(input("enter val 2:"))

print(x+y)