import numpy as np



####################################################
# Produit A x pour la matrice de la partie 1
def produit1(x,ddata):
    alpha,h = ddata
    prodx = x * 0.0

    # Completer ICI :
    # ...
    n=np.size(x)
    prodx[0]=(2+alpha*h*h)*x[0]-x[1]
    prodx[np.size(x)-1]=(2+alpha*h*h)*x[np.size(x)-1]-x[np.size(x)-2]
    prodx[1:n-1] = -x[0:n-2]+(2+alpha*h*h)*x[1:n-1]-x[2:n]
    #for i in range(1,np.size(x)-1):
     # prodx[i]=-x[i-1]+(2+alpha*h*h)*x[i]-x[i+1]
    return prodx
####################################################


####################################################
# Produit M^{-1} x pour la matrice de la partie 1
def diag1(x,ddata):
    alpha,h = ddata
    res = x* 0.
    # Completer ICI :
    res=x/(2+alpha*h*h)

    return res
####################################################




####################################################
# Produit M^{-1} x pour la partie 2 (image)
def diagImg(x,ddata):
    mask,regu,Nx,Ny = ddata
    diagg = x*0.
    diagg += mask.reshape(-1)
    diagg += regu * 4.0
    return x/diagg
####################################################



####################################################
# Produit A x pour la matrice de la partie 2 (image)
def produitImg(x,ddata):
    mask,regu,Nx,Ny = ddata
    xxImg = x.reshape(Nx,Ny)
    newImg = mask*xxImg
    # Completer ICI :
 
    newImg = newImg + regu*laplace(xxImg)
    	
    return newImg.reshape(-1)
####################################################

####################################################
# Calcul du Laplacien discret partie 2 (image)
def laplace(img):
    imgres = img*4.0 # Ici img est une matrice de taille Nx x Ny
    # Completer ICI :
    #Nx,Ny=img.shape
    #version matricielle :
    #for i in range(1,Nx-1):
    #	for j in range(1,Ny-1):
    #		imgres[i,j] = imgres[i,j] - img[i-1,j] - img[i,j-1] - img[i+1,j] - img[i,j+1]
    
    
    #version matricielle optimisée:
    imgres[1:-1,1:-1] -= img[:-2,1:-1] + img[1:-1,:-2] + img[2:,1:-1] + img[1:-1,2:]
    
    return imgres
####################################################
