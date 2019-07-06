#! /usr/local/bin/python3
import math

class Particle(object):
    def __init__(self, charge, mass, force, initialVel, initialPos):
        self.charge = charge
        self.mass = mass

        self.force = force

        # a particle has a current velocity, dependant on the previous velocity
        self.initialVel = initialVel
        self.currentVel = initialVel

        # a particle has a current position, dependant on the previous position.
        self.initialPos = initialPos
        self.currentPos = initialPos

        # a particle is non-static by default.
        self.static = False


class Simulation(object):
    def __init__(self, particle1, particle2):
        self.K = 8.99 * math.pow(10, 9)
        self.p1 = particle1
        self.p2 = particle2

    # get distance between two particles using pythagorean theorem
    def distance(self, p1, p2):
        x = p1.currentPos[0] - p2.currentPos[0] 
        y = p1.currentPos[1] - p2.currentPos[1] 
        z = p1.currentPos[2] - p2.currentPos[2] 

        # magnitude of distance vector \sqrt{x^2 + y^2 + z^2}
        distance = math.sqrt((math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)))

        return distance

    # get force between two particles from Coulomb's Law:
    #   F = kQ1Q2/r^2
    def coulomb(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        top = self.K * p1.charge * p2.charge
        bottom = math.pow(self.distance(p1, p2), 3) # changed to third power from second
        F = top/bottom

        fx = math.fabs(F * (p1.currentPos[0] - p2.currentPos[0]))
        fy = math.fabs(F * (p1.currentPos[1] - p2.currentPos[1]))
        fz = math.fabs(F * (p1.currentPos[2] - p2.currentPos[2]))

        p1.force = [fx, fy, fz]
        return p1.force

    def velocity(self, particle):
        # velocity vector = (force vector * time step)/mass + initial velocity vector
        self.particle = particle
        vx = ((particle.forces[0]*TIMESTEP)/particle.mass)+particle.initialVel[0]
        vy = ((particle.forces[1]*TIMESTEP)/particle.mass)+particle.initialVel[1]
        vz = ((particle.forces[2]*TIMESTEP)/particle.mass)+particle.initialVel[2]

        particle.currentVel = [vx, vy, vz]
        return particle.currentVel 

    def updatePosition(self, particle):
        self.particle = particle
        dx = particle.currentVel[0] * TIMESTEP
        dy = particle.currentVel[1] * TIMESTEP
        dz = particle.currentVel[2] * TIMESTEP
        # might be dumb but where to go from here? it's 3:45AM and i'm sleepy


    # returns two forces, that of p1 on p2 and that of p2 on p1
    # e.g. [[p1fx, p1fy, p1fz], [p2fx, p2fy, p2fz]]
    def accumulateForces(self, p1, p2):
        return [self.coulomb(p1,p2), self.coulomb(p2, p1)]

'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
