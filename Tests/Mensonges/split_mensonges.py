#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append("/Users/Guillaume/Documents/Informatique/psc")
from classes import *
import numpy.random as rd

def split():
    with open("/Users/Guillaume/Google Drive/Cours X/PSC/Groupe PSC/Corpus/Francais/Fichiers txt/mensongeX0.txt","rb") as fichier:
        T = fichier.read().decode("utf-8")
        TS = T.split("\n")
    for k in range(len(TS)):
        if (k%2==0):
            t = TS[k].encode("utf-8")
            with open("/Users/Guillaume/Google Drive/Cours X/PSC/Groupe PSC/Corpus/Francais/Fichiers txt/mensongeX"+str(k//2 + 1)+".txt", "wb") as fichier:
                fichier.write(t)
                    
def shake():
    with open("/Users/Guillaume/Google Drive/Cours X/PSC/Groupe PSC/Corpus/Francais/Fichiers txt/mensongeY0.txt","rb") as fichier:
        T = fichier.read().decode("utf-8")
        TS = T.split(".")
        TS2 = list(rd.permutation(TS))
        for k in range(len(TS2)):
            TS2[k] += "."
        T2 = "".join(TS2)
        
    with open("/Users/Guillaume/Google Drive/Cours X/PSC/Groupe PSC/Corpus/Francais/Fichiers txt/mensongeYshake.txt", "wb") as fichier:
        fichier.write(T2.encode("utf-8"))
                    