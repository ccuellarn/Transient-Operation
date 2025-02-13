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

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """
    Recibirá el nombre del archivo del cual se realizará el análisis para cargar los datos
    en un formato que permita el programa.
    ----------
    PARÁMETROS:
    nombre_archivo : str
        nombre del arcivo con el formato: 'nombre.csv'. 
    -------
    
    Retorna el DataFrame del archivo.
    """
    datos = nombre_archivo
    return datos

