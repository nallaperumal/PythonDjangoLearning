import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np

days =  np.array([1,2,3,4,5,6,7,8,9,10,11,12])
prices = np.array([350,400,410,435,451,489,500,350,310,329,331,350])
plt.plot(days, prices,marker='o', color='green')
plt.title("Simulated Silver Price")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()