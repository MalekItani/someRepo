import matplotlib.pyplot as plt
import numpy as np


limit = 31
cells = np.random.randint(0,2,(limit,limit))
cells[:,limit-1] = 0
cells[:,0] = 0
cells[0,:] = 0
cells[limit-1,:] = 0
frames = 500
plt.ion()
figure = plt.figure()
axis = figure.add_subplot(111)
plt.show()
dt = 0.1

while len(np.nonzero(cells)):
    for i in range(1,limit-1):
        for j in range(1,limit-1):
            ones=[]
            zeros=[]
            N = cells[i, j + 1] + cells[i, j-1] + cells [i+1, j] + cells[i-1, j] + cells[i+1, j-1] + cells[i-1,j+1] + cells[i+1, j+1] + cells[i-1, j-1]
            if cells[i,j] == 0 and N==3:
                ones.append((i,j))
            elif cells[i,j] == 1 and N in [3,4]:
                pass
            else:
                zeros.append([i,j])
            for x,y in ones:
                cells[x,y] = 1
            for x,y in zeros:
                cells[x,y] = 0
 
    alive = np.nonzero(cells)
    dead = np.where(cells==0)

    print(dead) 

    axis.scatter(alive[0], alive[1], marker='o')
    axis.scatter(dead[0], dead[1], marker='x')
    axis.set_xlim([-1, limit])
    axis.set_ylim([-1, limit])
    if plt.waitforbuttonpress(dt):
        plt.close()
        break
    plt.cla()


plt.close(figure)


