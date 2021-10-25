import re
import numpy as np
import matplotlib.pyplot as plt

x_list = []  # xi
y_list = []  # yi
z_list = []  # zi

with open('translationsFile.txt', 'rt') as myfile:  # Open translationsFile.txt for reading
    for myline in myfile:
        if myline.startswith("["):
            res = myline.replace("[","")
            res = res.replace(";","")
            res = res.replace("]","")
            res = float(res)
            x_list.append(res)
        elif myline.find(";")!=-1:
            res = myline.replace("[", "")
            res = res.replace(";", "")
            res = res.replace("]", "")
            res = float(res)
            y_list.append(res)
        elif myline.find("]") != -1:
            res = myline.replace("[", "")
            res = res.replace(";", "")
            res = res.replace("]", "")
            res = float(res)
            z_list.append(res)

t = np.array([x_list, y_list, z_list])[:,:500]
rotation_list = []

with open('rotationsFile.txt', 'rt') as myfile:  # Open rotationsFile.txt for reading
    for myline in myfile:
        res = myline.replace("[","")
        res = res.replace("]","")
        res = res.replace(";","")
        rotation_list.append(res)

rotation_list_plot= "".join(rotation_list)
f = open("rotationToPlotFile.txt", "a")
f.write(rotation_list_plot)
f.close()

pose_list = []
input = np.loadtxt("rotationToPlotFile.txt", delimiter=',')
mat3 = np.split(input,len(input)/3)[:500]

for i in range(500):
    ti=t[:,i]
    ri=mat3[i]
    pose=-ri.transpose() @ ti  # calculation of a current pose
    pose_list.append(pose)  # append this pose(i) in the pose_list

pose_list = np.array(pose_list)  # transfer to numpy array before plotting

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = pose_list[:,0],  pose_list[:,1],  pose_list[:,2]
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()