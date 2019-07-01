#! /usr/local/bin/python3

import numpy as np
import math

class Particle(object):
    def __init__(self, currentPos, mass, charge):
        # a particle has a static mass:
        self.mass = mass

        # a particle has a charge [positive: 1, negative: -1]:
        self.charge = charge

        # a particle has a current position, dependant on the previous position.
        # represented as a numpy array for easy cross products, vector additions
        self.previousPos = currentPos
        self.currentPos  = currentPos
        self.futurePos   = currentPos

        # a particle has a current velocity, dependant on the previous velocity

        # a particle is non-static by default.
        self.static = False

class Simulation(object):
    def __init__(self, particle1, particle2):
        self.K = 8.99 * math.pow(10, 9)
        self.p1 = particle1
        self.p2 = particle2

    # get distance between two particles using pythagorean theorem
    def distances(self, pos1, pos2):
        x = pos1[0] - pos2[0]
        y = pos1[1] - pos2[1]
        z = pos1[2] - pos2[2]

        distance = math.sqrt((math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)))

        return distance

    # get force between two particles from Coulomb's Law:
    #   F = kQ1Q2/r^2
    def coulomb(self, particle1, particle2):
        p1 = self.particle1
        p2 = self.particle2
        top = self.K * p1.charge() * p2.charge()
        bottom = math.pow(self.distances(p1.currentPos(), p2.currentPos()), 2)
        F = top/bottom



'''
    # need a collisions checker for simulating with boundaries
    def collisions(self, currentPos?):
        if xpos == maxsize || xpos == 0:
            xvel = -xvel
        if ypos == maxsize || ypos == 0:
            yvel = -yvel
        if zpos == maxsize || zpos == 0:
            zvel = -zvel
    # collision checking has to run per time step, after position is updated

Game plan:


    A particle's delta x per time step is the result of the forces interacting
    between particles. Working backwards:
        We have ma = F = [(k*Q1*Q2)/d^2] ??
        From there, I'm sure we can calculate the velocity yada yada

    Start with distance between two particles in XYZ given by pythagorean theorem?
        done
'''


'''
The simulation will be visualized using a 3D plot at a later time
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''
