#Informatique (INFO-F206)-Projet
#Professor: Jean Cardinal
#Student: Luciano Muratore, BAC Mathematiques
#Date: Octobre 2021


#Library Needed 
import sys
import random 

#argv parameters
#First: n number of repetitions
#Second: Text File Input which contains the Linear Transformations

n=int(sys.argv[1]) #nro of repetitions
name_fichier=sys.argv[2] #text file input 


#Reading of the Input File
def lecture(name_fichier):
    """
    lecture(name_fichier) opens a txt file and returns a list L of list.
    L[0]=n
    L[i]=T(i) 
    """
    fichier=open(name_fichier,'r') 
    L=[]
    for ligne in fichier:
        L.append([float(x) for x in ligne.split()]) #L es un Array con L[0]=n y L[i]=T(i) siendo T(i) las coordenadas de la transformacion Ti e i entre 1 y n
    fichier.close()
    return L

L=lecture(name_fichier)

#Applying T(i) to (x,y)
def T(i,G):
    """
    T(i) applies a linear transformation to one point (x,y)
    Returns a new (x,y) point 
    """
    x=G[0]
    y=G[1]
    P=[]
    x=(L[i][0]*x)+(L[i][1]*y)+L[i][2]
    P.append(x) 
    y=(L[i][3]*x)+(L[i][4]*y) +L[i][5]
    P.append(y)
    return P

#N repetitions of T(i)
def Repetitions(n):
    """
    Returns a Matrix M which has the points (x,y) after they have transformed by T(i)
    """
    for j in range(n-1):
        M=[]
        G=[0,0]
        G1=T(random.randint(1,L[0][0]),G)  
        M.append(G1)
        for j in range(n-1):
            G1=T(random.randint(1,L[0][0]),G1)
            M.append(G1)
    return M

M=Repetitions(n)

#Changing a list of floats in a string of characters
def string(L):
    """
    string(L) receives a list of floats [a,b] and returns a b as a string 
    """
    return ' '.join([str(x) for x in L])+'\n'


#Writing over the out.txt file
def ecrire():
    """
    ecrire() returns the out.txt file written.
    """
    fichier=open('out.txt','w')
    for i in range(len(M)):
        fichier.write(string(M[i]))
    fichier.close()

ecrire()