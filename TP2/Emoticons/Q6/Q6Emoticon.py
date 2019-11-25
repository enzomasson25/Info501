# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math


class Emoticon:
    # Constructor
    def __init__(self, sensor) :
        self.sensor = sensor

    # Sets the emoticon parameters
    def setEmoticonParameters(self, size) :        
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size]
        self.eyeRightPosition = [0.15*size, 0.1*size]    
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10    

    # Computes the position in the screen 
    def headToArea(self, position):
        L=[]
        L.append(position[0]+self.sensor.generalConfiguration.screen.get_width()/2)
        L.append(-position[1]+self.sensor.generalConfiguration.screen.get_height()/2)
        return L
        
    # Computes the color    
    def color(self,x):
        r=0
        g=0
        b=0
        pas=1/255
        if x==0:
            r=255
            g=255
            b=0
          
    
        if x>0:
            val=x/pas
            r=int(255-val)
            g=255
            b=0
        
        
        if x<0:
            val=-x/pas
            r=255
            g=int(255-val)
            
        return([r,g,b]) 
 
    # Draws head            
    def head(self, x):
        color=self.color(x)
        pygame.draw.circle(self.sensor.generalConfiguration.screen, color, [400, 300],self.sensor.generalConfiguration.emoticonSize//2) 
    
    # Draws one eye    
    def eye(self, position):
        pygame.draw.ellipse(self.sensor.generalConfiguration.screen, [0,0,0], [(position[0]-self.eyeWidth/2),(position[1]-self.eyeHeight/2),self.eyeWidth,self.eyeHeight])


    # Draws the mouth          
    def mouth(self, position, x):
        if x<=0.15 and x>=-0.15:
           pygame.draw.line(self.sensor.generalConfiguration.screen, [0,0,0],[position[0]-self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight/2],[position[0]+self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight/2])
       
        if x>0:
           pygame.draw.arc(self.sensor.generalConfiguration.screen, [0,0,0],[(position[0]-self.mouthMaxWidth/2),(position[1]-self.mouthMaxHeight/2),self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],4*math.pi/4, 8*math.pi/4)
       
        elif x<0:
           pygame.draw.arc(self.sensor.generalConfiguration.screen, [0,0,0],[(position[0]-self.mouthMaxWidth/2),(position[1]-self.mouthMaxHeight/2),self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],8*math.pi/4, 4*math.pi/4)
          
        
    # Draws the emoticon    
    def draw(self):   
        #On dessine la tête
        self.head(self.sensor.getTransformedValue())
        #On dessine les yeux en definissant d'abord les parametres de l'emoticon
        self.setEmoticonParameters(400)
        self.eye(self.headToArea(self.eyeLeftPosition))
        self.eye(self.headToArea(self.eyeRightPosition))
        
        self.mouth(self.headToArea(self.mouthPosition),self.sensor.getTransformedValue())        
        
