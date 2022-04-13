from random import choice


# Lecture du fichier texte
fichierALire = open('dico.txt', 'r')
liste_brute = fichierALire.readlines()
fichierALire.close()

liste_mots = []

#Calcul longueur des chaines
for i in range (len(liste_brute)):
    ligne=liste_brute[i].rstrip('\n')
    #print(ligne)
    listeElem = ligne.split ("\t") #Si plusieurs éléments sur upne même ligne
    if i > 0:
        liste_mots.append(ligne)



def choisir_mot():
    return 'stoppa'



def recup_mot(mot_complet):     #L'argument mot_complet sert uniquement pour le test de longueur
    mot = input("Saisissez votre mot : ")
    #Regarde si le mot proposé est de la même taille que le mot à trouver
    #Il faudra également regarder si le mot fait partie de la liste_mots
    if len(mot)!=len(mot_complet):              
        print("Proposition non conforme")
        return recup_mot(mot_complet)
    mot = mot.lower()
    for i in range(len(mot)):
        if not mot[i].isalpha():    #Regarde si l'on a bien que des lettres
            print("Proposition non conforme")
            return recup_mot(mot_complet)
    return mot


def Mot_masque(mot_complet, lettres_trouvees):  #Masques le mot à trouver à partir de ce que le joueur à trouver
    mot_masque = ""
    for l in range(len(mot_complet)):
        if lettres_trouvees[l][1]==2:           #Si le statut de la lettre est 2 alors on l'affiche
            mot_masque += mot_complet[l]
        elif lettres_trouvees[l][1]==1:         #Si le statut de la lettre test 1 alors on affiche un tiret pour dire que la lettre qui se trouve à cet emplacement
            mot_masque += "*"                   #dans la proposition se trouve à un autre emplacement dans le mot (un peu tordu et pas opti)
        
        else:
            mot_masque += "."                   #Si le statut de la lettre est 0 alors c'est que la lettre proposé ne se trouve pas dans le mot
    return mot_masque


continuer_partie = "oui"

while continuer_partie != "non":                
    mot_cherche = choisir_mot()
    mot_proposes = []
    etat_lettres = []                           #etat_lettres est une lipste de la forme [['o',0],['u',1],['i',2]] où chaque lettre fait partie du mot à trouver
    for l in range(len(mot_cherche)):           #0 : la lettre ne fait partie du mot proposé
        etat_lettres.append([mot_cherche[l],0]) #1 : la lettre proposé à cet emplacement fait partie du mot mais n'est pas au bon endroit (ici ['u',1] si on a proposé toi mais pas pour uti)
        if l == 0:                              #2 : la lettre a été proposé au bon endroit
            etat_lettres[l][1]=2                            #On affiche la première lettre
        print(etat_lettres[l][0])
    

        
    mot_trouve = Mot_masque(mot_cherche, etat_lettres)      #On masque le mot 
    nb_propositions = 5
    
    while mot_cherche != mot_trouve and nb_propositions > 0:
        print("Le mot a trouver est {0} et il vous reste {1} proposition(s)".format(mot_trouve, nb_propositions))
        mot = recup_mot(mot_cherche)
        occurences = []
        k=0
        #print(len(occurences))
        for i in range(len(mot_cherche)):
            #print("i =",i)
            if len(occurences)==0:
                occurences.append([mot_cherche[i],0,0])
                occurences[k][1]=mot_cherche.count(mot_cherche[k])
                k+=1
            else:
                oui=True
                for element in occurences:
                    #print(mot_cherche[i],element[0])
                    if mot_cherche[i]==element[0]:
                        oui=False
                #print(oui)
                if oui:
                    #print('ca passe',mot_cherche[i])
                    z=0
                    for j in range(len(occurences)):
                        #print("j = ",j)
                        #print("mot_cherche[i] = ",mot_cherche[i])
                        #print("occurences[j][0] = ",occurences[j][0])
                        if mot_cherche[i]==occurences[j][0]:
                            z=1
                    #print(z)
                    if z==0:
                        occurences.append([mot_cherche[i],0,0])
                        #print(len(occurences),i)
                        #print(mot_cherche[k],mot_cherche.count(mot_cherche[k]))
                        occurences[-1][1]=mot_cherche.count(mot_cherche[i])
                        k+=1
        #print("occurences :",occurences)

             
        for i in range(len(mot)):
            if etat_lettres[i][1]==1:                           #On initialise l'état des lettres à 1 pour le mettre à 0 sinon certaine les - vont rester même s'il n'y a pas de lettre mal placée
                etat_lettres[i][1]=0

        for i in range(len(mot)):
            if mot[i]==mot_cherche[i]:
                etat_lettres[i][1]=2                             #Si la lettre proposé dans le mot est au bon emplacement son état passe à 2
                for lettre in occurences:
                    if mot[i]==lettre[0]:
                        lettre[2]+=1                             #On incrément le nombre d'apparition de la lettre

        for i in range(len(mot)):
            passe = True
            for j in range(len(mot_cherche)):                     #On va regarder si parmis les lettres proposés, certaines sont au mauvais endroit
                #print("retour")
                if mot[i]==mot_cherche[j] and etat_lettres[i][1]!=2 and passe:
                    for lettre in occurences:
                        #print("mot[i],lettre :",mot[i],lettre)
                        if mot[i] == lettre[0] and lettre[2] < lettre[1]:
                            #print("i",i)
                            etat_lettres[i][1]=1
                            passe=False
                            #print('oui')
                            lettre[2]+=1
                            #print(etat_lettres)
                                
        #print("occurences :",occurences)
                        
        #print(etat_lettres)
        nb_propositions -= 1
        mot_trouve = Mot_masque(mot_cherche, etat_lettres)
        
    if mot_cherche == mot_trouve:
        print("Bravo vous avez gagné !")
    else:
        print("Vous avez perdu !, le mot a trouver était {0}".format(mot_cherche))

    continuer_partie = input("Voulez vous continuer à jouer ? ")
    continuer_partie = continuer_partie.lower()




