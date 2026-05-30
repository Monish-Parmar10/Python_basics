'''tuples'''

# ur_tuples =(1,100,1000)
# ur_tuples += (10000,100000)
# print(ur_tuples)

# tup_1 =(1,2,3)
# for elem in tup_1:
#     print(elem)
# tup_2 =(1,2,3,4)
# print(5 in tup_1)
# print(5 not in tup_2)

# tup_3 =(1,2,3,4)
# print(len(tup_3))
# print(5 not in tup_3)

# tup_4 =tup_1 + tup_2
# tup_5 = tup_3 * 2
# tup_6 = tup_3[2:]

# print(tup_4)
# print(tup_5)
# print(tup_6)


# '''string inside tuple'''
# ur_tuple = tuple((1,2,"string"))
# print(ur_tuple)
# print(type(ur_tuple))

# ur_list = [2,4,6]
# print(ur_list)
# print(type(ur_list))
# '''list -> tuple'''
# tup = tuple(ur_list)
# print(tup)
# print(type(tup))


# var = 123
# t1 = (1,) # ',' it use to denote it is a tuple
# t2 = (2,)
# t3 = (3,var)
 
# t1,t2,t3 = t2 ,t3,t1
# print(t1,t2,t3)
# print(type(t1),type(t2),type(t3))



# '''Dictionary'''

dictionary={
# key and value

"cat": "chat",
"dog": "chien",
"hourse": "cheval"
}

# phone_number ={
# 'boss' : 8888888888 ,
# 'suzy':22222222
#}
# empty_dictionary ={}

# print(dictionary)
# print(type(dictionary))
# print(phone_number)
# print(type(phone_number))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary["cat"])


# words = ['car','lion','hourse']
# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print("------",word,"is not in the dictionary","----")
#     for key in dictionary.keys(): ####
#         print(key,"->",dictionary[key])    
    
# for key, value in dictionary.items():
#     print(key,"->",value)
# for value in dictionary.items():
#     print(value)
# #------------------------------------------------

'''copy dict'''
# pol_eng_dictionary ={
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
# }
# print("pol_eng_dictionary:",pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_dictionary",copy_dictionary)

'''update_value(val of the key)'''

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)


'''crud operation inside the dict // POPitem // del //update'''
# phonebook ={} #an empty dict
# print(phonebook)
# phonebook["Adam"] = 598393849  # create/add a key-value pair #[] use for index or list etc
# print(phonebook) #O/p {"Adam": ............}
# print(type("adam"))

# del phonebook["Adam"]
# print(phonebook)

# pol_eng_dictionary = {"kwiat":"flower"}

# pol_eng_dictionary.update({
#     "globa":"soil"
# })
# print(pol_eng_dictionary)
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)