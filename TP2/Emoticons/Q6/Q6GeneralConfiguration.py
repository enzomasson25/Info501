# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q5Emoticon import Emoticon
from Q5Button import Button


class GeneralConfiguration:
    # Constructor
    def __init__(self) :
        self.initPygame()
        
        # Parameters for the emoticons        
        self.emoticonSize = 400
        self.emoticonBorder = 20  
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
                
        # Sensors list
        self.sensors = []
        
        self.selectedSensor = 0
        
    #getters
    def getScreen(self):
        return self.screen
    
    def getButtonWidth(self):
        return self.buttonWidth
    
    def getButtonHeight(self):
        return self.buttonHeight

    def getEmoticonSize(self):
        return self.emoticonSize
    
    def getEmoticonBorder(self):
        return self.emoticonBorder
    
    def getSensors(self):
        return self.sensors
    
    def getSelectedSensor(self): 
        return self.selectedSensor 
    
    #Retourne la largeur de la surface de dessin
    def get_width(self):
        return self.screen.get_width()
    #Retourne la hauteur de  la surface de dessin
    def get_height(self):
        return self.screen.get_height()
        
    # Initializes pygame        
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface()         
        
    # Getters
    # Compléter avec les Getters de la question Q1.4

        
    # Adds a sensor    
    def addSensor(self, sensor):
        #chaque sensor est composé d'un id, d'un emoticon et d'un button
        sensor.setGeneralConfiguration(self)
        sensor.setSensorId(len(self.sensors)) #id créer grâce à la liste sensors
        sensor.setEmoticon(Emoticon(sensor)) #emoticon
        sensor.setButton(Button(sensor)) #button
        self.sensors.append(sensor)
 
    # Retrieves the sensor id from a posiiion
    def positionToSensorId(self, position):
        for sensor in self.sensors:
            cg=sensor.button.getPosition()
            if position[0]>cg[0] and position[0]<cg[0]+self.buttonWidth:
                if position[1]>0 and position[1]<self.buttonHeight:
                    return sensor.getSensorId()
        return None

    # Checks if the display of a new sensor was requested
    def checkIfSensorChanged(self, eventPosition):
        if self.selectedSensor!=self.positionToSensorId(eventPosition) and self.positionToSensorId(eventPosition)!=None:
            self.selectedSensor=self.positionToSensorId(eventPosition)
    
    #calcul le nombre de button maximum par ligne en divisant la taille de la fenêtre par la taille d'un bouton 
    def maxButtonsPerLine(self):
        return self.get_width//self.buttonWidth
    

    #Calcul le nombre de boutons sur une ligne passée en paramètre
    def buttonsCountOnLine(self, line):
        ligne_compl=len(self.sensors)//self.maxButtonsPerLine() #le nombre de ligne qui sont complètes 
        if line <= ligne_compl: #si la ligne demandée est inférieur au nombre de ligne complète
            return self.maxButtonsPerLine() # alors cette ligne est complète donc on retourne le maximum qu'on peut avoir de bouton sur une ligne
        elif len(self.sensors)%self.maxButtonsPerLine()!=0 and line=ligne_compl+1: #si la ligne on nous demande la ligne qui suit la dernière ligne complète
            return (len(self.sensors))-ligne_compl*self.maxButtonsPerLine() #on calcul le nombre de bouton sur cette ligne
        else #si on nous demande une autre ligne
            return 0 #elle est vide donc on retourne 0
            
    
    # Draws on pygame screen      
    def draw(self):
        # Clears the surface
        pygame.display.get_surface().fill([0, 0, 0])
        #drawEmoticon
        self.sensors[self.selectedSensor].drawEmoticon()
        #drawButton
        for sensor in self.sensors:
            sensor.drawButton()
            
    # Displays   
    def display(self):
        # Draws on the screen surface
        self.draw()
        
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
               