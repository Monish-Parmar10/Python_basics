'''1st'''
# name = input("enter ur name:")
# age = int(input("enter ur age:"))
# course = input("enter ur course name:")

# print("your name :",name,"\nYour age:",age,"\nyour course name:",course)


'''2nd'''
#  for i in range(3):
#   i += 1
#   name = input("enter the name of  stdudents:")
#   age = int(input("enter the age of  students:"))
#   course = input("enter the course of three students:")


#  print("\n name :",name)
#  print("\n age :",age)
#  print("\n course :",course)

# for i in range(3):

#   name = input("enter the name of  stdudents:")
#   age = int(input("enter the age of  students:"))
#   course = input("enter the course of three students:")

#   if i == 0:
#    name1 = name
#    age1 =age
#    course1 = course
#   elif i == 1:
#    name2 = name
#    age2 = age
#    course2 = course
#   else:
#    name3 = name
#    age3 = age
#    course3 = course

# print("\nname1:",name1)
# print("\nage1:",age1)
# print("\ncourse1:",course1)

# print("\nname2:",name2)
# print("\nage2:",age2)
# print("\ncourse2:",course2)

# print("\nname3:",name3)
# print("\nage3:",age3)
# print("\ncourse3:",course3)
''' 3rd'''

# a = 3
# b= 4
# print(a+b)

'''4th'''

# a = 3.4
# b = 4.46

# print(a*b)

'''5th'''

'''7th'''
# a =7
# b =6
# print(a-b)

'''8th'''
#  a =7
#  b =6
#  print(a*b)

'''9th'''
# a =7
# b =6
# print(a/b)
'''10th'''
# a =4
# b =3
# print(a//b)
'''11th'''
# a =4
# b =3
# print(a%b)

'''12th'''
# a =4
# b =3
# print(a**b)

# print((("*")*5+"\n")*5)

# print((("#")*8+"\n")*6)

# print("#"*6)
# print(("#"+" "*4+"#\n")*4, end="") # end="" use to concatinate the end text  
# print("#"*6)

# for i in range(1,6):
#      for j in range(1,i+1):
        
#         print(j,end="")

#      print()


# print(" "*8+"*")
# print(" "*7+"*"+" "*2+"*")
# print(" "*6+"*"+" "*4+"*")
# print(" "*5+"*"+" "*6+"*")
# print(" "*4+"*"*3+" "*4+"*"*3)
# print(" "*6+"*"+" "*4+"*")
# print(" "*6+"*"+" "*4+"*")
# print(" "*6+"*"*5+"*")

# for i in range(1,10):
#      for j in range()

# for i in range(6):
#     print(str(i)*i)


# 1,2 ,fiz, 4 , fiz,buzz, 7,8,fiz , 10 , 11 ,fiz, 13, 14, buzz, 




'''series print question '''

# for series in range(1,51):
#     print(series)


# for i in range(1,51):
#  if i%2!=0: 
#     print("t",end="")
#  else:
#     print(i, end="")


# for i in range(1,50):
#  if i%2==0:
#    print("d",end="")
#  else:
#    print(i,end="")
    
# for i in range(1,51):
#    if i%5==0 and i%3==0:
#      print("FIZBUZZ")
#    elif i%5==0:
#      print("fiz")
#    elif i%3==0:
#      print("Buzz")
#    else:
#      print(i)

'''income and tax'''
# sly = float(input("enter your income"))
# total = 0
# if sly <= 85528:
#     total=(sly*0.18)-556.02
#     if total <0:
#         total = 0

# else:
#     total = 14839.02 + (sly - 85528)*0.32   #paying text on wt remain after subtacting current salery from 85528
# print(round(total))

''' leap year'''
# year =int(input("enter year to check:"))

# if year < 1582:
#     print("year is Not within the Gregorian calendar period.")
# elif year%4 != 0:
#     print("your entered year :",year,"its is a common year")
# elif year%100 != 0:
#     print("your entered year :",year,"its is a leap year")
# elif year%400 !=0:
#     print("your entered year :",year,"is is a common year")
# else:
#     print("it is a leap year")


'''mississipi'''
# import time
# for i in range(1,6):
#  print("mississippi",i)
#  time.sleep(2)
# print("ready or not here, i come!")
 
#or
 
# number = ["one","two","three","five"]

# for i in number:
#   print("mississippi",i)

'''vowels'''

# name = input("enter a name so i eat ugly vowel from it:")
# name = name.upper()
# no_vowel =""
# for i in name:
#     if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#      continue
#     no_vowel = no_vowel + i
# print(no_vowel)
 

'''box'''

# block = 6
# height = 0
# layer = 1
# while block >= layer:
#     block = block - layer
#     height = height + 1
#     layer = layer + 1
# print("height :",height)
# print("num of block left :",block)


'''Collatz '''

# c0 = int(input("enter a non-negative non zero int num"))

# while c0 !=1:
#  if c0%2 == 0:
#     print("c0 is even number")
#     c0 = c0/2
#     print("val of c0:",c0)
#  elif c0%2 != 0:
#     print("c0 is odd number:")
#     c0 = 3*c0+1;
#     print("val of c0:",c0) 
 
'''list update remove '''
# hat_lst =[1,2,3,4,6,5]
# num = int(input("enter num to replce it with mid val of list:-"))  

# print(len(hat_lst))

# hat_lst.remove(5)
# print("after removing the element ",hat_lst)

# for i in range(len(hat_lst)):
#     hat_lst[len(hat_lst)//2] = num
# print("after replacing the mid element ",hat_lst)


'''wow'''

# beatles = []
# beatles.append(["john lennon","paul McCartney","George Harrison"])
# print(beatles)
# Members = list(input("enter name of member in the list"))
# for i in range(len(Members)):
#  beatles.append([Members])
# print(beatles)

'''append insert del list'''

# beatles = []
# beatles.append(["john lennon","paul McCartney","George Harrison"])
# print(beatles)
# for i in range(2):
#  Members = input("enter name of member in the list")
#  beatles.append(Members)
# print(beatles)
# del beatles[1:]
# print(beatles)
# beatles.insert(0," Ringo Starr")
# print(beatles)


'''fiz /buzz'''
# for num in range(1,51):
#     if num%5==0 and num%3 ==0:
#        print("FixBuzz")
#     elif num%5==0:
#       print("Buzz")
#     elif num%3==0:
#        print("Fizz")
#     else:
#        print(num) 

# strg= "MindCoders password2 is : 1234"
# count =0
# for ch in strg:
#      if ch.isdigit():
#           count +=1
# print(count)   

# strg= "U r a a n S 0 f t s k i l l 1 s 1234"
# count =0
# for ch in strg:
#      if ch.isdigit():
#           count +=1
# print(count)   




