'''sea born'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.DataFrame({
    'marks':  np.random.randint(40,100,100),
    'study_hours': np.random.uniform(2,10,100),
    'city':        np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender': np.random.choice(['Male','female'],100)})

# plt.figure(figsize=(10,4))  
# sns.histplot(df['marks'],bins=20,kde=True, color='steelblue')
# plt.title('Distribution of student marks:')
# plt.show()

# '''BOX PLOT -] OUTLIERS AND SPREAD PER GROUP'''
# sns.boxplot(data = df , x = 'city', y ='marks', palette='Set2')
# plt.title('Marks distribution by city')
# plt.show()


'''CORRELATION HEAT MAP - CRITICAL IN DS'''
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(), annot = True, cmap='coolwarm', vmin=-1, vmax=1)
# plt.title('corelation matrx')
# plt.show()

# sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
# plt.show()

'''create csv with 25 student data , name , age , city , marks in 5 subject'''

'''ML gives prediction and acurate output on the basis of feeded data'''


