# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
from Q4GeneralConfiguration import GeneralConfiguration
from Q4Sensor import Sensor

def main():
 
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()

    # Creates a sensor
    sensor = Sensor(
        'https://www.polytech.univ-smb.fr/apps/myreader/capteur.php?capteur=epua_b204_clim', 
        'Temp. Clim B204',
        [20, 22, 23]    
    )
    # Injects the general configuration in the sensor
    sensor.setGeneralConfiguration(generalConfiguration)
  
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Draws the button
        elif event.type == pygame.USEREVENT:
            generalConfiguration.display()
            print(sensor.read()) #on utilise la methode read() de la classe Sensor pour afficher la temperature de notre objet sensor
            print(sensor.label) #on affiche l'attribut label de notre objet sensor
            print(sensor.getTransformedValue())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
                
# Calls the main function
if __name__ == "__main__":
    main()    