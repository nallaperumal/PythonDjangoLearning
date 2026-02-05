import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np
import pandas as pd

days =  np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dayFrame = pd.DataFrame(days,columns=['Day'])

# print(dayFrame)
prices = np.array([350,400,410,435,451,489,500,350,310,329,331,350])

dayAndPrice = np.array([[1,350],[2,410],[3,450]])
priceFrame = pd.DataFrame(dayAndPrice,columns=['Day','Price'])
print("...")
df = pd.read_csv('products-100.csv')
new_df = df.dropna()
print(df.info())
print("...")
# print(new_df.to_string())
print(new_df.info())
# plt.bar(days, prices,color='orange')
plt.bar(priceFrame['Day'], priceFrame['Price'],color='orange')
plt.title("Simulated Silver Price")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.grid(True)
# plt.show()