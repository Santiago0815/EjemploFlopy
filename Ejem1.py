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
    sim_name=name, exe_name="C:/Users/PERSONAL/Diplomado/mf6", version="mf6", sim_ws="workspace"
)
#busca mf6 en la carpeta especificada y guarda los archivos

tdis = flopy.mf6.ModflowTdis(
    sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)]
)
#crear objetos de flopy TDIS

ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")
#crear el paquete de objetos de flopy IMS

model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)
#crea el modelo de flujo de agua

"""
Created on Mon Jan 25 15:35:07 2021

@author: PERSONAL
"""

