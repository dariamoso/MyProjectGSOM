import numpy as np
import pandas as pd

income = np.array([10000, 20000, 15000, 17000, 30000, 28000, 27000, 36000, 40000, 49000])

income_without_tax = income * 0.7

expenses = np.array([-8000, -7000, -10000, -9000, -11000, -13000, -20000, -12000, -17000, -18000])

m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
data = {'income w\ tax, $': income_without_tax, 'expenses, $': expenses}
df = pd.DataFrame(data, index=m)

print(df)

print("\n1st Quarter (Jan, Feb, Mar):")
print(df.loc['Jan':'Mar'])