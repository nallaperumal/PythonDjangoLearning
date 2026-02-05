#pip install pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib
days =  np.array([1,2,3,4,5])
dayFrame = pd.DataFrame(days,columns=['Day'])
print(dayFrame)
dayAndPrice = np.array([[1,350],[2,410],[3,450]])
dayAndPriceFrame = pd.DataFrame(dayAndPrice,columns=['Day', 'Price'])
print("...")
print(dayAndPriceFrame)

dataFrameFromCSV = pd.read_csv("products-100.csv")
# print(dataFrameFromCSV.info())
new_df = dataFrameFromCSV.dropna()
dataFrameFromCSV.fillna(0, inplace=True)
dataFrameFromCSV.fillna({"Price":0}, inplace=True)
dataFrameFromCSV.drop_duplicates(inplace=True)

salesByCategory = dataFrameFromCSV.groupby(['Category'])['Price'].sum()
salesByCategory.to_csv("salesByCategory.csv")
# for x in dataFrameFromCSV.index:
#     if dataFrameFromCSV.loc[x, "Price"] > 500:
#         dataFrameFromCSV.loc[x, "Price"] = 500
# dataFrameFromCSV.to_csv("capped-price-products.csv")        
# print(new_df.info())
newDF = dataFrameFromCSV.loc[1:11,['Name', 'Price']]

plt.bar(newDF['Name'], newDF['Price'],color='orange')
plt.show()

prices = np.array([220,250,310,350,240])
# plt.plot(days, prices, marker='v', color='red')
# plt.bar(days, prices,color='orange')
# plt.bar(dayAndPriceFrame['Day'], dayAndPriceFrame['Price'],color='orange')
# plt.title("Simulated Silver Price")
# plt.xlabel("Days")
# plt.ylabel("price /g")
# plt.grid(True)
# plt.show()
