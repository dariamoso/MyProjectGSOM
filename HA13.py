import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

income = np.array([10000, 20000, 15000, 17000, 30000, 28000, 27000, 36000, 40000, 49000])

income_without_tax = income * 0.7

expenses = np.array([-8000, -7000, -10000, -9000, -11000, -13000, -20000, -12000, -17000, -18000])

m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
data = {'income w\ tax, $': income_without_tax, 'expenses, $': expenses}
df = pd.DataFrame(data, index=m)
df["saving"] = df['income w\ tax, $'] - df['expenses, $']

print(df)

print("\n1st Quarter (Jan, Feb, Mar):")
print(df.loc['Jan':'Mar'])


plt.plot(m, income, color='magenta', marker='.', label="income, $")
plt.xlabel("month")
plt.ylabel("income")
plt.show()

saving=income-expenses
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
colors = ["blue", "magenta", "green", "yellow", "red", "orange", "pink", "black","purple", "cyan"]
plt.bar(m, saving, color=colors)
plt.xlabel("month")
plt.ylabel("saving")
plt.show()

total_savings = saving.sum()
plt.pie(saving, labels=m, colors=colors)
plt.show()

q1 = income[0:3]
q2 = income[3:6]
q3 = income[6:9]
q4 = income[9:]

q1a = stats.mean(q1)
q2a = stats.mean(q2)
q3a = stats.mean(q3)
q4a = stats.mean(q4)

print(q1a)
print(q2a)
print(q3a)
print(q4a)


import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset("car_crashes")
print(car_crashes.head())

sns.relplot(
    x='speeding', 
    y='total', 
    size='ins_premium', 
    hue='alcohol',
    data=car_crashes
)

sns.lmplot(
    x='alcohol', 
    y='total', 
    data=car_crashes, 
)