'''negative indexing'''

# city = 'Bhopal'
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])


'''slicing'''

# name = 'priya sharma'

# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])

# print(len(city))
# print(len(name))

'''split or trim method for clearing white space'''

'''in for searching the text in list'''

# text = '  Hello Python World! '
# #Case

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# #Strip whitespace
# print(text.strip())

# #search

# print('python' in text) #true
# print(text.find('python')) # 8 space count including hello and white space
# print(text.count('l')) 


'''split and join  '''

csv = 'Rahul,22,Bhopal,Engineer'
parts = csv.split(',')
print(parts)
print(parts[0])
rejoined = ' | '.join(parts)
print(rejoined)

# # #check content

# # print('hello123'.isalnum())
# # print('12345'.isdigit())
# # print('Python'.isalpha())
# # print(' '.isspace())

# #start /end check

# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

'''Special string at , 62'''

# #assning 3 var at a time
# name,marks, rank = 'monish', 92.567 , 3 

# print(f'Hello,{name}!')

# #format number
# print(f'marks:{marks:.2f}') #92.57 (2 decimal place )
# print(f'marks:{marks:.0f}') #93 (rounded)
# print(f'count:{1000000:,}')#1,000,000 (comma saperator)

# #padding and alignment
# print(f'{name:<15} | {marks:>8.2f}|Rank:{rank}') # left/right align
# # monish     | 92.57 |Rank:3
# print(f'hello{name:^10}')
# print(f'hello {}')





# #Expression inside  {}
# price,gst = 500 ,0.18
# print(f'price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total.Rs/{price*(1+gst):.2f}')

string = "Hello , how are you doing today "
string = string.lower()
print(string)
count = 0
for wrd in string:
     if wrd in "aeiou":
#    if wrd == 'A' or wrd == 'E' or wrd == 'I' or wrd =='O'or wrd =='U' or wrd =='a' or wrd =='a' or wrd =='e' or wrd =='i' or wrd =='o':
      count +=1
print("vowel",count)
print(string[15:19])
result = string.split()
print(" ".join(result[::-1]))
print(string[-1:])
if string == string [::-1]:
    print("the string is palindrome")
else:
    print("string is not palindrome")

'''with or as resourse lock or resourse memangement '''

# with open("data.txt","r") as file:
#     data = file.read()

# print(data)

'''read/write/update'''
with open('students.txt','w') as f:
    f.write('Rahul sharma,87,bhopal\n')
    f.write('vijay sharma,77,Indore\n')
    f.write('amit sahu,98,sehore\n')

with open('student.txt', 'a') as f:
    f.write('Sneha joshi,88,bhopal\n')

with open('students.txt','r') as f:
    content = f.read()
print(content)

with open ('student.txt','r') as f:
   for line in f:
       name, marks, city = line.strip().split(',')
       print(f'{name:<15} | {marks:>5} | {city}')
       print("-----------")

