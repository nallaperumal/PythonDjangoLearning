#pip install pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

days =  np.array([1,2,3,4,5])
dayFrame = pd.DataFrame(days,columns=['Day'])
print(dayFrame)
dayAndPrice = np.array([[1,350],[2,410],[3,450]])
dayAndPriceFrame = pd.DataFrame(dayAndPrice,columns=['Day', 'Price'])
print("...")
print(dayAndPriceFrame)
prices = np.array([220,250,310,350,240])
# plt.plot(days, prices, marker='v', color='red')
# plt.bar(days, prices,color='orange')
plt.bar(dayAndPriceFrame['Day'], dayAndPriceFrame['Price'],color='orange')
plt.title("Simulated Silver Price")
plt.xlabel("Days")
plt.ylabel("price /g")
plt.grid(True)
plt.show()
