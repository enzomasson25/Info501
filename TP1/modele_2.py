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
        #print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")

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
        
        #numéro de colonne min
        def c_min(self):
            for i in range(0,self.W):
                for j in range(0,self.H):
                    if self.pixels[j][i]==0:
                        return i
         
        #numéro de ligne min
        def l_min(self):
            for i in range(0,self.H):
                for j in range(0,self.W):
                    if self.pixels[i][j]==0:
                        return i
        
        #numéro de colonne max
        def c_max(self):
            for i in range(self.W - 1,0,-1):
                for j in range(self.H - 1,0,-1):
                    if self.pixels[j][i]==0:
                        return i
        
        #numéro de ligne max
        def l_max(self):
            for i in range(self.H - 1,0,-1):
                for j in range(self.W - 1,0,-1):
                    if self.pixels[i][j]==0:
                        return i
                    
        dictio = {"c_min":c_min(self), "l_min":l_min(self), "c_max":c_max(self), "l_max":l_max(self)} 
        
        im = image()
        im.set_pixels(self.pixels[dictio["l_min"]:dictio["l_max"]+1,dictio["c_min"]:dictio["c_max"]+1])
        return im
        
#        print(c_min(self)) #good
#        print(l_min(self)) #good
#        print(c_max(self)) 
#        print(l_max(self))

         
         
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================

    def resize_im(self,new_H,new_W):
        
        im_resized = image()
        im_resized.pixels = resize(self.pixels, (new_H,new_W), 0)
        im_resized.H=new_H
        im_resized.W=new_W
        im_resized.pixels = np.uint8(im_resized.pixels*255)
        
        return im_resized

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================

    def simil_im(self,im):
        #on suppose que les 2 images ont la même dimension 
        pixelTotal=self.H*self.W
        pixelEgaux=0
        for i in range(0,self.H):
            for j in range(0,self.W):
                if self.pixels[i][j]==im.pixels[i][j]:
                    pixelEgaux=pixelEgaux+1
                
        return pixelEgaux/pixelTotal
    
     #==============================================================================
    # Methode de detection du chiffre
    #==============================================================================
    def chiffre(self):
        meilleurSimi=0
        res=0
        imBin=self.binaris(150)
        imLoc=imBin.localisation()
        list_model = lect_modeles()
        for i in range(0,len(list_model)):
            img = image()
            img=list_model[i]
            im_resize=imLoc.resize_im(img.H,img.W)
            if im_resize.simil_im(img)>meilleurSimi:
                meilleurSimi=im_resize.simil_im(img)
                res = i
        return res
    
 
    #==============================================================================
    # Methode de division de l'image en deux (le nombre localisé et le reste)
    #==============================================================================
   
    #fonction renvoyant true si toute la colonne est blanche
    def isColumnEmpty(self, numCol):
        #prned la liste de toutes les valeur des pixels d'une colonne et compte le nombre de noir, si il n'y en a pas la fonction retourne true
        return sum(list(map(lambda pixel : pixel == 0, [element[numCol] for element in [list(liste) for liste in self.pixels]]))) == 0
    
    
    #renvoie la première première colonne blanche
    def premiereColonneBlanche(self):
        
        #pour toutes les colonnes
        for col in range(0,self.W):
            
            #renvoie la col vide
            if self.isColumnEmpty(col):
                return col
        #sinon renvoie la dernière col + 1
        return self.W + 1
        
    
    #fonction qui renvoie l'image du chiffre et le reste
    def diviserImageEnChiffrePlusReste(self):
        
        #on commence par localiser l'image de départ
        selfLocalise = self.localisation()
        
        #les deux variables images
        imgReste, imgChiffre = image(), image()
        
        
        premiereColonneBlanche = selfLocalise.premiereColonneBlanche()
        
        #création des deux images
        imgChiffre.set_pixels(selfLocalise.pixels[0 : selfLocalise.H, 0 : premiereColonneBlanche - 1])
        imgReste.set_pixels(selfLocalise.pixels[0 : selfLocalise.H, premiereColonneBlanche : selfLocalise.W])
        
        #renvoie des images
        return imgChiffre, imgReste
    
    
    def direChiffres(self):
        
        images = self.diviserImageEnChiffrePlusReste()
        
        liste = []
        
        while images[1].W != 0:
            
            liste.append(images[0].chiffre())
            images = images[1].diviserImageEnChiffrePlusReste()
            
        liste.append(images[0].chiffre())
        
        return liste 
        
    
# fin class image



#==============================================================================
#  Fonction de lecture des fichiers contenant les images modeles
#  Les differentes images sont mises dans une liste
# l'element '0' de la liste de la liste correspond au chiffre 0,
# l'element '1' au chiffre 1, etc.
#==============================================================================

def lect_modeles():
    
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', '_7.png','_8.png','_9.png']
    
    list_model = []
    
    for fichier in fichiers:
        model = image()
        model.load_image(fichier)
        list_model.append(model)
        
    return list_model
   
#==============================================================================
#==============================================================================

#   PROGRAMME PRINCIPAL

#==============================================================================
# # Lecture image
#==============================================================================

print("\nImage Initiale")

im = image()
im.load_image('test9.JPG')
im.display("image initiale")
im = im.binaris(150)
print(im.direChiffres())

#==============================================================================
# Binarisation
#==============================================================================

#print("\nImage Binarisé")
#
#im_bin=im.binaris(150)
##print(type(im_bin))
#im_bin.display("image binarisé")

#
#==============================================================================
#  Localisation chiffre
#==============================================================================
#

#print("\nImage Localisé")
#im_loc=im_bin.localisation()
#im_loc.display("image localisé")

#
#==============================================================================
# Test de la fonction resize
#==============================================================================

#print("\nImage avec sa nouvelle Taille")
#
#im_resized=im_loc.resize_im(32,18)
#im_resized.display("image resized")


#
#==============================================================================
# Test de la fonction similitude
#==============================================================================

#print("\nTest de la fonction similitude")
#
#
#list_model = lect_modeles()
#img_1=image()
#img_1=list_model[1]
#img_1.display("veritable 1")
#
#rapportSimilitude = im_resized.simil_im(img_1.binaris(150))
#print(rapportSimilitude)





#==============================================================================
# Mesure de similitude entre l'image et les modeles 
# et recherche de la meilleure similitude
#==============================================================================

#imaTrouver = image()
#imaTrouver.load_image('test9.JPG')
#print(imaTrouver.chiffre())



#==============================================================================
# Lecture des chiffres modeles
#==============================================================================

#print("\n\n\n\n")
#
#list_model = lect_modeles()
## test verifiant la bonne lecture de l'un des modeles, par exemple le modele '8'
#list_model[8].display("modele 8")

#==============================================================================
# Mesure de similitude entre l'image et les modeles 
# et recherche de la meilleure similitude
#==============================================================================










