# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:04:24 2019

@author: 33762
"""

class etape:
    """
    -numero
    -date au plus tot
    -date au plus tard
    -liste de tâches
    """
    
    def __init__(self,numero,date_plus_tard,date_plus_tot,taches=[]):
        """
        constructeur de la classe etape
        """
        self.numero = numero
        self.date_plus_tard = date_plus_tard
        self.date_plus_tot = date_plus_tot
        self.taches = taches
    
    def  __str__(self):
        return self.numero
       
    def get_au_plus_tot(self):
        return self.date_plus_tot
    
    def get_au_plus_tard(self):
        return self.date_plus_tard
    
    def get_number(self):
        return self.numero
    
    def get_next_steps(self):
        res = []
        for tache in self.taches:
            res.append(tache.etape_suivante)
        return res
    
    def get_previous_steps(self,noeudAChercher,res=[]):
        """
        ne fonctionne pas quand il a plusieurs prédéceceurs
        """
        if self.get_next_steps() == [] : #fin de la recursivité
            return res # ne retourne rien 
        else :
            for etape_suivante in self.get_next_steps(): 
                print ("self :"+str(self)+" suivant : "+str(etape_suivante))
                if etape_suivante == noeudAChercher:
                    res.append(self.numero)
                return etape_suivante.get_previous_steps(noeudAChercher,res)
                
class tache:
    """
    -nom 
    -duree
    -etape suivante
    """
    
    def __init__(self,nom,duree,etape_suivante=None):
        """
        constructeur de la classe tache
        """
        self.nom = nom
        self.duree = duree
        self.etape_suivante = etape_suivante
        
    def __str__(self):
        return self.nom

etape8 = etape('8',220,220) 
tacheH = tache('H',10,etape8)
etape7 = etape('7',210,210,[tacheH]) 
tacheG = tache('G',60,etape7)
tacheT = tache('T',0,etape7)   
etape5 = etape('5',50,210,[tacheT]) 
etape6 = etape('6',150,150,[tacheG])    
etape3 = etape('3',150,210,[tacheT])   
tacheE = tache('E',10,etape5)
tacheF = tache('F',30,etape6)
tacheC = tache('C',30,etape3)
etape4 = etape('4',40,200,[tacheE])
etape2 = etape('2',120,120,[tacheC,tacheF])
tacheD = tache('D',10,etape4)
tacheB = tache('B',90,etape2)
etape1 = etape('1',30,30,[tacheB,tacheD])
tacheA = tache('A',30,etape1)
etape0 = etape('0',0,0,[tacheA])

print(etape0.get_previous_steps(etape7))