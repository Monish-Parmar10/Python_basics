'''Dictionary / using member ship operator'''


# Pol_eng_dictionary = {
#     "zamek" : "castle",
#      "woda" :  "water",
#     "glena": "soil"

#  }
# if "zamek1" in Pol_eng_dictionary:
#     print("yes! zamek1 is present in the dictionary")
# else:
#     print("No ! zamek1 is not present in the dictionary")

# print(Pol_eng_dictionary)
# print(len(Pol_eng_dictionary))
# '''del dictionary'''
# del Pol_eng_dictionary["zamek"]
# print(Pol_eng_dictionary)
# print(len(Pol_eng_dictionary))

# '''clear dictionary'''

# Pol_eng_dictionary.clear()
# print(Pol_eng_dictionary)
# print(len(Pol_eng_dictionary))





'''ques***''' #have a look #write in copy do dry run then shift tocode
# sch ={} #empty dictionary
# while True:
#     name = input("enter ur name:")
#     if name =="":
#         break
#     score = int(input(f"enter ${name}'s score"))
#     if score not in range(1,11):
#         break
#     if name in sch:
#         sch[name] += (score,)
#     else:
#         sch[name] = (score,)

# #for mark in sch
# print(sch)

# for name,mark in sch.items():
#     sum = 0
#     for m in mark: # for iteration
#         sum+=m
#     print(name,"->",sum/len(mark))
# print(type(score))
# print(type(name))




# std={
#     "Monish" : 85,
#     "rahul" : 70,
#     "aditi" : 92
# }

# for stdd in  std.keys():
#     print(stdd)
# print("marks of rahul:",std.get("rahul"))
# std["karan"] = 88
# print(std)
# std.update({"Monish": 95})
# print(std)

# if "aditi" not in std:
#   print(" no aditi is there")
# else: 
#    print("yes aditi in the list")
# print("total lenght of std:",len(std))

# del std["rahul"]
# print(std)



'''word counter / freq counting problem'''
# freq={}
# words = ["apple","banana","apple","orange","banana","apple"]
# for word in words:   #**
#     if word in freq:#**  USE TO SOLVE THE COUNT -> CHAR,VOTES WORDS,MARKS PRODUCT SOLD USING DICTIONARY
#      freq[word] +=1  #**
#     else:
#        freq[word] =1
# print(freq)


'''only take 3 letter frq in the list and append into another then pop'''
# teams =["RCB","GT","SRH","RR"]
# stach = []
# monish = [1,2,3]
# for t in teams:
#     if len(t) == 3:
#      stach.append(t)
# print(stach.pop()) #pop element
'''append/insert list'''
# list1 = [1,2,3,4]
# list2=[]
# for num in list1:
#     list2.insert(0,num)
# print(list2)

'''repeated'''

# name = "banana"  
# if len(name) == len(set(name)):
#  print("has no reap char")
# else:
#  print("string has repeated chat")

name = "noooob"

for i in range(len(name)-1):
    if name[i] == name[i +1] == name[i+2]:
     print("char is repeating")
else:
     print("this name is not repeating good",name)