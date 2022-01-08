# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:43:29 2022

@author: LENOVO
"""
from random import randrange

# Pour implementer CDMA, nous allons implementer plusieurs 
# fonctions decrivant son fonctionnement

# Processus emetteur

# Generer les sequences de chips

def Generer_code():
    
    chips=[]
    sequence=str()
    for i in range(4):
        for j in range(8):
            sequence=sequence+str(randrange(2))
        chips.append(sequence)
        sequence=""
    return chips        
            
# Calculer l'information qui sera envoyé aux recepteurs

def Calcul(info,e):
# e est une liste qui contient les bits qui seront envoyés par 
# les emetteurs
    code=[]
    for i in range(4):
        cle=randrange(8)
        val=int(info[i][cle])^int(e[i])
        code.append(info[i][:cle]+str(val)+info[i][cle+1:])
    return code

# Fonction decoder

def Decoder(info,sequence):
# l'information calculer par les emetteurs est envoyé
# aux recepteurs pour le decodage en utilisant les sequances
# de chips
    recepteur=[]
    for i in range(4):
        r=0
        for j in range(8):
            val=int(info[i][j])^int(sequence[i][j])
            r=r|val
        recepteur.append(r)
    return recepteur

    

        
    
