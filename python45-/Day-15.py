'''method self paremeters'''


# class classy:
#     def method(self,parameter):
#             print("method",parameter)

# obj = classy()
# obj.method(1)
# obj.method(2)

# class classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)


# obj = classy()

# obj.var = 3
# obj.method()




# class star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = star("sun","milky Way")
# print(sun)



# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' in ' + self.galaxy



# sun = Star("sun","milky Way")
# print(sun)



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

class Level1:
    varible_1 = 100
    def __init__(self):  #constructor
        self.var_1 = 101
    def fun_1(self):
        return 102
class Level2(Level1): #lev 2 inherit
    varible_2 = 200
    def __init__(self):#constructor
        super().__init__() 
        self.var_2 = 201
    def fun_2(self):
        return 202
class Level3(Level2):
    varible_3 = 400
    def __init__(self): #constructor
        super().__init__()
        self.var_3 = 403
    def fun_3(self):
        return 404
    
obj = Level3()
print(obj.varible_1,obj.var_1,obj.fun_1())
print(obj.varible_2,obj.var_2,obj.fun_2())
print(obj.varible_3,obj.var_3,obj.fun_3())
