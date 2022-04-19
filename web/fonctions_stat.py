from pydoc import visiblename
from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3, hashlib
from fonctions_wordle_flask import *
from fonctions_experience import *
import matplotlib.pyplot as plt
app = Flask(__name__)
from datetime import date




#-------------------------------------------------PARTIE CLASSIQUE--------------------------------------------
def recup_data(user):
    data=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Utilisateur"):
        data.append(i)
    con.commit()
    con.close()
    return(data)

def trace_histo(user):              #ET CALCULE MOYENNE
    histo=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Historique"):
        histo.append(i)
    con.commit()
    con.close()
    x=[]
    for u in histo:
        if u[1]==user and u[3]!=0:
            x.append(u[3])
    
    moyenne=0
    for u in x:
        moyenne=moyenne+u
    moyenne=str(moyenne/len(x))

    plt.clf()
    plt.hist(x, range=(0, 10), bins=10, rwidth = 0.6, align='left')
    plt.xlabel('Nombre de parties')
    plt.ylabel('Nombres X de coups')
    plt.title("Nombres de parties gagnées en X coups")
    plt.savefig('static/image.png')
    return(moyenne[:3])

def selection_joueur(user,data):
    for u in data:
        if u[1]==user:
            info=u
    nb_vict=info[4]
    nb_parties=info[4]+info[5]
    if nb_vict==0 or nb_parties==0:
        taux_vict ='0%'
    else:
        taux_vict=str((nb_vict/nb_parties)*100)
        taux_vict=taux_vict[:4]+"%"
    xp=info[6]
    return(nb_vict,nb_parties,xp,taux_vict)

#--------------------------------------------------PARTIE MDJ 1 ------------------------------------------------