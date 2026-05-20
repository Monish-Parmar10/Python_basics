'''looooppp'''
'''infinite LP'''

# while True:
#     print("the loop is here")



# large_num = -8888888
# number = float(input("enter a number or type -1 to stop :-"))
# while number != -1:   #use break and continue here
#     if number > large_num:
#         large_num = number
       
#     number = float(input("enter a number pr type -1 to stop:"))
# print("the largest number is :-",large_num)


'''write a program to print number 0 to 50 in one line'''

# num = int(input("enter the initial number to start"))
# num = 0
# while num < 50:
#     num = num + 1
#     print(num,end="")   # end is use to stop the print default (\n) - means it stop going on next line


'''this program will first take user input to print number as per user input'''

number = int(input("enter the initial number to start"))
count = 1
while count <= number:
   print(count, end="")
   count += 1

       


# num = int(input("enter the number to print the sequence"))

# count = 1
# even = 0
# odd = 0

# while count<=num:
#     if  count % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     count += 1
# print("Even",even)
# print("Odd",odd)



# for i in range(100):
#     print("i:-",i)

# for i in range(2,8):
#     print("i:-",i)


# for i in range(2,8,3):  # 2,8,3 the 3 is here for the step it use to take jump of 3
#     print("i:-",i)

# p =1
# for expo in range(16):
#     print("2 to the power of" ,expo,"is",p)
#     p *=2

# print("here is the break in struction")

for count in range(1,6):
    if count == 3:
        continue
        #break
    print("inside the loop ", count)
print("outside the loop")