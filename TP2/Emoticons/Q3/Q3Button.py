# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame

class Button:

    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration

    # Draws the button    
    def draw(self):   
        pygame.draw.rect(self.generalConfiguration.screen,[255,255,255],[90,200,120,50],1)
        
    
    #Question 3)1):Sachant que le bouton est centré on obtient le coin inferieur gauche en retirant la moitié de la largeur du bouton à la moitié de la largeur de la fenetre 
    #Sachant que le bouton est collé au haut de la fenetre, y=0 dans tous les cas
    def getPosition(self):
        L=[]
        x=(self.generalConfiguration.get_width()/2)-(self.generalConfiguration.get_buttonWidth()/2)
        L.append(x)
        L.append(0)
        return L
        
    
    def drawLines(self,lines):
        font = pygame.font.Font(None,14)
        i=0
        for ligne in lines:
            textImage = font.render(ligne, 1, [255,255,255])
            self.generalConfiguration.screen.blit(textImage,[100,200+i])
            i=i+10
        

        
