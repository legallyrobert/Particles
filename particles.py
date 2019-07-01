#! /usr/local/bin/python3
import math

class Particle(object):
    def __init__(self, currentPos, mass, charge):
        self.mass = mass
        self.charge = charge

        # a particle has a current position, dependant on the previous position.
        self.previousPos = currentPos
        self.currentPos  = currentPos

        # a particle has a current velocity, dependant on the previous velocity

        # a particle is non-static by default.
        self.static = False

    def getPos(self, d):
        return self.currentPos[d]
        

class Simulation(object):
    def __init__(self, particle1, particle2):
        self.K = 8.99 * math.pow(10, 9)
        self.p1 = particle1
        self.p2 = particle2

    # get distance between two particles using pythagorean theorem
    def distance(self, p1, p2):
        x = p1.getPos(0) - p2.getPos(0) 
        y = p1.getPos(1) - p2.getPos(1) 
        z = p1.getPos(2) - p2.getPos(2) 

        # magnitude of distance vector \sqrt{x^2 + y^2 + z^2}
        distance = math.sqrt((math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)))

        return distance

    # get force between two particles from Coulomb's Law:
    #   F = kQ1Q2/r^2
    def coulomb(self, particle1, particle2):
        p1 = self.particle1
        p2 = self.particle2
        top = self.K * p1.charge() * p2.charge()
        bottom = math.pow(self.distance(p1, p2), 2)
        F = top/bottom
        distance = math.fabs(self.distance(p1, p2))
        fx = math.fabs(F * ((p1.getPos(0) - p2.getPos(0)/distance)))
        fy = math.fabs(F * ((p1.getPos(1) - p2.getPos(1)/distance)))
        fz = math.fabs(F * ((p1.getPos(2) - p2.getPos(2)/distance)))

        if (p1.charge() * p2.charge()) > 0: #same charges -> repulsive forces
            # particles should accelerate away from each other
            # [fx, fy, fz] should be changed accordingly
            # if p1 coordinates are less than that of p2,
            # make the corresponding force negative to increase the
            # distance between the two particles
            if p1.getPos(0) < p2.getPos(0):
                fx *= -1
            if p1.getPos(1) < p2.getPos(1):
                fy *= -1
            if p1.getPos(2) < p2.getPos(2):
                fz *= -1

        else: # attractive forces
            # particles should accelerate towards each other
            # [fx, fy, fz] should be changed accordingly
            # if p1 coordinates are greater than that of p2,
            # make the orresponding force negative to decrease the
            # distance between the two particles.
            if p1.getPos(0) > p2.getPos(0):
                fx *= -1
            if p1.getPos(1) > p2.getPos(1):
                fy *= -1
            if p1.getPos(2) > p2.getPos(2):
                fz *= -1

        return [fx, fy, fz]

    # returns two forces, that of p1 on p2 and that of p2 on p1
    # e.g. [[p1fx, p1fy, p1fz], [p2fx, p2fy, p2fz]]
    def accumulateForces(self, p1, p2):
        return [self.coulomb(p1,p2), self.coulomb(p2, p1)]

'''
Game plan:
    A particle's delta x per time step is the result of the forces interacting
    between particles. Working backwards:
        We have ma = F = [(k*Q1*Q2)/d^2] ??
        From there, I'm sure we can calculate the velocity yada yada

    Start with distance between two particles in XYZ given by pythagorean theorem?
        done
    Use distance in Coulomb's Law to calculate forces between particles
        done
    Accumulate forces to be used in calculating accelerations of particles?

The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
