'''module 3 lists shorting'''

# list = [8,10,6,2,4]
# var1 = list[0]


# for var1 in range(list):
#   if var1>list:
#    var1,var1>list = var1>list,var1
#   else:
    
'''bubble short'''
# list =   [5,4,3,1,2] #[1,2,3,4,5]   #[8,10,6,2,4] 
# swapped = True #use to control while /  we need it to ener the while loop 
# count = 0
# index =0
# while swapped:
#      swapped = False # no swap so far
#      for i in range(len(list) - 1-index):
#         index = i
#         count +=1
#         if list[i] > list[i + 1]:
#          swapped = True
#          list[i],list[i+1] = list[i+1],list[i]
# print(list)  
# # print(count) 



# list =[33,9,8,6,7,8]
# count = 0
# list.sort()
# count +=1
# print(list)
# print(count)

'''reverse'''
# a = 'A'
# b = 'B'
# c = 'C'
# d = ''

# lst = [a,b,c,d]
# lst.reverse()
# print(lst)



# my_list = [1,2,3,4,5]
# my_list.sort()
# print(my_list)



# my_list.reverse()
# print(my_list)

# val = ord('A')
# print(val)



'''slice'''

#slice use to make brand new copy of the list or parts of a list
# list1 =[1]
# list2 = list1[:] # with [:] is make share the elemtn not the memory this time
# list1[0] = 2
# print(list1)
# print(list2)


# list = [10,8,6,3]
# new_list = list[1:3]
# print(list)
# print(new_list)




# list = [10,8,6,3,2]
# new_list = list[1:-1]
# print(list)
# print(new_list)



# list = [10,8,6,3,4]
# new_list = list[-5:3]
# print(new_list)




# list = [10,8,6,3]
# new_list = list[1:]
# print(list)
# print(new_list)



# list = [10,8,6,3]
# del list[1:2]
# print(list)




# list = [10,8,6,3]
# del list[0:]
# print(list)




# list =[0,3,1,5,6]
# print( 5 in list)
# print(3 not in list)
# print(12 in list)


'''write a program to print largest element in the list'''

# lst = [17,3,11,5,1,9,7,15,13]
# largest_num =0
# for i in range(len(lst)-1):
#      if lst[i] > largest_num:
#       largest_num = lst[i]
#       print(lst[i])
# print(largest_num)

'''finding the existing element from the list'''
# lst = [17,3,11,5,1,9,7,15,13]
# num = 5
# for i in range(len(lst)):
#     if lst[i] == num:
#      print("element index is:",i)
    

'''program to find how many num u hit'''
# choosen_lst = [3,7,11,42,34,49]
# drawn_lst =[5,11,9,42,3,49]
# hitlist = 0
# for number in choosen_lst:
#        if number in drawn_lst:
#         hitlist += 1
# print(hitlist)

'''write a program to remove duplicate number '''

# repeat_lst = [1,2,4,4,1,4,2,6,2,9]
# nw_lst = []

# for number in repeat_lst:
#     print(number)


# repeat_lst = [1,2,4,4,1,4,2,6,2,9]
# nw_lst = []

# for number in repeat_lst:
#     if number not in nw_lst:
#      nw_lst.append(number)
#      print(number)
# print(nw_lst)


# list_1 = ["A", "B", "C"]
# list_2 = list_1[:] #slice create copy not pointing at one
# list_3 = list_2 [:]
# del list_1[0]
# del list_2[0]
# print(list_3)


