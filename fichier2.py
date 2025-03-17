#Importación del fichier como asi tambien el nro (n) de repeticiones
import sys

#name_fichier=sys.argv[2] #nombre del archivo
n=int(sys.argv[1]) #nro de repeticiones
name_fichier=sys.argv[2]

#Lectura de un Fichier 
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

#Libreria para generar pseudo-aleatorio valores
import random

#T(i) retorna un punto [x,y] luego de realizar una transformacion 
def T(i,G):
    x=G[0]
    y=G[1]
    P=[]
    x=(L[i][0]*x)+(L[i][1]*y)+L[i][2]
    P.append(x) 
    y=(L[i][3]*x)+(L[i][4]*y) +L[i][5]
    P.append(y)
    return P


#Repetitions(n) retorna una Matriz M con puntos a los que se les aplico T
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

#str(L) convierte una lista de floats en una cadena de caracteres
def string(L):
    """
    string(L) receives a list of floats [a,b] and returns a b as a string 
    """
    return ' '.join([str(x) for x in L])+'\n'  


#Escritura del Fichier 'out.txt'
def ecrire():
    fichier=open('out.txt','w')
    for i in range(len(M)):
        fichier.write(string(M[i]))
    fichier.close()

ecrire()