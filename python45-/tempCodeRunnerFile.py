
search_name= input("search_by name")
found = False #creating a flag
with open('Cls.csv', 'r') as f :
            for row in csv.DictReader(f):
                if row['Name'] == search_name:
                  print(f'Found{search_name}')
                  print(f'{row['Name']}: {row['age']} age')
                  found = False
                  break
if not found:
      print("studen is not found")