# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:09:03 2015

@author: andre-jan
"""


import math as m

import Const as C


def cartesian_to_geodetic(point , jd):
    
    #Determine angle between the vernal equinox and the Greenwhich Meridian
    UT = m.fmod(jd + 0.5, 1.0)
    T = (jd - UT - 2451545.0) / 36525.0;
    omega = 1.0 + 8640184.812866 / 3155760000.0;
    gmst0 = 24110.548412 + T * (8640184.812866 + T * (0.093104 - T * 6.2E-6));
    theta_GMST = m.fmod(gmst0 + 86400.0 * omega * UT, 86400.0) * 2 * m.pi / 86400.0;
    
    #Setup coordinates to better illustrate calculations
    x , y , z = point[0] , point[1] , point[2]
    e = 0.081819190842622
    a = 6378.137  #Earths semi major axis
    
    #Calculate the geodetic longitude(radians)
    longitude = m.fmod( (m.atan2(y , x) - theta_GMST) , 2*m.pi)   
    
    #Calculate the geodetic latitude using an iterative method(radians)    
    latitude = m.atan2( z , m.sqrt(x*x + y*y))
     
    iters = 0
    latitudeOld = latitude
     
    while( (m.fabs(latitude - latitudeOld) < 1.0e-10) or iters == 0):   
    
         latitudeOld = latitude
         c = a * e * e * m.sin(latitudeOld) / m.sqrt( 1.0 - e * e * m.sin(latitudeOld) * m.sin(latitudeOld))
         latitude = m.atan2( ( z + c ) , m.sqrt(x*x + y*y) )
         iters = iters + 1
    
     
    print "Iterations needed for answers => " , iters
    
    
    altitude = m.sqrt(x*x + y*y)/m.cos(latitude) - a/m.sqrt(1 - e*e*m.sin(latitude)*m.sin(latitude))
    
    print "Longitude" , C.r2d(longitude)
    print "Latitude" , C.r2d(latitude)
    print "altitude" , altitude
    
    return latitude , longitude , altitude
    
    
def generate_TLE_set(alt , incl , meanAno , raan , argOfPeri , ecco , n , epoch_yr , epoch_days):
   
    #Define the first string   
    s = "1"
    s = s + ' ' + "25544U" #Satellite number - unused
    s = s + ' ' + "98067A   " #Launch Information - not used
    
    #Use "2013/01/01 00:00:00" as the reference epoch
    s = s +  str(epoch_yr) + str(epoch_days)
    s = s + " -.00002182" #First derivative of mean motion - hopefully unimportant
    s = s + "  00000-0 "
    s = s + "-00000-0" #B-Star Drag Term - Zeroed
    s = s + " 0"
    s = s + "  292" #Element Set Number
    s = s + "7" #Checksum 
    
    l1 = s
    
    print l1
    
    s = "2"
    s = s + " 25544 " #Append Satellite Number
    
    #Must be of format NNN.NNNN
    c = "{0:.4f}".format(C.r2d(incl)).rstrip("0") 
    
    print "c for incl" , c
    
    while( len(c) != 8):
       if(len(c) > 4 and c[3] != '.'):
           c = "0" + c
       else:
           c = c + "0"
    
    
    s = s + c
    s = s + " "
    
    c = "{0:.4f}".format(C.r2d(raan)).rstrip("0")
    
    print 'c for raan' , c
    
    while( len(c) != 8):
       if(len(c) > 4 and c[3] != '.'):
           c = "0" + c
       else:
           c = c + "0"
    
    
    s = s + c
 
    
    '''
    while( len(e) != 8):
       if(len(e) > 6 and e[3] != '.'):
           e = '0' + e
           e.replace(" " , '0')
           e.replace(" " , "")
       else:
           e = e + "0"
    e.replace(' ' , '0')
    
    
    l = len(c)
    for x in xrange(0 , l):
        if c[x] == '.':
            i = x
        
        
    for x in xrange(0 ,4 - i):
    
        c = '%d%s'  % (0, c)

    
    #Must be of format NNN.NNNN    
    while( len(c) <= 9):
           c = c + str(0) 
    '''

          
  
    
    c = str(int(ecco*m.pow(10,7))) 
    
    if(len(c) != 7):
        
        c = c.zfill(7)
        
    s = s + " " +  c + " "
    
    c = "{0:4f}".format(C.r2d(argOfPeri)).rstrip("0")  
    
    while( len(c) != 8):
       if(len(c) > 4 and c[3] != '.'):
           c = "0" + c
       else:
           c = c + "0"
    
    
    
    
    s = s + c
    
    c = " {0:4f}".format((meanAno)).rstrip("0")
    
    while( len(c) != 9):
           c = c + "0"
    
    
    s = s + c
    
    c = "{0:10f}".format(n)
    
    while( len(c) != 12):
           c = c + "0"
    
    s = s + c
    s = s + "56353" #Revolution Number - not used
    s = s + "7" #Checksum
    
    l2 = s
    
    print l2
    
    return l1 , l2
        
    
    
    