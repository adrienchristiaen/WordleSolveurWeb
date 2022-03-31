#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fichier = open('ods6.txt', 'r')
contenu = fichier.readlines()
fichier.close()

L=[[] for i in range(20)]

for i in range(len(contenu)):
    x=contenu[i][:-1]
    contenu[i]=x

for mot in contenu:
    L[len(mot)-1].append(mot)


fichier = open('liste_taille_1.txt', 'w')
fichier.write(str(len(L[0])))
for mot in L[0]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_2.txt', 'w')
fichier.write(str(len(L[1])))
for mot in L[1]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_3.txt', 'w')
fichier.write(str(len(L[2])))
for mot in L[2]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_4.txt', 'w')
fichier.write(str(len(L[3])))
for mot in L[3]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_5.txt', 'w')
fichier.write(str(len(L[4])))
for mot in L[4]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_6.txt', 'w')
fichier.write(str(len(L[5])))
for mot in L[5]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_7.txt', 'w')
fichier.write(str(len(L[6])))
for mot in L[6]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_8.txt', 'w')
fichier.write(str(len(L[7])))
for mot in L[7]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_9.txt', 'w')
fichier.write(str(len(L[8])))
for mot in L[8]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_10.txt', 'w')
fichier.write(str(len(L[9])))
for mot in L[9]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_11.txt', 'w')
fichier.write(str(len(L[10])))
for mot in L[10]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_12.txt', 'w')
fichier.write(str(len(L[11])))
for mot in L[11]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_13.txt', 'w')
fichier.write(str(len(L[12])))
for mot in L[12]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_14.txt', 'w')
fichier.write(str(len(L[13])))
for mot in L[13]:
    fichier.write("\n"+mot)
fichier.close()

fichier = open('liste_taille_15.txt', 'w')
fichier.write(str(len(L[14])))
for mot in L[14]:
    fichier.write("\n"+mot)
fichier.close()






