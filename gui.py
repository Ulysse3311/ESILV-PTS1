# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:18:54 2020

@author: ulyss
"""

import tkinter as tk
import time
import random

def randMatrice():
    couleurs=('red','white','orange','yellow','green','blue')
    mat=[]
    for face in range(6):
        f=[[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                f[i][j]=random.choice(couleurs)
        f[1][1]="grey"
        mat.append(f)
    print(mat)
    af.afficher(mat)
    af.canvas.after(1000,randMatrice)


class GUI():
    def __init__(self,cube,root):
        self.tailleCote=30
        self.tailleFace=self.tailleCote*3
        
        self.root=root
        self.root.title("Redi Cube")
        self.root.geometry("300x400")      
        self.canvas=tk.Canvas(self.root,width=300,height=400,bg="grey")
        
        self.afficher(cube)
        
        self.canvas.pack()
        

        
    def afficher(self,cube):
        #mise en 2d du cube
        margeX=15
        margeY=20
        self.posFaces=[              (self.tailleFace+margeX,0+margeY,cube[4]),
         (0+margeX,self.tailleFace+margeY,cube[3]),(self.tailleFace+margeX,self.tailleFace+margeY,cube[0]),(2*self.tailleFace+margeX,self.tailleFace+margeY,cube[1]),
                        (self.tailleFace+margeX,2*self.tailleFace+margeY,cube[5]),
                        (self.tailleFace+margeX,3*self.tailleFace+margeY,cube[2])]
        #affichage
        for posX,posY,couleurs in self.posFaces:
            for y in range(3):
                for x in range(3):
                    #création carrés de la face
                    self.canvas.create_rectangle(posX+x*self.tailleCote,posY+y*self.tailleCote,posX+(x+1)*self.tailleCote,posY+(y+1)*self.tailleCote, fill=couleurs[y][x])
                
 
matrice = []
for i in ('red','white','orange','yellow','green','blue'):
    matrice.append([[i,i,i],[i,'grey',i],[i,i,i]])
        
root=tk.Tk()
af=GUI(matrice,root)

matrice=[]
for i in ('blue','white','orange','yellow','green','red'):
    matrice.append([[i,i,i],[i,'grey',i],[i,i,i]]) 

#time.sleep(3)
#af.canvas.after(1000,af.afficher(matrice))    
#af.afficher(matrice)
randMatrice()
root.mainloop()  





