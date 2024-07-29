import matplotlib.pyplot as plt
import numpy as np

data=np.random.randn(1000)
plt.hist(data,bins=30,edgecolor="black")
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("frequency")

plt.show()