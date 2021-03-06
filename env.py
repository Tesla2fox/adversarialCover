# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:43:14 2018

@author: robot
"""

import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import random
from numpy import *
from copy import *
import copy


class Pnt:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def pnt2dict(self):
        dic = dict(x = x,y= y)
        return dic
    def display(self):
        print('x = ',self.x,'y = ',self.y)

class Circle:
    def __init__(self,pnt = Pnt(),rad = 0):
        self.x = pnt.x
        self.y = pnt.y
        self.rad = rad
        self.x0 = self.x  - self.rad
        self.y0 = self.y  - self.rad
        self.x1 = self.x  + self.rad
        self.y1 = self.y  + self.rad
    def circle2dict(self):
        dic = dict()
        dic['type'] = 'circle'
        dic['xref'] = 'x'
        dic['yref'] = 'y'
        dic['x0'] = self.x0
        dic['y0'] = self.y0
        dic['x1'] = self.x1
        dic['y1'] = self.y1        
        dic['line'] = dict(color = 'rgba(50, 171, 96, 1)')
        return dic
class Line:
    def __init__(self,pnt0 =Pnt(),pnt1=Pnt()):
        self.x0 = pnt0.x
        self.y0 = pnt0.y
        self.x1 = pnt1.x
        self.y1 = pnt1.y
    def line2dict(self):
        dic= dict()
        dic['type']='line'
        dic['x0'] =self.x0
        dic['y0'] =self.y0
        dic['x1'] =self.x1
        dic['y1'] =self.y1
        dic['line'] = dict(color = 'rgb(128, 0, 128)')
        return dic
class Rect:
    def __init__(self,pnt =Pnt(),width =0,height =0):
        self.x0 = pnt.x
        self.y0 = pnt.y
        self.x1 = self.x0 + width
        self.y1 = self.y0 + height
    def rect2dict(self):
        dic = dict()
        dic['type']='rect'
        dic['x0'] = self.x0
        dic['y0'] = self.y0
        dic['x1'] = self.x1
        dic['y1'] = self.y1
        dic['line'] = dict(color = 'rgb(128, 0, 128)')
        return dic

def getLevelColor(level):
    strcolor = 'rgba('
    for i in range(3):
        strcolor = strcolor + str(level*50)+','
    strcolor = strcolor + str(1/level) +')'
    return strcolor    

colorLst = ['white','grey','pink','purple','black']

class Env:
    def __init__(self, mat = zeros((2,2))):
        self.mat = mat
        self.shapeLst = []
        self.drawData = []
    def addTest(self):
        
        pathTrace = go.Scatter(x = [5],
                    y = [5],
                    mode= 'lines',
                    line = dict(shape = 'spline',
                                width = 4),
                    name = 'Path_'+str(i+1))
        self.drawData.append(pathTrace)                    
    def addgrid(self):
        g_color = 'blue'
        row = len(mat)        
        for i in range(row):
            for j in range(len(self.mat[i])):
                pnt = Pnt(i,j)
                rect = Rect(pnt,1,1)
                rectDic = rect.rect2dict()
                rectDic['line']['color'] = g_color
                rectDic['line']['width'] = 0.5
                rectDic['fillcolor'] = colorLst[int(mat[i][j])]
#                getLevelColor(mat[i][j])
                self.shapeLst.append(copy.deepcopy(rectDic)) 
    def drawPic(self,name ='env',fileType = True):
        layout = dict()
        layout['shapes'] = self.shapeLst
        layout['xaxis'] = {'range':[0,len(self.mat[0])]}
        layout['yaxis'] = {'range':[0,len(self.mat)]}
        layout['xaxis'] = dict(
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels = False)
        layout['yaxis'] = dict(
        scaleanchor = "x",
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels = False)
        layout['font'] = dict(
            family='sans-serif',
            size=25,
            color='#000'
        )
        layout['autosize'] = False
        layout['height'] = 1000
        layout['width']= 1000   
#        print(layout)
        fig = dict(data = self.drawData ,layout = layout)
        if(fileType):
            plotly.offline.plot(fig,filename = name)
        else:
            py.image.save_as(fig,filename = name+'.jpeg')
    
        


if __name__ == '__main__':

    row = 10
    col = 10
    
    mat = zeros((row,col))
    proLst = []
    for i in range(5):
        proLst.append(i)
        
    for i in range(row):
        for j in range(col):
            mat[i][j] = random.choice(proLst)

    row = len(mat)
    env = Env(mat)
    env.addgrid()
    env.addTest()
    env.drawPic()