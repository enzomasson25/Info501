# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math

class Emoticon:
    
   """ # Constructor
    def __init__(self) :
        self.initPygame()
         # Parameters for the emoticons        
        self.emoticonSize = 400
        self.emoticonBorder = 20 
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
        
        
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)
        # Gets pygame screen
        self.screen = pygame.display.get_surface()"""

    # Setters
   def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
        
        
        
   def setEmoticonParameters(self, size) :
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size]
        self.eyeRightPosition = [0.15*size, 0.1*size]
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10  
        
        
   def get_eyeLeftPosition(self):
       return self.eyeLeftPosition
   
   def get_eyeWidth(self):
       return self.eyeWidth
   
   def get_eyeHeight(self):
       return self.eyeHeight

    # Draws the emoticon    
   def draw(self): 
       #On dessine la tête
        self.head(0)
        #On dessine les yeux en definissant d'abord les parametres de l'emoticon
        self.setEmoticonParameters(400)
        self.eye(self.headToArea(self.eyeLeftPosition))
        self.eye(self.headToArea(self.eyeRightPosition))
        
        self.mouth(self.headToArea(self.mouthPosition),0)
        
        
        
        
   
    
  #Question 2)b) : On translate simplement le repère en partant du principe que le [0,0] est au milieu de la tête.  
   def headToArea(self, position):
        L=[]
        L.append(position[0]+self.generalConfiguration.screen.get_width()/2)
        L.append(-position[1]+self.generalConfiguration.screen.get_height()/2)
        return L
    
   #Question 2)c) : On décompose le problème en 3 cas: 
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
        
        
     #Question 2)d): On récupère la couleur avec la méthode "color" et on l'applique sur le cercle:   
        
   def head(self,x):
        color=self.color(x)
        #pygame.draw.rect(self.generalConfiguration.screen,[64,175,198],[0,0,800,600])
        #On prends en compte "emoticonBorder"
        #pygame.draw.rect(self.generalConfiguration.screen,[0,0,0],[200-self.generalConfiguration.emoticonBorder,100-self.generalConfiguration.emoticonBorder,self.generalConfiguration.emoticonSize+2*self.generalConfiguration.emoticonBorder,self.generalConfiguration.emoticonSize+2*self.generalConfiguration.emoticonBorder])
        #On prends en compte "emoticonSize"
        #pygame.draw.rect(self.generalConfiguration.screen,[255,255,255],[200,100,self.generalConfiguration.emoticonSize,self.generalConfiguration.emoticonSize])
        
        pygame.draw.circle(self.generalConfiguration.screen, color, [400, 300],self.generalConfiguration.emoticonSize//2) 
        
        #pygame.draw.ellipse(self.screen, [0,0,0], [300,220, 55,80])
        #pygame.draw.ellipse(self.screen, [0,0,0], [438,220, 55,80])
        
        #pygame.draw.arc(self.screen, [0,0,0], [320,380, 170, 80], 4*math.pi/4, 8*math.pi/4)
        
        
        
        
   def eye(self,position):
        pygame.draw.ellipse(self.generalConfiguration.screen, [0,0,0], [(position[0]-self.eyeWidth/2),(position[1]-self.eyeHeight/2),self.eyeWidth,self.eyeHeight])
        
   
   def mouth(self,position,x):
       if x<=0.15 and x>=-0.15:
           pygame.draw.line(self.generalConfiguration.screen, [0,0,0],[position[0]-self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight/2],[position[0]+self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight/2])
       
       if x>0:
           pygame.draw.arc(self.generalConfiguration.screen, [0,0,0],[(position[0]-self.mouthMaxWidth/2),(position[1]-self.mouthMaxHeight/2),self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],4*math.pi/4, 8*math.pi/4)
       
       elif x<0:
           pygame.draw.arc(self.generalConfiguration.screen, [0,0,0],[(position[0]-self.mouthMaxWidth/2),(position[1]-self.mouthMaxHeight/2),self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],8*math.pi/4, 4*math.pi/4)
          
            

          
        
       
    
    
    
    
        
    
    
    # Displays   
   def display(self):
        # Draws on the screen surface
        self.draw()
        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
        
            
            
        
    
            
            
    
    
    
    
    