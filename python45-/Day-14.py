
'''class,obj , prop/ using cls attributes and method(self) calling to get data through obj '''


class ThisIsMyfirstClass: #<- class
    name = "monish" #property they are class attributes
    age = 20                   #they are class attributes

    def getName(self): #method (self) refers to the current obj(obj calls me i will receive)
        print()


firstObject = ThisIsMyfirstClass()  #obj(instance of the class)
print(firstObject) #o/p Default string representation of the object (includes its type and an internal memory identifier).
firstObject.getName() #to exicute get name method / method belongs to the object /ex - hey obj execute ur getname method then python send obj as self
print(firstObject.name)   
print(firstObject.age) 



'''using constructor and updating data after creating obj '''


class student: #class student blue print of obj ex- mould of something which give shape containng the 
   
   #auto run whenever obj is createds
    def __init__(dm):
        #(so called instance attributes)
        dm.name ="" #it means current obj has var so called name
        dm.age = 0   #it means current obj-> create var called name or age etc
        dm.gender = ""
        dm.grade = ""
#3 things obj does 1st memory(obj) is created in RAM 2nd cunstructor runs automatically 3rd address/reference of obj stored in variable -monish 
monish = student() #obj student as a constructor and it give the addresss where the data sstores and put into the monish
                   #or for obj student() calls the class, which creates a new object and automatically runs __init__() to initialize it.
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


'''using constructor(initialise val) and method to print data '''


class Student: #self explicit pass automatically
    def __init__(self, name, age , gender,grade):#constuct- initial constructor    #__init__ fix keyword in python for constructor
     self.name = name
     self.age = age
     self.gender = gender
     self.grade = grade         #class prop
    
    def printDetails(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("gender",self.gender)
        print("grade:",self.grade)
#monish vaiable holding refrence to that obj
monish = Student("monish",20,"male","12th")#()-> create obj      #obj student as a constructor and it give the addresss where the data sstores and put into the monish
print(monish) #it gives unreadable address or memory address of obj
print(monish.__dict__) #dict returns a dictionary containing the object's instance attributes and their values.(type of structure store like key and values)
monish.printDetails()
 

#(remeber pass obj as a self)