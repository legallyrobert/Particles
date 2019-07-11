#! /usr/local/bin/python3
import numpy as np
from scipy import constants as sci


class Particle(object):

    #Coulomb's constant
    K=1/(4*sci.pi*sci.epsilon_0)

    def __init__(self,charge,mass,previousVel,previousPos):
        self.charge=charge
        self.mass=mass

        self.force=np.zeros([1,3])

        self.previousVel=previousVel
        self.currentVel=previousVel

        self.previousPos=previousPos
        self.currentPos=previousPos

        self.static=False   #currently unimplemented

    def d(self,p2):
        return np.subtract(self.currentPos,p2.currentPos)

    def r(self,p2):
        return np.linalg.norm(self.d(p2))

    def r_hat(self,p2):
        return np.divide(self.d(p2),self.r(p2))

    def coulomb(self,p2):
        top=(self.K*self.charge*p2.charge*(
            self.r_hat(p2)
            /self.r(p2))
            )
        bottom=np.power(self.r(p2),2)

        self.force=top/bottom

    def magnetism(self,p2):
        top=(sci.mu_0*self.charge*np.cross(
            self.currentVel,
            self.r_hat(p2),
            axis=1
            ))
        bottom=(4*sci.pi*np.power(self.r(p2),2))
        B=top/bottom

        F=(p2.charge*np.cross(
            p2.currentVel,
            B,
            axis=1
            ))

        p2.force=np.add(p2.force,F)

    def accumulateForces(self,p2):
        self.coulomb(p2)
        self.magnetism(p2)
        return self.force

    def updateVelocity(self,t):
        tmp=self.currentVel
        self.currentVel=(self.force*t/self.mass+self.previousVel)
        self.previousVel=tmp

    def updatePosition(self,t):
        tmp=self.currentPos
        self.currentPos=(self.currentVel*t+self.previousPos)
        self.previousPos=tmp

class Simulation(object):
    def __init__(self,p1,p2,time,steps=1000):
        self.p1=p1
        self.p2=p2
        self.time=time
        self.steps=time*1000
        self.timerange=np.linspace(0,time,steps)

    def simulate(self):
        for i in self.timerange:
            self.p1.accumulateForces(self.p2)
            self.p2.accumulateForces(self.p1)

            self.p1.updateVelocity(i)
            self.p2.updateVelocity(i)

            self.p1.updatePosition(i)
            self.p2.updatePosition(i)


def main():
    #Initial velocity np arrays
    v1=np.array([[1,2,0]])
    v2=np.array([[-3,0,1]])

    #Initial position np arrays
    p1=np.array([[0.1,-0.2,0.4]])
    p2=np.array([[0.0,0.0,0.0]])

    proton=Particle(sci.e,sci.m_p,v1,p1)
    electron=Particle(-sci.e,sci.m_e,v2,p2)
    
    t=2

    sim=Simulation(proton,electron,t)
    sim.simulate()

    print("After",sim.steps,"iterations over",t,"seconds:")
    print("Final position of proton   ",proton.currentPos)
    print("Final position of electron ",electron.currentPos)

if __name__ == '__main__':
    main()

'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
