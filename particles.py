#! /usr/local/bin/python3
import numpy as np
from scipy import constants as sci


class Particle(object):

    #Coulomb's constant
    K=1/(4*sci.pi*sci.epsilon_0)

    def __init__(self,charge,mass,previousVel,previousPos,static=False):
        self.charge=charge
        self.mass=mass
        self.reducedMass=0

        self.force=np.zeros([1,3])

        self.previousVel=previousVel
        self.currentVel=previousVel

        self.previousPos=previousPos
        self.currentPos=previousPos

        self.static=static   #currently unimplemented

    def d(self,p2):
        return np.subtract(self.currentPos,p2.currentPos)

    def r(self,p2):
        return np.linalg.norm(self.d(p2))

    def r_hat(self,p2):
        return np.divide(self.d(p2),self.r(p2))

    def reduceMasses(self,p2):
        self.reducedMass=p2.reducedMass=\
                np.divide(self.mass*p2.mass,self.mass+p2.mass)

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
        if not self.static:
            tmp=self.currentVel
            self.currentVel=(self.force*t/self.reducedMass+self.previousVel)
            self.previousVel=tmp
        else:
            self.currentVel=self.previousVel

    def updatePosition(self,t):
        if not self.static:
            tmp=self.currentPos
            self.currentPos=(self.currentVel*t+self.previousPos)
            self.previousPos=tmp
        else:
            self.currentPos=self.previousPos

class Simulation(object):
    def __init__(self,p1,p2,time,steps=1000):
        self.p1=p1
        self.p2=p2
        self.time=time
        self.steps=time*1000
        self.timerange=np.linspace(0,time,steps)

    def simulate(self):
        self.p1.reduceMasses(self.p2)

        outfile=open('out.txt','w')

        for i in self.timerange:
            self.p1.accumulateForces(self.p2)
            self.p2.accumulateForces(self.p1)

            self.p1.updateVelocity(i)
            self.p2.updateVelocity(i)

            self.p1.updatePosition(i)
            outfile.write(
                    str(i)+" "+
                    str(self.p1.currentPos[0,0])+" "+
                    str(self.p1.currentPos[0,1])+" "+
                    str(self.p1.currentPos[0,2])+"\n")
            self.p2.updatePosition(i)
            outfile.write(
                    str(i)+" "+
                    str(self.p2.currentPos[0,0])+" "+
                    str(self.p2.currentPos[0,1])+" "+
                    str(self.p2.currentPos[0,2])+"\n")

        outfile.close()


def main():
    #Initial velocity np arrays
    v1=np.array([[0,0,0]])
    v2=np.array([[0.1,0.1,0.1]])

    #Initial position np arrays
    p1=np.array([[0.0,0.0,0.0]])
    p2=np.array([[0.1,0.1,0.1]])

    proton=Particle(sci.e,sci.m_p,v1,p1)
    electron=Particle(-sci.e,sci.m_e,v2,p2)
    
    t=1

    sim=Simulation(proton,electron,t)
    sim.simulate()

    print("Reduced mass of system: ",proton.reducedMass, electron.reducedMass)

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
