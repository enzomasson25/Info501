#
# ATTENTION : NE PAS METTRE D'ACCENT, MEME DANS LES COMMENTAIRES
#
# import des bibliotheques
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class image:
    # Initialisation d'une image composee d'un tableau 2D vide
    # (pixels) et de 2 dimensions (H = height et W = width) mises a 0
    def __init__(self):
        self.pixels = None 
        self.H = 0
        self.W = 0
        
    # Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
    # et affectation des dimensions de l'image self avec les dimensions 
    # du tableau 2D (tab_pixels) 
    def set_pixels(self, tab_pixels):
        self.pixels = tab_pixels
        self.H,self.W = self.pixels.shape 

    # Lecture d'un image a partir d'un fichier de nom "file_name"
    def load_image(self, file_name):
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")

    # Affichage a l'ecran d'une image
    def display(self, window_name):
        fig=plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide")
            
    

    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================

    def binaris(self,S):
        #ecrire ici la methode binarisation
        for i in range(0,self.H):
            for j in range(0,self.W):
                if self.pixels[i][j]<S:
                    self.pixels[i][j]=0
                else :
                    self.pixels[i][j]=255
        return self
        
    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================

    def localisation(self):
        #ecrire ici la methode localisation
        def c_min(self):
            for i in range(0,self.W):
                for j in range(0,self.H):
                    if self.pixels[j][i]==0:
                        return i
         
        def l_min(self):
            for i in range(0,self.H):
                for j in range(0,self.W):
                    if self.pixels[i][j]==0:
                        return i
        
        def c_max(self):
            for i in range(0,self.W):
                for j in range(self.H,0,-1):
                    if self.pixels[j][i]==0:
                        return i
        
        def l_max(self):
            for i in range(self.H,0,-1):
                for j in range(self.W,0,-1):
                    if self.pixels[i][j]==0:
                        return j
                    
                    
        print(c_min(self)) #good
        print(l_min(self)) #good
        print(c_max(self)) 
        print(l_max(self))
        
    
    
         
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================

#    def resize_im(self,new_H,new_W):

        # ecrire ici la methode de redimensionnement
		# attention la fonction resize fournit une image
		# dont des valeurs sont reelles et comprises entre 0 et 1
		# il faut donc multiplier le resultat par 255
		# et convertir au format entier non signe sur 8 bits :
		# ima_resize.pixels = np.uint8(ima_resize.pixels*255)



    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================

#    def simil_im(self,im):
        # ecrire ici la methode de mesure de similitude par correlation




   
# fin class image


#==============================================================================
#  Fonction de lecture des fichiers contenant les images modeles
#  Les differentes images sont mises dans une liste
# l'element '0' de la liste de la liste correspond au chiffre 0,
# l'element '1' au chiffre 1, etc.
#==============================================================================

def lect_modeles():

    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
             '_7.png','_8.png','_9.png']
    list_model = []
    for fichier in fichiers:
        model = image()
        model.load_image(fichier);
        list_model.append(model)
    return list_model
   
#==============================================================================
#==============================================================================

#   PROGRAMME PRINCIPAL

#==============================================================================
# # Lecture image
#==============================================================================

im = image()
im.load_image('test10.JPG')
im.display("image initiale")

#==============================================================================
# Binarisation
#==============================================================================

im_bin=im.binaris(150)
print(type(im_bin))
im_bin.display("image binarisé")

#
#==============================================================================
#  Localisation chiffre
#==============================================================================
#
im_loc=im_bin.localisation()


#
#==============================================================================
# Test de la fonction resize
#==============================================================================




#
#==============================================================================
# Test de la fonction similitude
#==============================================================================




#==============================================================================
# Lecture des chiffres modeles
#==============================================================================

list_model = lect_modeles()
# test verifiant la bonne lecture de l'un des modeles, par exemple le modele '8'
list_model[8].display("modele 8")

#==============================================================================
# Mesure de similitude entre l'image et les modeles 
# et recherche de la meilleure similitude
#==============================================================================



