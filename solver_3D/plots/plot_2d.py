#!/bin/usr/python3
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

range_min=-1e-2
range_max= 1e-3
fname1 = "output_000000.dat"
# fname1 = "output_000020.dat"
# fname1 = "output_007000.dat"
fname1 = "output_004000.dat"


# global settings
plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0 #x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0 #y軸主目盛り線の線幅
plt.rcParams['font.size'] = 22 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1.0 # 軸の線幅edge linewidth。囲みの太さ
plt.rcParams['text.usetex'] = True # Latex text
plt.rcParams["axes.formatter.use_mathtext"]=True

fig = plt.figure()
fig.set_size_inches([10, 8])
# fig.figsize= fig.figaspect(4)
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.16)

# data read
data1=(np.loadtxt(fname1,dtype="float",skiprows=0)).T
print(np.shape(data1))

# data definition
jmax = 101
kmax = 101

x1=data1[0,:jmax]  # x
x2=data1[0,:kmax]  # y
q1=data1[2]  # r
q2=data1[3]  # u
q3=data1[4]  # v
q4=data1[5]  # w
q5=data1[6]  # p
q6=data1[7]  # ry1
# q6=data1[7]  # ry2
# q7=data1[8]  # ry3

q1 = np.array(q1).reshape(-1, jmax).tolist()
q2 = np.array(q2).reshape(-1, jmax).tolist()
q3 = np.array(q3).reshape(-1, jmax).tolist()
q4 = np.array(q4).reshape(-1, jmax).tolist()
q5 = np.array(q5).reshape(-1, jmax).tolist()
q6 = np.array(q6).reshape(-1, jmax).tolist()
# q7 = np.array(q7).reshape(-1, jmax).tolist()

# format
# plt.xlim(0,1)
# plt.ylim(range_min,range_max)
plt.grid(False)
nmax = x1.shape[0]

# plt.title("Plot 2D array")
plt.xlabel(r'$x$',fontsize=22)
plt.ylabel(r"$z$",fontsize=22)
# plt.xticks(np.arange(0,1.2,0.2))

xx, yy = np.meshgrid(x1, x2)
cf = plt.contourf(xx, yy, q1, cmap="jet")
# cf = plt.contourf(xx, yy, q2, cmap="jet")
# cf = plt.contourf(xx, yy, q3, cmap="jet", levels=12)
# cf = plt.contourf(xx, yy, q4, cmap="jet", levels=12)
# cf = plt.contourf(xx, yy, q5, cmap="jet", levels=12)
# cf = plt.contourf(xx, yy, q6, cmap="jet", levels=12)


cb = plt.colorbar(cf)
# cb.set_label(r'$\rho$',fontsize=22,y=1,x=1.2,rotation=0)
# cb.formatter.set_scientific(True)
cb.ax.ticklabel_format(style='sci', scilimits=(-6,6)) 

ax = plt.gca()
aspect = (ax.get_xlim()[1] - ax.get_xlim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0])                     
ax.set_aspect(aspect)

# plt.show()
fig.savefig("2dtest.png")
