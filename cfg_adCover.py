# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:28:50 2018

@author: robot
"""


import random
from numpy import *

row = 10
col = 10

mat = zeros((row,col))
proLst = []
for i in range(5):
    proLst.append(0.2*i)
    
for i in range(row):
    for j in range(col):
        mat[i][j] = random.choice(proLst)




print(mat)        
    