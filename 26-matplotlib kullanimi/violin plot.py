import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=[np.random.normal(0,std,100) for std in range(1,4)]

sns.violinplot(data=data)
plt.title("Violin Plot")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()