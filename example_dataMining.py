from matplotlib import pyplot as plt
plt.axis([5,60,0,100])
plt.title('Pushes')
plt.xlabel('# of pushes')
plt.ylabel('# of posts')
plt.xticks([15, 10,30])
plt.bar([60,30,55])
plt.show()
