# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame     
        
class Button: 
    # Constructor      
    def __init__(self, sensor) :
        self.sensor = sensor
        
    # Gets the sensor position on the screen   
    def getPosition(self):
        id=self.sensor.getSensorId()
        nb_btn=len(self.sensor.generalConfiguration.sensors)
        L=[]
        if nb_btn%2 == 0 :#paire
            x=(self.sensor.generalConfiguration.get_width()/2)-(nb_btn/2*self.sensor.generalConfiguration.buttonWidth)
        else :
            x=(self.sensor.generalConfiguration.get_width()/2)-(nb_btn//2*self.sensor.generalConfiguration.buttonWidth)-(self.sensor.generalConfiguration.buttonWidth/2)
        L.append(x+(id*self.sensor.generalConfiguration.buttonWidth))
        L.append(0)
        return L

    # Draws the text 
    def drawLines(self, lines):
        pos=self.getPosition()
        font = pygame.font.Font(None,14)
        i=0
        for ligne in lines:
            textImage = font.render(ligne, 1, [255,255,255])
            self.sensor.generalConfiguration.screen.blit(textImage,[pos[0]+50,pos[1]+i])
            i=i+10
        
    # Draws the button
    def draw(self):   
        pos=self.getPosition()
        largeur=1
        if self.sensor.isSelected()==True:
            largeur=3
        
        pygame.draw.rect(self.sensor.generalConfiguration.screen,[255,255,255],[pos[0],pos[1],self.sensor.generalConfiguration.buttonWidth,self.sensor.generalConfiguration.buttonHeight],largeur)        
        self.drawLines(['',self.sensor.getLabel(),'',self.sensor.read()])
