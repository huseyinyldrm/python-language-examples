import matplotlib.pyplot as plt

"""
#Stack Plot

yil=[2011,2012,2013,2014,2015]

oyuncu1=[8,10,12,7,9]
oyuncu2=[7,10,12,17,19]
oyuncu3=[18,10,12,27,29]


plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("Yillara gore atilan goller")

plt.xlabel("yil")
plt.ylabel("gol sayisi")
plt.legend()

plt.show()

"""
"""

# Pie Grafigi

goal_types="Penalti","Serbest Vurus","Kaleye Atilan Sut"

goals=[12,35,7]
colors=["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")

plt.show()

"""

"""

# Cubuk Grafigi

# Verileri tanimlayin

audi_x = [1.75, 2.75, 3.75, 4.75, 5.75]
audi_y = [80, 20, 40, 70, 80]

volvo_x = [2.25, 3.25, 4.25, 5.25, 6.25]
volvo_y = [30, 60, 30, 80, 90]

# Çubuk grafikler
plt.bar(audi_x, audi_y, label="AUDI", width=0.3)
plt.bar(volvo_x, volvo_y, label="VOLVO", width=0.3)

# Efsane, etiketler ve baslik
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (KM)")
plt.title("Araç Bilgileri")

# Grafigi goster
plt.show()

"""
# Histogram Grafigi

yaslar=[22,55,54,65,77,88,99,76,65,44,32,34,66,78,11,2,33,21,24,25,23]
yasGruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yasGruplari,histtype="bar",rwidth=0.8)
plt.xlabel("Yas Gruplari")
plt.ylabel("Kisi Sayisi")
plt.title("Histogram Grafigi")

plt.show()

