# list =[]
# for i in range(1,21):
#     list.append(i)
# print([list])

# list =[3,4,5,6,8,9]
# total= 0
# for sumation in list:
#     total = total + sumation
# print(total)


# list =[]
# for even in range(1,21):
#     if even%2==0:
#       list.append(even)
# print(list)

# list =[]
# for num in range(1,15):
#     if num%2 !=0:
#      list.append(num)
# print(list)

# list =[1,2,3,4,5,6,7]
# for element in list:
#     print(element)

# list = [1,2,3,4,5,6,7,8]
# num =0
# for sum in list:
#     num = num +sum
# print(num)


    
    
# list = [1,2,3,4,5,6,7,8]
# count = 0
# for element in list:
#   count += 1
# print(count)

# list = [1,2,3,4,5]

# for element in range(len(list)):
#     list[element] += 5
# print(list)

# list = [1,2,3,4,5]
# for num in range(len(list)):
#     list[num] *=  2  
# print(list)


# list = [1,2,3,4,5]
# for num in range(len(list)):
#     list[num] *=  -1  
# print(list)



# list = [1,2,3,4,5]
# for num in range(len(list)):
#     list[num] **=2
# print(list)

'''largest number without max'''


# list =[1,2,3,4,5,6,7,8]
# largest_num =  list[0]
# for itration in list:
#     if itration > largest_num:
#         largest_num = itration
# print(largest_num)





'''word counter / freq counting problem'''
# freq={}
# words = ["apple","banana","apple","orange","banana","apple"]
# for word in words:   #**
#     if word in freq:#**  
#      freq[word] +=1  #**
#     else:
#        freq[word] =1
# print(freq)

'''or'''


# words ={}
# sentance = "apple banana orange banana apple mango"
# sentance = sentance.split()
# for fruits in sentance:
#     if fruits in words:
#         words[fruits] += 1
#     else:
#         words[fruits] = 1
# print(words)


'''only take 3 letter frin the list and append into another then pop'''
# teams =["RCB","GT","SRH","RR"]
# stach = []
# monish = [1,2,3]
# for t in teams:
#     if len(t) == 3:
#      stach.append(t)
# print(stach.pop()) #pop element


'''append/inset list'''
# list1 = [1,2,3,4]
# list2=[]
# for num in list1:
#     list2.insert(0,num)
# print(list2)

