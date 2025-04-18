#! /bin/env/python3 # for our *nix friends

# Nuerolux class definitions
#
# Defines the classes and the methods for cardiac, respiratory, and activity data
# The goal is to keep the example Jupyter file easy to read for everyone

# ---------------------------
# Imports
# ---------------------------
# start with our friendly neighborhood data analysis packages
import numpy as np
import pandas as pd
import math
from scipy import signal
from scipy.signal import savgol_filter
from scipy.interpolate import CubicSpline

# OS and file manipulation tools
import platform
from pathlib import Path
from glob import glob
import psutil
from tkinter import filedialog, Tk
from typing import NamedTuple, Tuple

# plotting tools
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.dates as md
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Slider

# other handy stuff
from datetime import datetime, timedelta



# ---------------------------
# Parameter structure
# ---------------------------
class paramstruct(NamedTuple):
    '''
    Parameters for loading all of the data from the experiment
    
    Fields:
        fs: int                 : sampling frequency (Hz)
        total_time: float       : the total time of the experiment. This will be taken care of when the file is loaded
        
        vital_w: int            : vital sign calculation window in seconds
        vital_ovlp: float       : fraction of window overlapped - 1 is complete, 0 is none - flipped from initial code (0.25)
        hs_freq: tuple          : heart sound Band Pass Filter frequencies (Hz) (25, 390)
        hs_len: float           : maximum heart sound length (seconds) [0.165] (Luisada, Mendoza, Alimurung 1948)
        hs_thresh: tuple        : heart sound magnitude thresholds, post normalization (1E-5, 0.3)
        hr_range: tuple         : minimum and maximum expected heart rate (Hz) (400, 900)
        act_thresh: tuple       : activity Band Pass Filter frequencies (Hz) (1E-5, 0.5)
        min_scale: int          : 
        max_scale: int          : 
        min_scale_resp: int     :
        max_scale_resp: int     :
        fs_ds: int              : downsampled sample rate

        resp_freq: tuple        : respiratory frequency (Hz) (1.25, 3.0) (original??)
        resp_axis: str          : axis of IMU to use for respiration data ('x')
        ds_resp: int            : respiration downsampling sample rate
        fs_resp: int            : not sure. initial respiration fs? 
        resp_pk_ht: float       : Max height for respiration signal (None)
        resp_pk_prom: float     : respiration peak minimium prominence (2E-5)
        resp_pk_w               : None
        resp_pk_wlen            : None

        xconn_len: int          : disconnection length threshold before splitting into new chunk (ms) (1000)
        min_chunk: float        : minimum chunk length. Shorter chunks will be discarded (s) (60)
    
    '''

    # parameters for the entire experiment
    fs: int
    total_time: float
    # HR Parameters
    vital_w: int
    vital_ovlp: float
    hs_range: tuple
    hs_len: float
    hr_freq: tuple
    hs_thresh: tuple
    activity_thresh: tuple
    min_scale: int
    max_scale: int
    min_scale_resp: int
    max_scale_resp: int
    fs_ds: int
    resp_freq: tuple 
    resp_axis: str      
    ds_resp: int        
    fs_resp: int        
    resp_pk_ht: float   
    resp_pk_prom: float 
    resp_pk_w: None
    resp_pk_wlen: None

    xconn_len: intas
    min_chunk: float


    def init(self, fs:int = 2000, total_time: float = 0, vital_w:int = 4,
             vital_ovlp:float = 0.25, hs_freq:tuple[int, int] = (25, 390), 
             hs_len:float = 0.165, hs_thresh:tuple[float,float] = (1E-5, 0.3),
             hr_range:tuple[float, float] = (400, 900), 
             act_thresh:tuple[float,float] = (1E-5, 0.5), resp_freq:tuple[float, float] = (1.25, 3.0),
             resp_axis:str = 'x', ds_resp:float = 50., resp_pk_ht = None, 
             resp_pk_prom:float = 1E-5, resp_pk_w = None, resp_pk_wlen = None, xconn_len = ssda)









# ---------------------------
# Cardiac
# ---------------------------














# ---------------------------
# Respiration
# ---------------------------











# ---------------------------
# Activity
# ---------------------------