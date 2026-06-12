'''Csv'''

# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Monish',99,'Indore','A'],
#     ['Naman',90,'Bhopal','B'],
#     ['Aman',90,'NYC','B'],
# ]
# with open('student.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('student.csv', 'r') as f :
#           for row in csv.DictReader(f):
#                 print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')



# import csv

# records = [
#     ['Name','age','Hindi','English','Maths'],
#     ['Monish',20,80,90,92],
#     ['Ansh ',19,77,50,82],

# ]

# import csv
# with open('Cls.csv','w',newline='') as f:
#        csv.writer(f).writerows(records)


# search_name= input("search_by name")
# found = False #creating a flag
# with open('Cls.csv', 'r') as f :
#             for row in csv.DictReader(f):
#                 if row['Name'] == search_name:
#                   print(f'Found{search_name}')
#                   print(f'{row['Name']}: {row['age']} age')
#                   found = True 
#                   break
# if not found:
#       print("studen is not found")


# #impoert numput lib as np np -> is a variable

# import numpy as np 

# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[22,33,44],[55,22,55],[77,44,22]])   #3 student * 3 subject

# print(arr2d.shape) #(3,3)

# print(arr2d.dtype)#int 64
# print(arr2d.ndim)#2 (2-dimensional)