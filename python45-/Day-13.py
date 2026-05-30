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



'''word counter'''
dict={}
words = ["apple","banana","apple","orange","banana","apple"]
values =0
count =0
dict = words.copy()
print(dict)
for word in dict:
    if dict.count(word)>1:
        count +=1
    else:
        count ==1
    print(word,count)