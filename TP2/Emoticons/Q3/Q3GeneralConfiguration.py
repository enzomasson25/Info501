# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame

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
    #Retourne la largeur de la surface de dessin
    def get_width(self):
        return self.screen.get_width()
    #Retourne la hauteur de  la surface de dessin
    def get_height(self):
        return self.screen.get_height()
    
    #getters de la question 1)d):
    def get_screen(self):
        return self.screen 
    
    def get_buttonWidth(self):
        return self.buttonWidth
    
    def get_buttonHeight(self):
        return self.buttonHeight
    
    def get_emoticonSize(self):
        return self.emoticonSize
    
    def get_emoticonBorder(self):
        return self.emoticonBorder
    
    # Compléter avec les Getters de la question Q1.4

        
    # Draws on pygame screen      
    def draw(self):
        pass
            
    # Displays   
    def display(self):
        # Draws on the screen surface
        self.draw()
        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
               

