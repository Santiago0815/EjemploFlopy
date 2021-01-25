import os
import numpy as np
import matplotlib.pyplot as plt
import flopy
# -*- coding: utf-8 -*-
name = "tutorial1"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name="mf6", version="mf6", sim_ws="."
)

"""
Created on Mon Jan 25 15:35:07 2021

@author: PERSONAL
"""

