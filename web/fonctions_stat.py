from pydoc import visiblename
from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3, hashlib
from fonctions_wordle_flask import *
from fonctions_experience import *
import matplotlib.pyplot as plt
app = Flask(__name__)
from datetime import date




def recup_data(user):
    data=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    data = cur.execute("SELECT * FROM Utilisateur WHERE Nom_utilisateur = (?)", ([user]))
    data = list(data.fetchall()[0])
    print(data)
    con.commit()
    con.close()
    return(data)

def trace_histo(user,mdj):              #ET CALCULE MOYENNE
    histo=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Historique WHERE Identifiant = (?) AND Mode_de_jeu = (?)", ([user,mdj])):
        histo.append(i)
    con.commit()
    con.close()
    nb_partie=len(histo)
    x=[]
    for u in histo:
        if  u[3]!=0:
            x.append(u[3])
    
    moyenne=0
    for u in x:
        moyenne=moyenne+u
    if len(x)!=0:
        moyenne=(moyenne/len(x))
    moyenne=str(moyenne)
    if len(moyenne)>=4:
        moyenne=moyenne[:3]
    
    if x==[]:
        meilleur_classique=0
        meilleur_score=0
    else:
        meilleur_classique=min(x)
        meilleur_score=max(x)

    plt.clf()
    plt.hist(x, range=(0, 10), bins=10, rwidth = 0.6, align='left')
    plt.ylabel('Nombre de parties')
    if mdj=="Classique":
        plt.xlabel('Nombres X de coups')
        plt.title("Nombres de parties gagnées en X coups")
    else:
        plt.xlabel('Score')
        plt.title("Scores des différentes parties")
    plt.savefig('static/image.png',transparent=True)
    return(moyenne,meilleur_classique,meilleur_score,nb_partie)

def selection_joueur(user,data):
    nb_vict=data[4]
    nb_parties=data[4]+data[5]
    if nb_vict==0 or nb_parties==0:
        taux_vict ='0%'
    else:
        taux_vict=str((nb_vict/nb_parties)*100)
        taux_vict=taux_vict[:4]+"%"
    xp=data[6]
    return(nb_vict,nb_parties,xp,taux_vict)


def histo_histo(user,mdj):
    histo=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Historique WHERE Identifiant = (?) AND Mode_de_jeu = (?)", ([user,mdj])):
        histo.append(i)
    con.commit()
    con.close()
    histo=histo[-5:]
    x=[]
    y=[]

    for u in histo:
        y.append(u[3])
        x.append(u[4])

    x_test=[i for i in range(1,len(x)+1)]
    print(x)
    print(y)

    plt.clf()
    plt.plot(x_test,y,marker="o")
    plt.xticks(x_test,x)
    plt.xlabel('')
    plt.ylabel('Score')
    plt.title("Progression sur les 5 dernières parties")
    plt.savefig('static/image2.png',transparent=True)





















