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

        self.static=static

    def r_vec(self,p2):
        return np.subtract(self.currentPos,p2.currentPos)

    def r(self,p2):
        return np.linalg.norm(self.r_vec(p2))

    def r_hat(self,p2):
        return np.divide(self.r_vec(p2),self.r(p2))

    def reduceMasses(self,p2):
        self.reducedMass=p2.reducedMass=\
                np.divide(self.mass*p2.mass,self.mass+p2.mass)
        return self.reducedMass

    def coulomb(self,p2):
        top=(self.K*self.charge*p2.charge*self.r_hat(p2))
        bottom=np.power(self.r(p2),2)

        return top/bottom

    def magnetism(self,p2):
        top=(sci.mu_0*p2.charge*np.cross(
            p2.currentVel,
            self.r_hat(p2)
            ))
        bottom=(4*sci.pi*np.power(self.r(p2),2))
        B=top/bottom

        F=(self.charge*np.cross(
            self.currentVel,
            B
            ))

        return F

    def accumulateForces(self,p2):
        self.force=self.coulomb(p2)+self.magnetism(p2)
        return self.force
        #POSSIBLE ISSUE: force of magnetism seems negligible ???

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
        self.timestep=self.timerange[1]

    def simulate(self):
        self.p1.reduceMasses(self.p2)
        self.p2.reduceMasses(self.p1)

        outfile=open('out.txt','w')

        for i in self.timerange:
            self.p1.accumulateForces(self.p2)
            self.p2.accumulateForces(self.p1)

            self.p1.updateVelocity(self.timestep)
            self.p2.updateVelocity(self.timestep)

            self.p1.updatePosition(self.timestep)
            outfile.write(
                    str(i)+" "+
                    str(self.p1.currentPos[0,0])+" "+
                    str(self.p1.currentPos[0,1])+" "+
                    str(self.p1.currentPos[0,2])+"\n")
            self.p2.updatePosition(self.timestep)
            outfile.write(
                    str(i)+" "+
                    str(self.p2.currentPos[0,0])+" "+
                    str(self.p2.currentPos[0,1])+" "+
                    str(self.p2.currentPos[0,2])+"\n")

        outfile.close()


def main():
    #Initial velocity np arrays
    v1 = np.array([[1.0,1.0,1.0]])
    v2 = np.array([[-1.,-1.,-1.]])

    #Initial position np arrays
    p1 = np.array([[0.07234652,0.09779895,0.05384959]])
    p2 = np.array([[0.09992369,0.09922008,0.09956159]])
    
    proton=Particle(sci.e,sci.m_p,v1,p1)
    electron=Particle(-sci.e,sci.m_e,v2,p2)
    
    t=.005

    sim=Simulation(proton,electron,t,1000)
    sim.simulate()

    print("pos_f, proton\n",proton.currentPos)
    print("pos_f, electron\n",electron.currentPos)

if __name__ == '__main__':
    main()

'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
