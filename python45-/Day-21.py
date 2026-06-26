
import numpy as np #here np is a varible
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[22,33,44],[55,22,55],[77,44,22]])   #3 student * 3 subject



print(arr2d.shape) #(3,3) #dimention

print(arr2d.dtype)#int 64 
print(arr2d.ndim)#2 (2-dimensional) ndim n=2 


zeros = np.zeros((3,4)) #print(3X4) matrix containing zeros
print(zeros)

ones = np.ones((2,5)) #print(2x5) matrix contaiining ones
print(ones)

rng = np.arange(0,50,5) #5  getting gap btw the numbers
print(rng)

lin = np.linspace(0,1,11) #it prints the val btw the 0->1 taking around 11 element
print(lin)

random = np.random.randint(40,100,(5,3))  #print(matrix 5x3) containing random values btw 1 40 to 100
print(random)






'''vectorised math'''


arr = np.array([10,20,30,40,50,])
print(arr*2) #it crete new array not update the existing one
print(arr) 
print(arr + 5)
print(arr ** 2)


'''statistics operation with numpy'''


marks_2 = max([[22,33,44,55],[33,44,55,66],[66,77,88]])
print(marks_2)

marks_2 =np.array([[22,33,44,55],[33,44,55,66],[11,66,77,88]])

print(np.mean(marks_2))
print(np.mean(marks_2, axis = 1))
print(np.mean(marks_2, axis = 0))
print(np.max(marks_2))
print(np.std(marks_2))


'''boolean indexing (criticl for data filtering)'''

marks_2 =np.array([22,33,44,55,33,44,55,70,11,66,77,88])

print(marks_2[marks_2>70]) 


'''PANDAS'''


arr = np.array([11,22,33])
print(arr)
print(arr.__dict__)

