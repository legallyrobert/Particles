#! /usr/local/bin/python3
import numpy as np
from scipy import constants as sci

class Particle(object):
    def __init__(self,charge,mass,initialVel,initialPos):
        self.charge=charge
        self.mass=mass

        self.force=np.zeros([3,1])

        self.initialVel=initialVel
        self.currentVel=initialVel

        self.initialPos=initialPos
        self.currentPos=initialPos

        self.static=False

class Simulation(object):
    def __init__(self,p1,p2):
        self.K=1/(4*sci.pi*sci.epsilon_0)
        self.p1=p1
        self.p2=p2
        self.d=np.subtract(self.p1.currentPos,self.p2.currentPos)
        self.r=np.linalg.norm(self.d)
        self.r_hat=self.d/self.r

    def coulomb(self):
        top=(self.K
                *self.p1.charge
                *self.p2.charge
                *(self.r_hat/self.r)
                )
        bottom=np.power(self.r,2)

        self.p1.force=top/bottom
        self.p2.force=np.negative(self.p1.force)
        
    def magnetism(self):
        top=(sci.mu_0*self.p1.charge*np.cross(
            self.p1.currentVel,
            self.r_hat/self.r,
            axis=0) # define vectors along first axis, rather than last
            )
        bottom=(4*sci.pi*np.power(self.r,2))
        B=top/bottom

        F=(self.p1.charge*np.cross(
            self.p1.currentVel,
            B,
            axis=0)
            )

        self.p1.force=np.add(self.p1.force, F)
        self.p2.force=np.negative(self.p1.force)

    def accumulateForces(self):
        self.coulomb()
        self.magnetism()

    '''
    def velocities(self):
        tmp1=self.p1.currentVel
        tmp2=self.p2.currentVel

        for i in range(0, 3):
            self.p1.currentVel[i]=(
                    self.p1.forces[i]
                    *TIMESTEP
                    /self.p1.mass
                    +self.p1.initialVel[i]
                    )
        for i in range(0, 3):
            self.p2.currentVel[i]=(
                    self.p2.forces[i]
                    *TIMESTEP
                    /self.p2.mass
                    +self.p2.initialVel[i]
                    )

        self.p1.initialVel=tmp1
        self.p2.initialVel=tmp2

    def positions(self):
        tmp1=self.p1.currentPos
        tmp2=self.p2.currentPos

        for i in range(0,3):
            self.p1.currentPos[i]=(
                    self.p1.currentVel[i]
                    *TIMESTEP
                    +self.p1.initialPos[i]
                    )
        for i in range(0,3):
            self.p2.currentPos[i]=(
                    self.p2.currentVel[i]
                    *TIMESTEP
                    +self.p2.initialPos[i]
                    )

        self.p1.initialPos=tmp1
        self.p2.initialPos=tmp2
    '''

def main():

    #Initial velocity np arrays
    v1 = np.zeros([3,1])
    v2 = np.zeros([3,1])

    #Initial position np arrays
    p1 = np.zeros([3,1])
    p2 = np.zeros([3,1])

    #Set velocity
    v1[0] = 1
    #Set position
    p1[0] = 1

    proton   = Particle(sci.e, sci.m_p, v1, p1)
    electron = Particle(-sci.e, sci.m_e, v2, p2)
    
    simulation = Simulation(proton, electron)
    simulation.accumulateForces()

    print("Force from proton to electron:\n%s" %proton.force)
    print("Force from electron to proton:\n%s" %electron.force)

if __name__ == '__main__':
    main()
else:
    print("Particle initialization format:\n")
    print("p = particles.Particle(Q, m, v_i, u_i)\n")
    print("where\tv_i = [vi_x, vi_y, vi_z],\n\tu_i = [x_i, y_i, z_i],")
    print("\tand are defined as 3x1 numpy arrays\n\t\te.g. v_i = np.ones([3,1])")

'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
