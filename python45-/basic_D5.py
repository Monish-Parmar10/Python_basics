'''logical expression'''
# var = 20
# print(var > 0)
# print( not (var <= 0))
# print(var != 0)
# print(not(var == 0))

'''List M3 '''
# number = [10,9,8,7,6]
# print(number)
# print(type(number))

'''INDEX logic '''
#number[0] => number address + ((number of bytes occupied * index)) => 0x0000 =10
#number[1] => number address + ((number of bytes occupied * index)) => 0x0002 =5
#number[2] => number address + ((number of bytes occupied * index)) => 0x0004 =7

# number = [10,9,8,7,6]
# print("first element of conntent:",number[0])
# print("second element of conntent:",number[1])
# print("third element of conntent:",number[2])
# print("fourth element of conntent:",number[3])
# print("fifth element of conntent:",number[4])


# list = [2,3,4,5,5]
# print("val ofindex[0]",list[1])
# print(list)
# print(list.index(3))




'''update list'''
# number[0] =123
# print("number[0]:",number[0])
# print(number)

# number[1] = 404
# print("number[1]:",number[1])
# print(number)

# number = [10,9,8,7,6]
# print(number[-1])
# print(number[-2])
# print(number[-3])

# print(number[-8]) # index out of bound

# number = [1,2,3,4,5]
# print(len(number))
# del number[-1]
# print(number)

''' check this'''

# list = [1,2,3,4,5]
# n1 = int(input("enter ur number to replace it with mid value of list"))
# list[len(list)//2] = n1
# print(list)


'''correct one'''

# number[len(number)//2] = int(input("enter number to replace it with middle number"))
# print(number)

'''function/method ''' 

'''insert / append'''
# list = []
# print(list)
# list.append(10)
# print(list)

# list.insert(1,404)
# print(list)


# list.insert(0,404)
# print(list)

# list.insert(2,444)
# print(list)

# x = list.index(444)
# print(x)