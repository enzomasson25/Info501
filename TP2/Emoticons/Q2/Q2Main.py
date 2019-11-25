# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
from Q2GeneralConfiguration import GeneralConfiguration
from Q2Emoticon import Emoticon

def main():
 
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()

    # Creates an emoticon
    emoticon = Emoticon()
    # Injects the general configuration in the emoticon
    emoticon.setGeneralConfiguration(generalConfiguration)
    
    print(emoticon.headToArea([0,0]))
    
    
  
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Draws the emoticon
        elif event.type == pygame.USEREVENT:
            emoticon.draw()
            emoticon.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
        
'''generalConfiguration = GeneralConfiguration() 
emoticon = Emoticon()       

print(emoticon.headToArea([0,0]))'''

"""Test pour la question 2)b)       
print(emoticon.headToArea([0,0])) """  

"""Test pour la question 2)c)
print(emoticon.color(1))
print(emoticon.color(0.156))
print(emoticon.color(-1))
    """ 
        

        
                
# Calls the main function
if __name__ == "__main__":
    main()    