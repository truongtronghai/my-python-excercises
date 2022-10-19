from matplotlib import pyplot as plt
import numpy as np

xpoints = np.array([1,5,8])
ypoints = np.array([3,4,10])
labels = ["shop1","shop2","shop3"]
plt.plot(xpoints,ypoints,"*-.g")
plt.xticks(xpoints,labels,rotation='vertical') # gan label cho gia tri x cua plot nay

plt.plot([6,9,14],[7,1,5],"o:b")

plt.show()

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(231),plt.plot(x,y),plt.title("Plot 1")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(236)
plt.plot(x,y)
plt.title("Plot 2")

plt.show()
