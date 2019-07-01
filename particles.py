#! /usr/local/bin/python3

import numpy as np

class Particle(object):
    def __init__(self, currentPos, currentVel, mass, charge):
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

'''
The Universe is where the simulation takes place.
I think it will be in a cube of N size with centerpoint around [0,0,0] in 3D plot

class Universe(object):
    def __init__(self, ..., ):

    def collisions(self, currentPos?):
        if xpos == maxsize || xpos == 0:
            xvel = -xvel
        if ypos == maxsize || ypos == 0:
            yvel = -yvel
        if zpos == maxsize || zpos == 0:
            zvel = -zvel
    # collision checking has to run per time step, after position is updated

'''


'''
The simulation will be visualized using a 3D plot
    e.g. ./simple_3danim.py,
    from https://matplotlib.org/1.4.2/examples/animation/simple_3danim.html
'''


'''
The System is the implementation of physics on Particles in the Universe
I'm still not sure about what all to put here:
  Time stepping?
  Force accumulation?


Game plan:
    A particle's delta x per time step is the result of the forces interacting
    between particles. Working backwards:
        We have ma = F = [(k*Q1*Q2)/d^2] ??
        From there, I'm sure we can calculate the velocity yada yada


class System(Universe):
    def __init__(self, ..., ):
    
'''
