# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:45:38 2015

@author: andre-jan

This file contains a large number of constants which are often used by various
programs. 

Defining them here prevents any magic number trends and also allows to easily 
verify the results of changing one specific simulation parameter.

If any constants are linked ONLY to specific assumptions, the are grouped
accordingly.

"""

import math

'''
Sphecial Earth Constants
'''

AVG_RAD = 6378136.6 #Average Radius of the Earth in Meters. 

'''
Elipsoid Earth Constants
'''

POL_RAD =  6356752.3 #Average Radius of the Earth from center to the Poles in m
EQR_RAD =  6378137.0 #Average Radius of the Earth from center to the Poles in m

'''
Angle Transformations
'''
def d2r(angle):
    
    return angle * math.pi / 180
    
def r2d(angle):
    
    return angle * 180 / math.pi
    

'''
Coordinate Transformations

This declares the transformation needed to convert between Earth-Centered
Cartesian Coordiantes (x , y , z ) and Geodetic Coordinates ( lat , long, height) 
'''




    
