class ExampleClass:
    def __init__(self,val=1):
        self.first = val
    def set_second(self,val):
        self.second = val

object_1=ExampleClass(1)
object_2=ExampleClass(2)
object_2.set_second(3)
object_3=ExampleClass(4)
object_3.third = 5 # type: ignore

print(object_1.__dict__) # dict dictionary that stores all instances variable of obj
print(object_2.__dict__) # use to print the key and there values in reprentable format or readable format
print(object_3.__dict__)