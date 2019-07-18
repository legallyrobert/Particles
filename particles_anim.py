from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd

df=pd.read_csv('out.txt',names=['t','x','y','z'],sep=' ')

def update_graph(t):
    data = df[df['t']==t]
    graph.set_data(data.x,data.y)
    graph.set_3d_properties(data.z)
    title.set_text('time={}'.format(t))
    return title,graph,

fig=plt.figure()
ax=Axes3D(fig)
title=ax.set_title('Particle Simulation')

data=df[df['t']==0]

ax.set_xlim3d(df['x'].min(),df['x'].max())
ax.set_xlabel('X')
ax.set_ylim3d(df['x'].min(),df['y'].max())
ax.set_ylabel('Y')
ax.set_zlim3d(df['x'].min(),df['z'].max())
ax.set_zlabel('Z')

graph, = ax.plot(data.x, data.y, data.z, linestyle="", marker="o")

time=df['t']

ani = matplotlib.animation.FuncAnimation(fig, 
        update_graph, 
        time, 
        interval=1,
        blit=True
        )

plt.show()
