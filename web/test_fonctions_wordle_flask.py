from fonctions_wordle_flask import *

def test_verif_mot():
    #Mots de longueurs différentes
    assert verif_mot("TRAUMATISME","trauma") == False
    #Mot contenant un caractère non alphabétique
    assert verif_mot("TR&UMA","trauma") == False
    #Même mot
    assert verif_mot("ARBRE","arbre") == True
    #Mot non existant de même longueur
    assert verif_mot("TATATA","trauma") == False
    #Mot existant de même longueur
    assert verif_mot("NAPPE","arbre") == True
    #Même mot mais en minuscules
    assert verif_mot("arbre","arbre") == False

def test_calcul_etat_lettres():
    #Test mêmes mots
    assert calcul_etat_lettres("ARBRE","ARBRE") == "22222"
    #Test mots totalement différents sans points communs
    assert calcul_etat_lettres("PLOUF","ARBRE") == "00000"
    #Test mots similaires
    assert calcul_etat_lettres("MOUES","MISES") == "20022"
    #Test lettres mal placées
    assert calcul_etat_lettres("LATTE","ARBRE") == "10002"
    #Test lettres mal placées, deux A sont mal placés mais le mot cherché en possède un seul
    assert calcul_etat_lettres("VISAGES","MATELAS") == "0101002"
    #Test lettre qui n'est pas dans le mot car déjà utilisée
    assert calcul_etat_lettres("AMAS","AMIS") == "2202"
    #Test toutes les lettres mal placées
    assert calcul_etat_lettres("AMIS","MISA") == "1111"