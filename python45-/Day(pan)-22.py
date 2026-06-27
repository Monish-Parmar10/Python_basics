
import pandas as pd

data = {

'Name': ['Rahul','Monish','Naman','Aman','Baman'],
'Age': [22,21,44,55,54],
'Marks': [45,67,87,88,45],
'City': ['Bhopal','Indore','Bhopal','Sehore','Indore'],
}

df = pd.DataFrame(data)
# print(df)

# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())


# print("df['Name']: \n",df['Name']) #using sq braket because it say pass the list and then pass the key 

# print(df[['Name','Marks']])

# print(df[df['Marks']>= 85])
# print(df[df['City'] == 'Bhopal'])
# print(df[(df['Marks']>=22) & (df['City'] == 'Indore')])



# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x>= 75:
#         return 'B'
#     else:
#         return 'c'
    
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print("-----------")
# print(df)


#groupby - like excel pivot
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)
'''cleaning csv file, using split/strip/replace'''

df2 =pd.read_csv('student.csv')
print(df2)

#.str. ->vectorization string operation

# df2 ['Name'] = df2['Name'].str.split() #strip convert each string into list of string
# print(df2)



# df2 ['First'] = df2['Name'].str.split().str[0]#for getting 1st last name   
# print(df2,'\n')                               #for getting 1st last name      
# df2["Last"] = df2['Name'].str.split().str[1]  #for getting 1st last name 
# print('/n',df2)

df2['Name'] = df2['Name'].str.strip()
print(df2)

df2['Marks'] = df2['Marks'].str.strip('#')
print(df2)


df2['Grade'] = df2['Grade'].str.strip('@')
df2['Grade'] = df2['Grade'].str.strip('*')
print(df2)


df2['City'] = df2['City'].str.replace('dict','')
df2['City'] = df2['City'].str.replace('City','')
print(df2)

df2.to_csv('clean_output.csv', index=False) 

#.upper()/.lower() /.str.replace / str.contains / .str.capitalize() / len