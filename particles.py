#! /usr/local/bin/python3
import numpy as np
from scipy import constants as sci

class Particle(object):

    #Coulomb's constant
    K=1/(4*sci.pi*sci.epsilon_0)

    def __init__(self,charge,mass,initialVel,initialPos):
        self.charge=charge
        self.mass=mass

        self.force=np.zeros([3,1])

        self.initialVel=initialVel
        self.currentVel=initialVel

        self.initialPos=initialPos
        self.currentPos=initialPos

        self.static=False   #currently unimplemented

    def d(self, p2):
        return np.subtract(self.currentPos,p2.currentPos)

    def r(self, p2):
        return np.linalg.norm(self.d(p2))

    def r_hat(self, p2):
        return np.divide(self.d(p2),self.r(p2))

    def coulomb(self, p2):
        top=(self.K*self.charge*p2.charge*(
            self.r_hat(p2)
            /self.r(p2))
            )
        bottom=np.power(self.r(p2),2)

        self.force=top/bottom

    def magnetism(self, p2):
        top=(sci.mu_0*self.charge*np.cross(
            self.currentVel,
            self.r_hat(p2)/self.r(p2),
            axis=0
            ))
        bottom=(4*sci.pi*np.power(self.r(p2),2))
        B=top/bottom

        F=(self.charge*np.cross(
            self.currentVel,
            B,
            axis=0
            ))

        self.force=np.add(self.force,F)

    def accumulateForces(self, p2):
        self.coulomb(p2)
        self.magnetism(p2)
        return self.force


'''
class Simulation(object):
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

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
    v1,v2 = np.zeros([3,1]),np.zeros([3,1])

    #Initial position np arrays
    p1,p2 = np.zeros([3,1]),np.zeros([3,1])

    #Set velocity
    v1[0] = 1
    #Set position
    p1[0] = 1

    proton   = Particle(sci.e, sci.m_p, v1, p1)
    electron = Particle(-sci.e, sci.m_e, v2, p2)
    
    print("Force from proton to electron:\n%s"
            %proton.accumulateForces(electron))
    print("Force from electron to proton:\n%s"
        %electron.accumulateForces(proton))

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
