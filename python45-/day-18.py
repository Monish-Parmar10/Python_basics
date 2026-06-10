'''use super class and super method '''
class super:
    def __init__(self,name):
        self.name = name
    def __str__(self): #end user also use repr method but str is for internal use 
        return "my name is " +self.name+"."
class Sub(super):
    def __init__(self,name):
        super.__init__(self,name)

obj = Sub("Andy")
print(obj)
print(obj.__dict__)#also custamise the dict format #use for explaining 
    
'''multiple inheritance'''

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):
#     pass

# obj = Sub()

# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# '''multilevel inheritance'''
# # in python it checks from bottom-to-top
# class Level1: 
#     var = 100
#     def fun(self):
#         return 101
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
    
# class Level3(Level2):
#    pass
   
    # var = 303
    # def fun(self):
    #     return 333
    

# obj = Level3()
# print(obj.var,obj.fun())


#here about on same level left right
'''multiple inheritance'''

# class Left:
#     var = "L"
#     var_left="LL"
#     def fun(self):
#         return "left"
# class Right:
#     var= "R"
#     var_right="RR"
#     def fun(self):
#         return "right"
# class Sub(Right,Left): #(left,right)
#     pass

# obj = Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())

# MRO method resolution order precidence and order both in multilevel and multiple inheritance

'''polymorphism one name many forms'''

# class One: 
#     def do_it(self):
#         print("do it from one")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it  from Two")

# # class Three(Two):
# #       super.do_it(self):
# #       print():  #try with super

# one = One()
# two = Two()
# one.doanything()
# two.doanything()   


# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#         return n
#     else:
#         print("evenrything is fine")
#         return
# print("-----------------")
# print("reciprocal(2)",reciprocal(2))

# print("-----------------")
# print("reciprocal(0)",reciprocal(0))
# print("-----------------")

'''finally'''

# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#         return n
#     else:
#         print("evenrything is fine")
#         return
#     finally:
#         print("its time to exit")
#         return n


# print("-----------------")
# print("reciprocal(2)",reciprocal(2))

# print("-----------------")
# print("reciprocal(0)",reciprocal(0))
# print("-----------------")




# try:
#     i = int("hello")
# except Exception as e:

#     print(e)
#     print(e.__str__())



'''create ur own exception/using base_keyword'''

class MyZeroDivisionError(ZeroDivisionError):
    pass
def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("SOME WORSE NEWS")#raise is use to rise an error
    else:
        raise ZeroDivisionError("some bad news")

do_the_division(False)
do_the_division(True)


