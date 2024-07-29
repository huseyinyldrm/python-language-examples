import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,9,20)
y=x**3
z=x**2

"""
figure=plt.figure()

axesCube=figure.add_axes([0.1,0.1,0.8,0.8]) # 0'a 1 lik kismi %80 kaplar.

axesCube.plot(x,y,'b')
axesCube.set_xlabel("X Axis")
axesCube.set_ylabel("Y Axis")
axesCube.set_title("Cube")

axesSquare=figure.add_axes([0.20,0.65,0.25,0.25])
axesSquare.plot(x,z,'r')
axesSquare.set_xlabel("X Axis")
axesSquare.set_ylabel("Y Axis")
axesSquare.set_title("Square")

"""

"""
figure=plt.figure()

axes=figure.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=2)
# legend'e konum vermek icin loc=1 ise sag ustte,loc=2 ise sol ustte , loc=3 ise sol altta , loc=4 ise sag allta konumlanir.


"""

fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(5,5))
axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.png")
# figuru kaydetmek icin.pdf olarak da kaydedilebilir.

fig.savefig("figure1.pdf")

plt.show()
