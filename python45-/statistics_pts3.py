import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score  


study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
marks = [25,38,52,65,71,78,85,89,93,43,68,82,91,67]

x = np.array(study).reshape(-1,1)
y = np.array(marks)

x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

print(f'Slope: {model.coef_[0]:.2f}')
print(f'Intercept: {model.intercept_:.2f}')

y_pred = model.predict(x_test)
print(f'R**2 Score:{r2_score(y_test, y_pred):.4f}')
print(f'RMSE: {mean_squared_error(y_test, y_pred)**0.5:.2f} marks average error')

#predict new student

new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks: {new_pred:.1f}')

#plot
plt.figure(figsize=(9,5))
plt.scatter(x,y,color='steelblue', s=100,alpha=0.8, label='actual')
plt.plot(x,model.predict(x),color='red',linewidth=2, label='predicted line')
plt.xlabel('Study Hours/Day')
plt.ylabel(' Exam Marks')
plt.title('linear regression - study hours vs marks')
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()                                                  