# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:04:53 2017

@author: rohit
"""

trialDf = {'Work' : dataset.Work_accident}
trialDf['Work'].astype('category')

X = dataset.iloc[:,[0,1,2,3,4,5,6,7,8]].values