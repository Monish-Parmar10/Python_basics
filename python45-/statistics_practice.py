import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats #open sourse py library used for scientific , mathametic

#emplyee salaries (in thoushands rs)
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency  - where is the 'centre ' of data?

mean = np.mean(salaries)
median = np.median(salaries)
mode = stats.mode(salaries,keepdims = True).mode[0]

print(f'Mean (Average ): Rs.{mean:.1f}K')
print(f'Median   (middle value): Rs.{median}K')
print(f'Mode: (most common) Rs.{mode}K')


# Spread -  how varied is the data?
std = np.std(salaries)
variance = np.var(salaries)
rng = max(salaries) - min(salaries)
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3 - q1

print(f'Std Deviation : {std:.2f}K (most importtant spread measure)')
print(f'IQR: {iqr}K (Q1 = {q1}, Q3 = {q3})')

#outlier dectection  using IQR (integration range)

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr#1.5 is the rule to caculate the outliers
outliers = [x for x in salaries if x < lower or x > upper]
print(f'outliers : {outliers}') #outlier is like exception like out of range data which is not in the range of data