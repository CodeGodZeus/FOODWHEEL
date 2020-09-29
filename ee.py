import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print customer_amount.head()
 

plt.hist(range(201),bins=40)
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Kk")
plt.show()
