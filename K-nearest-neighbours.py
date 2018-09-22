# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:52:36 2018

@author: rusha
"""

import os
import pandas as pd
os.getcwd()
os.chdir("C:/Users/rusha/Desktop/Airbnb")
df = pd.read_csv("dc_airbnb.csv")
df
df.info()

