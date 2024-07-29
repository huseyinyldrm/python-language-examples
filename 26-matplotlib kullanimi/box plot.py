import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
 
data=[np.random.normal(0,std,100) for std in range(1,4)]
sns.boxplot(data=data)
plt.title("Box Plot")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()