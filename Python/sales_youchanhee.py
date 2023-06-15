import pandas as pd
import matplotlib.pyplot as plt


sales_data = pd.read_csv('./sales_data_.csv')
sales_data.head()

fig, ax = plt.subplots()

ax.plot(sales_data['month'], sales_data['tv'], linewidth=3, marker='o', markersize=7, label='TV sales')
ax.plot(sales_data['month'], sales_data['laptop'], linewidth=3, marker='o', markersize=7, label='Laptop sales')
ax.plot(sales_data['month'], sales_data['phone'], linewidth=3, marker='o', markersize=7, label='Phone sales')


ax.set_xticks(sales_data['month'])
ax.set_yticks([1000, 2000])
ax.set_xlabel('month')
ax.set_ylabel('Unit')
ax.set_title('You Chan Hee Sales Data')
ax.legend(loc='upper left')

plt.show()