import numpy as np
from random import randint
from math import sqrt, pi
from Constants import *

class Particle:

    def __init__(self):

        """



        """


        self._position = np.array([
                float(randint(0,HEIGHT),
                float(randint(0,WIDTH))
             ])

        self._velocity = np.array([0.0,0.0])
        self._radius = 2
        self._setMass()
        self._merged = False

    def _resetAcceleration(self):

        self._acceleration = np.array([0.0,0.0])

    def _updateAcceleration(self, particle):

        """

        :param particle: Calculates the acceleration contribution
                         from another particle
        :return:
        """

        dr = particle._position - self._position
        dsq = dr[0]**2 + dr[1]**2
        magnitude = sqrt(dsq)
        force = GRAVITY*self._mass*particle._mass/dsq if dsq>1e-10 else 0
        self._acceleration[0] += force*dr[0]/magnitude
        self._acceleration[1] += force*dr[1]/magnitude

    def updatePosition(self):
        self.position += self._velocity
        self._velocity += self._acceleration
        self._resetAcceleration()

    def _setMass(self):

        self._mass = (DENSITY * 4.0 * pi * (self._radius**3.0)/3)

    def _setRadius(self):

        self._radius = (3.0 * self._mass/(DENSITY * 4.0 * pi))**(0.333333)

    def _contact(self, p1, p2):
        dr = p1-p2
        dsq = (p1[0]*p2[0] + p1[1]*p2[1])
        magnitude = sqrt(dsq)
        return magnitude <= (p1._radius + p2._radius)

