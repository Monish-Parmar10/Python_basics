
'''class,obj , prop, '''

# class ThisIsMyfirstClass:
#     name = "monish" #property
#     age = 20

#     def getName(dm): #method
#         print() 



# firstObject = ThisIsMyfirstClass()  #obj
# print(firstObject)
# firstObject.getName()
# print(firstObject.name)


class student: #class student blue print of obj ex- mould of sothing which give shape containng the 
    def __init__(dm):
        dm.name ="" #it means current obj has varble so called name
        dm.age = 0
        dm.gender = ""
        dm.grade = ""
#3 things obj does 1st memory(obj) is created in RAM 2nd cunstructor runs automatically 3rd address/reference of obj stored in variable -monish 
monish = student() #obj student as a constructor and it give the addresss where the data sstores and put into the monish

print(monish)
#updating obj data
monish.name = "monish parmar"
monish.age = 19
monish.gender = "male"
monish.grade = "1th"
print(monish.name)
print(monish.age)
print(monish.gender)
print(monish.grade)



class Student:
    def __init__(dm, name, age , gender,grade):#constuct- initial value        #__init__ fix keyword in python for constructor
     dm.name = name
     dm.age = age
     dm.gender = gender
     dm.grade = grade         #class prop
    
    def printDetails(dm):
        print("Name:",dm.name)
        print("age:",dm.age)
        print("gender",dm.gender)
        print("grade:",dm.grade)

monish = Student("monish",20,"male","12th")#final val         #obj student as a constructor and it give the addresss where the data sstores and put into the monish
print(monish)

monish.printDetails()
