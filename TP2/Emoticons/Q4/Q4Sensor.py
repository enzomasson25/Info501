# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib
import ssl

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label 
        self.thresholds = thresholds
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getLabel(self):
        return self.label
                     
    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):        
        try:
            self.request = urllib.request.urlopen(url=self.url, context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH))
        except OSError:
            return False
        else: 
            return self.request.getcode() == http.HTTPStatus.OK

    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None
            
    # Gets the transformed value
    def getTransformedValue(self): #on décompose le problème de 2 parties et on gère les maximums/minimums à la fin
        val=float(self.read())
        #On calcul les pas 
        pas_inf=(1/(self.thresholds[1]-self.thresholds[0]))*100
        pas_sup=(1/(self.thresholds[2]-self.thresholds[1]))*100
        
        if val>self.thresholds[1]: #Entre 0 et 1
            res=val/pas_sup
            
        if val<self.thresholds[1]: #Entre -1 et 0
            res=-val/pas_inf
            
        if val>self.thresholds[2]: #Maximum
            res=1
        if val<self.thresholds[0]: #Minimum
            res=-1
            
        return res
            
            
            
            
            
        
            
                   
        