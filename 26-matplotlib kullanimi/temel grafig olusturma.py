import matplotlib.pyplot as plt
import numpy as np
"""
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,"o--b")
plt.axis([0,6,0,20]) # x ekseninin alacagi degerler.

plt.title("Grafik basligi")
plt.xlabel("x Label")
plt.ylabel("y Label")

"""
"""
x=np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("grafik basligi")
plt.legend() # plt.plot icindeki labelleri ekranda gostermek icin bu eklendi.

"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(3) # alt alta 3 grafik yapmak icin.
axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("cubic")

plt.tight_layout() # basliklarin ic ice gecmemesi icin.


"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2) # toplam 4 parca halindeki grafik olusturma.
fig.suptitle("Grafik Basligi")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="yellow")
axs[1,1].plot(x,x**4,color="black")

"""


import pandas as pd

df=pd.read_csv("nba.csv")

df=df.drop(["Number"],axis=1)

# Takım bazında grupla
grouped=df.groupby("Team")

# Sadece sayısal sütunları seç ve ortalamalarını al
df_grouped=grouped.mean(numeric_only=True)

# İlk 50 satırı al ve subplots=True ile çiz
df.head(50).plot(subplots=True,figsize=(10,12))

plt.legend()

plt.show()

"""
'b' => mavi duz grafik cizgisi.
'or'=> kirmizi grafik cizgisi.
'-g'=> yesil duz grafik cizgisi.
'--g'=> yesil cizgili grafik cizgisi.
'--' => istenilen rengi yanina yaz ve cizgili grafik cizgisi olussun.
' ^k:'=> cizgi ve ucgen belirtecli grafik cizgisi.marker=ucgen sekline olur.
bunlari plt.plot() ' a 3. parametre olarak gondeririz.
"""