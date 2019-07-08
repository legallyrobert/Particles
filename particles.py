#! /usr/local/bin/python3
import math

class Particle(object):
    def __init__(self,charge,mass,initialVel,initialPos):
        self.charge=charge
        self.mass=mass

        self.force=[0,0,0] # determined and replaced by Simulation.forces()

        self.initialVel=initialVel
        self.currentVel=initialVel

        self.initialPos=initialPos
        self.currentPos=initialPos

        self.static=False

class Simulation(object):
    def __init__(self,p1,p2):
        self.K=8.99*math.pow(10,9)
        self.p1=p1
        self.p2=p2

    def distance(self, p1, p2):
        x=self.p1.currentPos[0]-self.p2.currentPos[0]
        y=self.p1.currentPos[1]-self.p2.currentPos[1]
        z=self.p1.currentPos[2]-self.p2.currentPos[2]

        return math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))

    def forces(self):
        top=self.K*self.p1.charge*self.p2.charge
        bottom=math.pow(self.distance(self.p1,self.p2),3)#changed to third power from second
        F=top/bottom

        for i in range(0,3):
            self.p1.force[i]=(
                    math.fabs(
                        F*(
                            self.p1.currentPos[i]
                            -self.p2.currentPos[i]
                            )
                        )
                    )

        self.p2.force=[-x for x in self.p1.force]

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
    # standard electric charge of proton, -e for electron
    e = 1.602*math.pow(10, -19)

    proton   = Particle(e, 1.6726219*math.pow(10, -27), [0,0,0], [1,0,0])
    electron = Particle(-e, 9.10938356*math.pow(10, -31), [0,0,0], [0,0,0])
    
    simulation = Simulation(proton, electron)
    simulation.forces()

    print("Force from proton to electron: %s" %proton.force)
    print("Force from electron to proton: %s" %electron.force)

if __name__ == '__main__':
    main()

'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
