# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:52:36 2018

@author: rusha
"""

import os
import pandas as pd
import numpy as np

#Setting the path
os.getcwd()
os.chdir("C:/Users/rusha/Desktop/Airbnb")

#Load the csv and create a copy
dc_listings = pd.read_csv("dc_airbnb.csv")
list(dc_listings)
dc_listings1= dc_listings.copy()


#Finding the distance of my house with 3 rooms compared to other houses
dc_listings1["distance"]=abs(dc_listings["accommodates"]-3)
list(dc_listings1["distance"].value_counts())

#Cleaning the price column
dc_listings["price"] = dc_listings["price"].str.replace(",","")
dc_listings["price"] = dc_listings["price"].str.replace("$","").astype("float")
dc_listings1["price"] = dc_listings1["price"].str.replace(",","")
dc_listings1["price"] = dc_listings1["price"].str.replace("$","").astype("float")

dc_listings["price"].describe()

#Finding the mean prices of all the houses with 3 rooms
mean = dc_listings[dc_listings1["distance"]==0]["price"].mean()
mean

#Function that finds the absolute distance for accomodates and finds the predicted price
def get_mean(number_of_rooms,k,dc_listings1):
    dc_listings1["distance"]=abs(dc_listings["accommodates"]-number_of_rooms)
    dc_listings1 = dc_listings1.loc[np.random.permutation(len(dc_listings1))]
    mean = dc_listings1[dc_listings1["distance"]==0]["price"][:k].mean()
    error = (dc_listings1["price"]-mean)**2
    return mean,error.sum()**0.5

print(get_mean(3,5,dc_listings))

#def knn(k,dc_listings1,num_rooms,num_bathrooms):
   # dc_listings1[]=dc_listings1["accommodates"]-num_rooms
    