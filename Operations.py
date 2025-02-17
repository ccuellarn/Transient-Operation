#-*- coding: utf-8 -*-
"""
@author: Clauwn
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy import constants as C
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
from astropy import units as u

#Convert the DMS format to degrees
def ConvertLaLo(l):
    l_ = l.split('-')
    D = float(l_[0])
    M = float(l_[1])
    S = float(l_[2])
    dir = l_[3]
    r = D + (M/60) + (S/3600)
    if dir=='W' or dir=='S':
        return r*(-1)
    else:
        return r

def Observations(longitude, latitude, RA, DEC, Date):
    time_obs = Time(Date)
    lat_conv = ConvertLaLo(latitude)
    lon_conv = ConvertLaLo(longitude)
    observer = EarthLocation(lat=lat_conv*u.deg, lon=lon_conv*u.deg)
    Conditionals = []

    for i in range(0,len(RA)):

        celestial_coord = SkyCoord(ra=RA[i], dec=DEC[i]) #mantain the degrees units

        # Calculate the coordenates AltAz for the time and observer
        frame_altaz = AltAz(obstime=time_obs, location=observer)
        altaz_coord = celestial_coord.transform_to(frame_altaz) #Transform for the J200 coordinate system for altaz
    
        # Determinate if its observable (altitude > 0 degrees), return a boolean
        Conditionals.append(altaz_coord.alt > 0*u.deg)

    #Put everything on a dataframe in the format for better reading
    Data = pd.DataFrame([])
    Data.style.set_caption(Date)
    Data['Observable'] = Conditionals
    Data['RA'] = RA
    Data['Dec'] = DEC

    return Data

