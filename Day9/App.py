import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np
import pandas as pd

days =  np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dayFrame = pd.DataFrame(days,columns=['Day'])

# print(dayFrame)
prices = np.array([350,400,410,435,451,489,500,350,310,329,331,350])

dayAndPrice = np.array([[1,350],[2,410],[3,450]])
priceFrame = pd.DataFrame(dayAndPrice,columns=['Day','Price'])
# print("...")
dataFrame = pd.read_csv('products-100.csv')
new_df = dataFrame.dropna()
# print(dataFrame.info())
dataFrame.drop_duplicates(inplace = True)
# print(dataFrame.info())
# print(df.info())

# df.dropna(inplace = True)
# df.fillna(0,inplace = True)
dataFrame.fillna({"Price": 0}, inplace=True)
for x in dataFrame.index:
  if dataFrame.loc[x, "Price"] > 600:
    dataFrame.loc[x, "Price"] = 600
salesByCategory = dataFrame.groupby('Category')['Price'].sum()    
print(salesByCategory)
salesByCategory.to_csv('products-100_updated.csv')
print("...")
# print(new_df.to_string())

# print(dataFrame[['Name','Price']])
filteredDF = (dataFrame.loc[3:9,['Name','Price']])
# filteredDF.plot()
plt.bar(days, prices,color='orange')
plt.bar(filteredDF['Name'], filteredDF['Price'],color='orange')
plt.title("Simulated Silver Price")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()