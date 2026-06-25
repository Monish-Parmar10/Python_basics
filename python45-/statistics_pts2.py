import numpy as np# ra
import seaborn as sns #heatmap, barplot ,scatter plot,Used for(beautiful statistical graphs)
import matplotlib.pyplot as plt #used for making graphs , line /pie/Histogram
import pandas as pd #Dataframes
from scipy import stats #statistics module
#data
np.random.seed(42)#it use to take the random values under 42(and feed it inside)
study = np.random.uniform(2, 10, 60) #it mean genrate 60 decimal values btw 2 and 10
marks = study * 8 + np.random.normal(0, 1, 60) #(mean,std deviatnion,size) it genrate 60 values with mean 0 and std deviation 1
absent = 10 - study + np.random.normal(0, 1, 60)
df = pd.DataFrame({"Study_Hours":study,"Marks":marks,"Absence":absent})

corr_matrix = df.corr()

print(corr_matrix.round(3))

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot = True, cmap='coolwarm',vmin=-1, vmax = 1,fmt='.2f')
plt.title('Correlation')
#pearson correlation

r, p_value = stats.pearsonr(study,marks)
print(f'Study-Marks correlation: r={r:.3f}, p = {p_value:.4f}')
print('Interpretation', 'strong positive' if r>0.7 else 'moderate' if r>0.4 else 'weak')




import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm      #normal distribbution calculator

# #you feed it a mean and standard deviationn and it can answer any probability question about it

# #normal distribution - the bell curve
# #normal distribution with mean 165cm and standard deviation 7cm
# mean_h, std_h = 165, 7

# #probablity of being taller than 175cm
# prob = 1 - norm.cdf(175, mean_h, std_h)
# print(f'P(height > 175cm) = {prob:.4f} = {prob*100:.1f}%')

# #the 68-95-99.7 rule
# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')


'''assignment- sales data analysis'''


'''train-test-split'''
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

#simulatedd datasert : 500 students records
np.random.seed(42)
X = np.random.rand(500,5)     #5 features
y = np.random.randint(0,2,500)     #labels: pass(1)/fail(0)

#80/20 train-test split
X_train,X_test,y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, random_state=42)
cv_scores =  cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f'CV Scores each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')