#!/usr/bin/python

import sys
import os
import unittest

# get parent directory name to import module to be tested
parentdir = os.path.abspath(os.pardir)
#sys.path.append(parentdir)

# Import from installed/checked-out package
from pserpoppy.population import Population


# not sure yet that population needs much testing... it's so simple
class testPopulation(unittest.TestCase):
    def setUp(self):
        self.population = Population()
