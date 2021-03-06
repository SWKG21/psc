import sys
sys.path.append("/Users/Guillaume/Documents/Informatique/Projets-git/psc")
from time import time
d = time()

from classes import *
from carac_gramm import *
from carac_lettres import *
from carac_ponct import *
from carac_complexite import *
from carac_stopwords import *
from Apprentissage.svm import SVM
from Apprentissage.reseau_textes import reseau_neurones

oeuvres_training =[("hamilton",k) for k in range(1,52)] + [("madison",k) for k in range(1,20)] 
oeuvres_eval = [("madison",k) for k in range(31,41)] 
analyseur = Analyseur([freq_gram, freq_ponct, freq_stopwords])
classifieur = SVM()
P = Probleme(oeuvres_training, oeuvres_eval, 1000, analyseur, classifieur, langue = "en", full_text = True)

P.creer_textes(equilibrage = True)
P.analyser(normalisation = False)
P.appliquer_classifieur()
P.interpreter()
P.afficher()



f = time()
print()
print("Temps d'exécution : " + str(f-d) + "s")