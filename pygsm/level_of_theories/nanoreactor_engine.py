
# standard library imports
import sys
import os
from os import path
import re

# third party
import numpy as np

# local application imports
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))

try:
    from .base_lot import Lot
    from .file_options import File_Options
except:
    from base_lot import Lot
    from file_options import File_Options
from utilities import *

'''
'''

class nanoreactor_engine(Lot):

    def __init__(self,options):
        super(...)

        # can we do a check here?
        engine=options['job_data']['engine']

    def run(self,geom,mult,ad_idx,runtype='gradient'):
        self.Gradients={}
        self.Energies = {}

        xyz = manage_xyz.xyz_to_np(geom)*units.ANGSTROM_TO_BOHR

        # Call the engine
        energy,gradient = self.engine.compute_gradient(xyz)

  
        # Store the values in memory 
        self._Energies = self.Energy(energy,'Hartree')
        self._Gradients = self.Gradient(gradient,'Hartree/Bohr')


if __name__=="__main__":
    from nanoreactor.engine import get_engine                      
    from nanoreactor.parsing import load_settings_from_args
    from nanoreactor.engine import TCPBEngine


    # read settings from name
    db, setting_name, settings = load_settings_from_args(kind='refine', create=False,  
              description='Refining reactions paths.')

    # Create the nanoreactor TCPB engine
    engine_type=settings['engine'].pop('type')
    engine = get_engine(r.mol, engine_type=engine_type, **settings['engine'])

    
    # read in a geometry
    geom = manage_xyz.read_xyz('../../data/ethylene.xyz')
    xyz = manage_xyz.xyz_to_np(geom)
    
    # create the pygsm level of theory object
    test_lot = nanoreactor_engine(geom,job_data = {'engine',test_engine})

    # Test
    print("getting energy")
    print(test_lot.get_energy(xyz,1,0))

    print("getting grad")
    print(test_lot.get_gradient(xyz,1,0))


    
