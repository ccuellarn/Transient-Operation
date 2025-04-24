from flask import Flask, render_template, request
from datetime import datetime
import numpy as np
import pandas as pd
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is a planner for astronomical observations'

if __name__ == '__main__':
    app.run()