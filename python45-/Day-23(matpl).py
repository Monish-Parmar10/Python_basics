
# #Data
# months = ['Jan','Fub','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# sales = [45,52,48,62,58,72,69,75,68,82,90,95] #in thousand

# #line Chart - tends over time

# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker='o',color='steelblue', linewidth = 2,markersize = 8) #plot
# plt.fill_between(months, sales, alpha=0.15, color='steelblue')
# plt.title('Monthly Sales 2024 (Rs.thousands)',fontsize=14, fontweight = 'bold')
# plt.xlabel('Months')
# plt.ylabel('Sales(Rs. k)')
# plt.grid(True,alpha=1.5)
# plt.tight_layout()
# plt.show()


# #Data 
# cities = ['Bhopal','Indore','Ujjain','Gwalior','Jabalpur']
# std =[1200,2800,980,850,650] 
# colors = ['#2196F3','#4CAF50','#ff9800','#9C27B0','#F44336']

# #bar chart = comparing categories

# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, std, color = colors, edgecolor= 'white', linewidth=1.5)
# plt.title('students Enrolled per city')
# plt.ylabel('Number of students')
# plt.xlabel('Cities')
# for bar, val in zip(bars,std):
#     plt.text(bar.get_x()+bar.get_width()/2,val+20,str(val),ha = 'center', fontweight ='bold')
# plt.tight_layout()
# plt.show()


'''SCATTER PLOT / TELL ABOUT DATA PLOT AND POINT DEFINE BY THE COLORS'''


#clip for get proper range
# import numpy as np
# std_hrs = np.random.uniform(2,10,50)
# mrks = std_hrs * 7 + np.random.normal(0,8,50)
# mrks = np.clip(mrks,30,100)

# plt.figure(figsize=(8,5))
# plt.scatter(std_hrs, mrks, c=mrks, cmap='RdYlGn', s = 100, alpha =0.8)
# plt.colorbar(label = 'Marks')
# plt.title('study hours vs exam marks:')
# plt.xlabel('Study hourse/Day')
# plt.ylabel('Exam Marks')
# plt.show()

'''Seaborn'''
'''significance of 42 in maths or other'''

'''create a line chart'''
'''histplot/ histogram plot'''
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
import pandas as pd

np. random.seed(42)
#Data
df = pd.DataFrame({
    'marks':  np.random.randint(40,100,100),
    'study_hours': np.random.uniform(2,10,100),
    'city':        np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender': np.random.choice(['Male','female'],100)})

plt.figure(figsize=(10,4))  
sns.histplot(df['marks'],bins=20,kde=True, color='steelblue')
plt.title('Distribution of student marks:')
plt.show()