# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:19:14 2020

@author: wyue
"""


# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.p", "wb" ) )
