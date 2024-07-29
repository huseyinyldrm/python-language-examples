import matplotlib.pyplot as plt

labels=["Category A","Category B","Category C"]
sizes=[30,40,50]
plt.pie(sizes,labels=labels,autopct="%1.1f%%",shadow=True)

plt.title("Pie Chart")
plt.show()