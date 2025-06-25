import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


import algo as algo
import data as data

import affichage as affichage


####################################################
## Etude de méthodes itératives et reconstruction d'image
####################################################

####################################################
# Choix de la partie
print('Que souhaitez-vous faire ?')
print('1. Résoudre le systeme lineaire Ax = b via une methode iterative.')
print('2. Faire une étude comparative des méthodes itératives.')
print('3. Reconstruire une image déteriorée')
choixPartie = input('Choix : ')
####################################################


####################################################
# Choix de la méthode
choixMethode = '1'
if(choixPartie == '1' or choixPartie == '3'):
    print('Quelle méthode voulez-vous utiliser ?')
    print('1. Jacobi')
    print('2. Descente de gradient')
    print('3. CG')
    print('4. PCG')
    choixMethode = input('Choix : ')
####################################################

####################################################
if(choixPartie == '1' or choixPartie == '2'):

    ###############################################
    ## Parametres du probleme
    # Modifier ICI:
    N = 100
    hh = 1./(N+1)
    alpha = 1.0

    tol = 1e-5 # Critere d'arret de la méthode
    iteMax = 1000 # Nombre maximal d'iterations

    ddata = [alpha,hh] # Donner utiles pour calculer le produit A x
    ###############################################

    ###############################################
    ## Solution exacte :
    solex = np.cos(np.arange(1,N+1)*hh*2*np.pi)
    ## Et second membre associé :
    # Completer ICI :
    bb=data.produit1(solex,ddata)

    ###############################################

    ###############################################
    ## Resolution du probleme Ax = b
    x0 = solex*0.
    xx = x0*1.0
    if(choixPartie=='1'):
        residus = []
        if(choixMethode == '1'):
            xx, residus = algo.Jacobi(data.produit1,data.diag1,x0,bb,ddata,iteMax,tol)
        if(choixMethode == '2'):
            xx, residus = algo.DescenteGrad(data.produit1,x0,bb,ddata,iteMax,tol)
        if(choixMethode == '3'):
            xx, residus = algo.CG(data.produit1,x0,bb,ddata,iteMax,tol)
        if(choixMethode == '4'):
            xx, residus = algo.PCG(data.produit1,data.diag1,x0,bb,ddata,iteMax,tol)
        ###############################################

        ###############################################
        ## Calcul erreur et affichage erreur residu:
        print('Err || sol - sol_ex||_2 = ',np.sqrt(np.dot(xx-solex,xx-solex))/N )
        # Tracer de la solution numerique :
        #affichage.afficher([np.arange(0,len(xx))*hh],[xx])
        # Tracer de l'erreur de residu || A x_k - b||_2 en fonction de k
        affichage.afficher([np.arange(0,len(residus))],[np.log10(residus)])
        ###############################################

    if(choixPartie=='2'):
        ###############################################
        ## Calcul des residus pour les 3 méthodes :
        xx, residusJacob = algo.Jacobi(data.produit1,data.diag1,x0,bb,ddata,iteMax,tol)
        xx, residusDesce = algo.DescenteGrad(data.produit1,x0,bb,ddata,iteMax,tol)
        xx, residusCG = algo.CG(data.produit1,x0,bb,ddata,iteMax,tol)

        # Tracer de la solution numerique :
        affichage.afficher([np.arange(0,len(xx))*hh],[xx])
        ###############################################

        ###############################################
        ## Affichage comparatif des courbes de convergence :
        affichage.afficherConv([np.arange(0,len(residusJacob)), np.arange(0,len(residusDesce)), np.arange(0,len(residusCG))],[(residusJacob),(residusDesce),(residusCG)])
        ###############################################
    ###############################################

####################################################






####################################################
## Reconstruction d'image
if(choixPartie == '3'):

    ###############################################
    ## Lecture du fichier image et donnee :
    img = mpimg.imread("Img_AltGray.png")
    img = img*255
    img = img.astype(float)
    img = img[:,:,0:3]
    imgGray = img[:,:,0]*1.0

    Nx = len(img[:,0,0])
    Ny = len(img[0,:,0])
    Mask = np.loadtxt('Mask.txt');
    # Modifier ici :
    tol = 1e-5
    iteMax = 50
    regul = 1
    ###############################################

    ###############################################
    ## Resolution du probleme moindre carré via equation normale :
    x0 = imgGray.reshape(-1) # Reecrit en ligne (la matrice de) l'image
    bb = imgGray.reshape(-1) # Reecrit en ligne (la matrice de) l'image
    ddata = [Mask,regul,Nx,Ny] # Donner utiles pour calculer le produit A x
    xx = x0*1.0
    residus = []
    if(choixMethode == '1'):
        xx, residus = algo.Jacobi(data.produitImg,data.diagImg,x0,bb,ddata,iteMax,tol)
    if(choixMethode == '2'):
        xx, residus = algo.DescenteGrad(data.produitImg,x0,bb,ddata,iteMax,tol)
    if(choixMethode == '3'):
        xx, residus = algo.CG(data.produitImg,x0,bb,ddata,iteMax,tol)
    if(choixMethode == '4'):
        xx, residus = algo.PCG(data.produitImg,data.diagImg,x0,bb,ddata,iteMax,tol)
    ###############################################

    ###############################################
    ## Sauvergarde de l'image reconstruite
    ImgRecons = xx.reshape(Nx,Ny)
    imgReconsRGB = img*1.0
    imgReconsRGB[:,:,0] = ImgRecons[:,:]
    imgReconsRGB[:,:,1] = ImgRecons[:,:]
    imgReconsRGB[:,:,2] = ImgRecons[:,:]
    mpimg.imsave("Img_Recons.png", imgReconsRGB.astype(np.uint8))
    ###############################################

####################################################
