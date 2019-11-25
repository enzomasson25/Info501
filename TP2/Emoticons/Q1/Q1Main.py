# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q1GeneralConfiguration import GeneralConfiguration

def main():

    # Creates an instance of the class GeneralConfiguration
    generalConfiguration = GeneralConfiguration()
    print(generalConfiguration.screen.get_width())
    print(generalConfiguration.screen.get_height())
      
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        # Checks if the user wants to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Display the drawing
        elif event.type == pygame.USEREVENT:
            generalConfiguration.display()
                       
        # Checks if the user has clicked with the mouse               
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
                
# Calls the main function
if __name__ == "__main__":
    main()    

