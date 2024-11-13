#Data Analysis Task3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = {'name':['Dasha', 'Matvey', 'Masha', 'Anya', 'Sasha'], 'attendance':[100, 95, 87, 50, 30], 'mark': [100, 85, 82, 65, 50]}
df=pd.DataFrame(students)

print(df)

plt.scatter(df['attendance'], df['mark'], marker='x')