def stopwords_en():
    """
    :return: liste des stopwords anglais
    :rtype: list
    """
    with open("/Users/Guillaume/Documents/Informatique/Projets-git/psc/Utilitaires/stopwords_en.txt","r") as fichier:
        s = fichier.read()
    return s.split()
    
def stopwords_fr():
    with open("/Users/Guillaume/Documents/Informatique/Projets-git/psc/Utilitaires/stopwords_fr.txt","r") as fichier:
        s = fichier.read()
    return s.split()