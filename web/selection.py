from random import choice




def ouvrir_fichier(nomFichier):
    # Lecture du fichier texte
    fichierALire = open(nomFichier, "r")
    liste_brute = fichierALire.readlines()
    fichierALire.close()

    liste_retour = []

    #Calcul longueur des chaines
    for i in range (len(liste_brute)):
        ligne=liste_brute[i].rstrip('\n')
        #print(ligne)
        if i > 0:
            liste_retour.append(ligne)
    
    return liste_retour



def choisir_mot(nombre_lettres):
    nombre_lettres = str(nombre_lettres)
    nomFichier = "Dictionnaire/liste_taille_" + nombre_lettres + ".txt"
    liste_mots = ouvrir_fichier(nomFichier)
    mot = choice(liste_mots)
    return mot
