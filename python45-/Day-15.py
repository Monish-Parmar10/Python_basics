'''method self paremeters   /***'''


# class classy:
#     def method(self,parameter): #self point to the obj whenever the method is called
#             print("method",parameter)
            
# obj = classy() #obj stores the object's reference
# obj.method(1)#and when method is call it temporarily refers to the that obj
# obj.method(2)#ex -> classy.method(obj,1)

# class classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)


# obj = classy()

# obj.var = 3  # in this 1st goes on object check is there varia = 2 in the object nope then goes on classy check there true
#             #take it , if it get the req thing direct in the obj or obj instace attribute it will top there
# obj.method()




# class star:
#     def __init__(self,name,galaxy): #tempobject = new star object
#         self.name = name #like to be star __init__(temp_object,"sun","milky way")
#         self.galaxy = galaxy
        

# sun = star("sun","milky Way") #star = tempobject
# print(sun)



class Star:
    def __init__(self,name,galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy  
# or
    # def show(self):
    #     return self.name +" in "+ self.galaxy

sun = Star("sun","milky Way")
print(sun)
# print(sun.show())

'''***'''
# class vehicle:
#     pass
# class landvechile(vehicle):
#     pass
# class trackedvechile(landvechile):
#     pass
# for cls1 in [vehicle , landvechile , trackedvechile]:
#     for cls2 in [vehicle, landvechile,trackedvechile]:
#         print(issubclass(cls1,cls2) ,end="\t")
#     print()


# class super:
#     supvar = 1

# class sub(super):
#     subvar = 2

# obj = sub()
# print(obj.subvar)
# print(obj.subvar)


# class super:
#     def __init__(self):
#         self.supVar =11
# class sub(super):
#     def __init__(self):
#       super().__init__()
#       self.subVar =12

# obj = sub()
# print(obj.subVar)
# print(obj.supVar)



'''multi- level inheritence'''

# class Level1:
#     varible_1 = 100
#     def __init__(self):  #constructor(special method)
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
# class Level2(Level1): #lev 2 inherit
#     varible_2 = 200
#     def __init__(self):#constructor
#         super().__init__()  #calling parent class constructor
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
# class Level3(Level2):
#     varible_3 = 400
#     def __init__(self): #constructor
#         super().__init__()
#         self.var_3 = 403
#     def fun_3(self):
#         return 404
    
# obj = Level3()
# print(obj.varible_1,obj.var_1,obj.fun_1())
# print(obj.varible_2,obj.var_2,obj.fun_2())
# print(obj.varible_3,obj.var_3,obj.fun_3())

