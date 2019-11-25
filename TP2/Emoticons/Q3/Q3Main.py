# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
from Q3GeneralConfiguration import GeneralConfiguration
from Q3Button import Button

def main():
 
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()

    # Creates a button
    button = Button()
    # Injects the general configuration in the button
    button.setGeneralConfiguration(generalConfiguration)
  
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Draws the button
        elif event.type == pygame.USEREVENT:
            button.draw()
            
            lines=['', 'Temp. Toit', '', '38.4']
            button.drawLines(lines)
            generalConfiguration.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
                
# Calls the main function
if __name__ == "__main__":
    main()    