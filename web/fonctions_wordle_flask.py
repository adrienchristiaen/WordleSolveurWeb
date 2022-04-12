from random import choice
import sqlite3


def recup_table():
    #Connexion base de données
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    #________________Récupération depuis la base de données________________#
    nb_essais=cur.execute("SELECT Nb_essais FROM Modes ")
    nb_essais=nb_essais.fetchall()
    #print("nb_essais :",nb_essais)

    nb_lettres=cur.execute("SELECT Nb_caracteres FROM Modes ")
    nb_lettres=nb_lettres.fetchall()
    #print(nb_lettres)

    mot_cherche=cur.execute("SELECT mot_cherche FROM Modes ")
    mot_cherche=mot_cherche.fetchall()
    #print(mot_cherche)

    mots_proposes=cur.execute("SELECT mots_proposes FROM Modes ")
    mots_proposes=mots_proposes.fetchall()
    #print(mots_proposes)

    etat_lettres=cur.execute("SELECT etat_lettres FROM Modes ")
    etat_lettres=etat_lettres.fetchall()
    #print(etat_lettres)

    mode_de_jeu=cur.execute("SELECT Mode_de_jeu FROM Modes ")
    mode_de_jeu=mode_de_jeu.fetchall()
    #print(mode_de_jeu)
    #______________________________________________________________________#
    return nb_essais, nb_lettres, mot_cherche, mots_proposes, etat_lettres, mode_de_jeu




def creation_liste_mots_proposes(nb_lettres,nb_essais,mots_proposes,point):
    liste_mot_propose=[]                                                   #Liste contenant tous les mots proposés par le joueur
    for i in range(len(mots_proposes)):                                    #Exemple : ['Bondir','Rouges','......','......']
        liste_mot_propose.append(mots_proposes[i][0])                      #On ajoute les mots déja proposés qui se trouvent dans la BD
    #print('avant test',liste_mot_propose)
    if liste_mot_propose[0]=='':                                           #On regarde si aucun mot n'a encore été proposé
        remplissage = nb_essais[0]-len(liste_mot_propose)                  #Jusqu'au else, le code permet de générer liste_mot_propose de la forme suivante :
        for j in range(remplissage):                                       #liste_mot_propose = [('.'*nb_lettres)*nb_essais]
            liste_mot_propose.append('')
        for k in range (len(liste_mot_propose)):
            if liste_mot_propose[k]=='':
                liste_mot_propose[k]=point*nb_lettres
    else:
        #print('else',liste_mot_propose)                                   #Si la liste contient déja un mot
        liste_mot_propose.reverse()                                        #On l'inverse ['Bonjour','']  => ['','Bonjour']
        liste_mot_propose.pop(0)                                           #On spprime l'élément 0 => ['Bonjour']
        #print(liste_mot_propose)
        remplissage = nb_essais[0]-len(liste_mot_propose)                  #On remplit selon la même méthode au-dessus
        for i in range(remplissage):
            liste_mot_propose.append('')
        for k in range (len(liste_mot_propose)):
            if liste_mot_propose[k]=='':
                liste_mot_propose[k]=point*nb_lettres
    return liste_mot_propose


def creation_liste_etat_lettres(nb_lettres,nb_essais,etat_lettres,zero):
    liste_etat_lettres=[]                                                  #Liste contenant l'état des lettres de tous les mots proposés
    for i in range(len(etat_lettres)):                                     #Exemple : ['221001','201102','000000','000000']
        liste_etat_lettres.append(etat_lettres[i][0])                      #On ajoute les etats de lettre déja proposés qui se trouvent dans la BD
    #print('avant test',liste_etat_lettres)
    if liste_etat_lettres[0]=='':
        remplissage = nb_essais[0]-len(liste_etat_lettres)                 #Même méthode que pour liste_mots_proposes
        for j in range(remplissage):
            liste_etat_lettres.append('')
        for k in range (len(liste_etat_lettres)):               
            if liste_etat_lettres[k]=='':
                liste_etat_lettres[k]=zero*nb_lettres                      #liste_etat_lettres = [('0'*nb_lettres)*nb_essais]
        #print('if',liste_etat_lettres)
    else:
        liste_etat_lettres.reverse()
        liste_etat_lettres.pop(0)
        #print(liste_mot_propose)
        remplissage = nb_essais[0]-len(liste_etat_lettres)
        for i in range(remplissage):
            liste_etat_lettres.append('')
        for k in range (len(liste_etat_lettres)):
            if liste_etat_lettres[k]=='':
                liste_etat_lettres[k]=zero*nb_lettres
    #print('else',liste_etat_lettres)
    return liste_etat_lettres



def place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point):
    #_______________________Place la première lettre_______________________#
    test=True
    #print(test,liste_mot_propose)
    for i in range(len(liste_mot_propose)):
        if liste_mot_propose[i] == point*nb_lettres and test:                   #Place la première lettre uniquement pour le prochain mot :
            liste_mot_propose[i]=mot_cherche[0]+point*(nb_lettres-1)            #mot_cherche = 'PYTHON'
            test=False                                                          #liste_mot_propose = ['ROULER','P.....','......']                                          
            #print('ca passe')  
    #print(liste_mot_propose)
    #______________________________________________________________________#
    return liste_mot_propose 



def calcul_etat_lettres(mot_cherche, mot_propose):
    etat_lettres=''
    liste_de_test =[]
    for l in range(len(mot_propose)):           #0 : la lettre ne fait partie du mot proposé
        liste_de_test.append([mot_propose[l],0]) #1 : la lettre proposé à cet emplacement fait partie du mot mais n'est pas au bon endroit (ici ['u',1] si on a proposé toi mais pas pour uti)
    #print(liste_de_test)

    for i in range(len(mot_propose)):
        if liste_de_test[i][1]==1:           #On initialise l'état des lettres à 1 pour le mettre à 0 sinon certaine les - vont rester même s'il n'y a pas de lettre mal placée
            liste_de_test[i][1]=0

        if mot_propose[i]==mot_cherche[i]:          #Si la lettre proposé dans le mot est au bon emplacement son état passe à 2
            liste_de_test[i][1]=2

        else:
            for j in range(len(mot_cherche)):                           #On va regarder si parmis les lettres proposés, certaines sont au mauvais endroit
                if mot_propose[i]==mot_cherche[j] and liste_de_test[j][1]!=2:    
                    liste_de_test[i][1]=1
    for i in range(len(liste_de_test)):
        etat_lettres+=str(liste_de_test[i][1])
    #print(etat_lettres)
    return etat_lettres





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