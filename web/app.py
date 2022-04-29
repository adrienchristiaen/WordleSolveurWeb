from pydoc import visiblename
from flask import Flask, render_template, redirect, request, url_for, flash, session, g, json
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3, hashlib, random
from fonctions_wordle_flask import *
from fonctions_experience import *
from fonctions_stat import *
import matplotlib.pyplot as plt
app = Flask(__name__)
from datetime import date

#Configuration
app.config.update(
    DEBUG = True,
    SECRET_KEY = "choose_a_secret_key"
)

#Mise en place de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#Modèle d'utilisateur
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "%d" % (int(self.id))
    
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

#Callback
@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == "__main__":
    app.run()

global point, zero
point = '.'
zero = '0'


#Accueil
@app.route('/')
@app.route('/accueil',methods=['GET','POST'])
def accueil(nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[],vie=None,score_survie=None,nb_essais_big50=None,score_big50=None,timer1=None,timer2=None,score_clm=None):
    #Connexion base de données
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()

    #________________Récupération depuis la base de données________________#
    nb_essais = recup_table()[0]

    nb_lettres = recup_table()[1]
    nb_lettres = nb_lettres[0][0]                                          #Idem mot_cherche

    mot_cherche = recup_table()[2]
    mot_cherche = mot_cherche[0][0]                                        #On prend le premier élément de la liste mot_cherche (tous les éléments sont identiques)

    mots_proposes = recup_table()[3]

    etat_lettres = recup_table()[4]

    mode_de_jeu = recup_table()[5]
    mode_de_jeu =  mode_de_jeu[0][0]
    
    vie = recup_table()[6]
    vie =  vie[0][0]

    score_survie = recup_table()[7]
    
    nb_essais_big50 = recup_table()[8]

    score_big50 = recup_table()[9]
    score_big50 =  score_big50[0][0]

    depart_clm = recup_table()[10]
    depart_clm = depart_clm[0][0]

    score_clm = recup_table()[11]
    score_clm =  score_clm[0][0]
    #______________________________________________________________________#

    #__________________Mise des tuples sous forme de liste_________________#
    for i in range(len(nb_essais)):
        nb_essais[i]=nb_essais[i][0]                                       #On passe d'une liste de la forme [(5,)(6,)] à [5,6]
    nb_essais.reverse()                                                    #Car je souhaite une liste décroissant : [5,6] => [6,5]
    #print("nb_essais :",nb_essais)
    for i in range(len(score_survie)):
        score_survie[i]=score_survie[i][0]                                       #On passe d'une liste de la forme [(3,)(0,)] à [3,0]
    score_survie.reverse()                                                    #Car je souhaite une liste décroissant : [0,3] => [0,3]
    #print("score_survie :",score_survie)
    for i in range(len(nb_essais_big50)):
        nb_essais_big50[i]=nb_essais_big50[i][0]                                       #On passe d'une liste de la forme [(49,)(50,)] à [49,50]
    nb_essais_big50.reverse()                                                    #Car je souhaite une liste décroissant : [50,49] => [50,49]
    #print("nb_essais_big50 :",nb_essais_big50)
    #______________________________________________________________________#

    #______________Initialisation des listes pour le tableau_______________#
    liste_mot_propose = creation_liste_mots_proposes(nb_lettres,nb_essais,mots_proposes,point)
    #print('liste_mot_propose :',liste_mot_propose)

    liste_etat_lettres = creation_liste_etat_lettres(nb_lettres,nb_essais,etat_lettres,zero)
    #print('liste_etat_lettres :',liste_etat_lettres)
    #______________________________________________________________________#

    #_________________Actualisation de la barre d'expérience_______________#
    #Cette fonctionnalité est réservée au joueurs connectés
    if current_user.is_authenticated:
        #Connexion BD
        con=sqlite3.connect('wordle.sql')
        cur = con.cursor()
        #Expérience joueur
        req = cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur = (?)", ([session['username']]))
        elements = req.fetchall()
        xp = elements[0][0]
        #Calcul niveau joueur
        lvl = level_function(xp)
        #Infos expériences
        L_info_xp = lvl_info(xp)
        #Pourcentage de progression
        progress = int(L_info_xp[1]/L_info_xp[2]*100)
    
    #Valeurs par défaut
    if not current_user.is_authenticated:
        xp, lvl, L_info_xp, progress = 0,0,[0,0,0],0
    #______________________________________________________________________#

    #____________Si la partie commmence pour chaque mode de jeu____________#
    if mot_cherche=='':
        mot_propose = ''
        etat_lettres = ''
        #print("etat_lettres",etat_lettres)
        mot_cherche=choisir_mot(nb_lettres)
        cur.execute("DELETE FROM Partie WHERE mot_cherche=('') ")
        cur.execute("INSERT INTO Partie VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu,vie,score_survie[-1],nb_essais_big50[-1],score_big50,depart_clm,score_clm)) 
        con.commit()
    #______________________________________________________________________#

    #__________________Si on commence un contre la montre__________________#

    #______________On sauvegarde le temps du début de partie_______________#
    if depart_clm == '' and mode_de_jeu =='clm':
        depart_clm = depart()
        cur.execute("DELETE FROM Partie WHERE Clm_depart=('') ")
        cur.execute("INSERT INTO Partie VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu,vie,score_survie[-1],nb_essais_big50[-1],score_big50,depart_clm,score_clm)) 
        con.commit()
    #______________________________________________________________________#

    #________On capture le temps actuel pour calculer le timer_____________#    
    if mode_de_jeu =='clm':
        timer=chrono(depart_clm)[0]
        timer_dyn = chrono(depart_clm)[1]
        #print(timer,depart_clm,'yup')
    else:
        timer_dyn=0
        timer = '00:00'
    #______________________________________________________________________#

    #______________________________________________________________________#

    #________________Si le joueur vient de proposer un mot_________________#
    if request.method == "POST":
        if mode_de_jeu != 'clm':
            liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point)       #On place la première lettre dans le mot a deviné
        else:
            if chrono(depart_clm)[0] != '00:00' or nb_essais[0]!=6:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point)       #On place la première lettre dans le mot a deviné
        print("\n##############################")
        print("Le mot à trouver est : ",mot_cherche)
        mot_propose=request.form.get("mot_propose")
        mot_propose = mot_propose.upper()

        #_________________Si le mot proposé est de la bonne forme__________________#
        if verif_mot(mot_propose,mot_cherche):                                  #Voir fonction verif_mot
            #print(nb_essais[0],nb_essais[-1], nb_essais[0]-nb_essais[-1])
            liste_mot_propose[nb_essais[0]-nb_essais[-1]] = mot_propose         #Ajoute le mot proposé dans la liste liste_mot_propose
            #print(nb_essais)
            #print(liste_mot_propose)

            print("Le mot proposé est : ",mot_propose)

            etat_lettres = calcul_etat_lettres(mot_cherche, mot_propose)        #Calcul de l'état des lettres
            
            liste_etat_lettres[nb_essais[0]-nb_essais[-1]] = etat_lettres       #On ajoute l'état des lettres du mot dans la liste liste_etat_lettres
            #print(liste_etat_lettres)
            print("Placement des lettres :", etat_lettres)
            print("##############################\n")
            nb_essais.append(nb_essais[-1]-1)                                   #On décrémente le nombre d'essai restant
            #print(liste_etat_lettres[nb_essais[0]-nb_essais[-1]-1])
            
            #__Si le mode de jeu est big50, on décrémente le nombre total d'essais__#
            if mode_de_jeu=='big50':
                nb_essais_big50.append(nb_essais_big50[-1]-1)
            #_______________________________________________________________________#

            #____________________Mise à jour de la table de Jeu_____________________#
            if etat_lettres == '2'*nb_lettres:
                if mode_de_jeu == 'survie':
                    score_survie.append(score_survie[-1]+nb_essais[-1]+1)
                if mode_de_jeu == 'big50':
                    score_big50+=1
                if mode_de_jeu == 'clm':
                    score_clm+=1
            
            if nb_essais[-1]==0:
                if mode_de_jeu == 'survie':
                    vie-=1
            cur.execute("INSERT INTO Partie VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu,vie,score_survie[-1],nb_essais_big50[-1],score_big50,depart_clm,score_clm)) 
            con.commit()
            #_______________________________________________________________________#

            #_________On met à jour les stats si l'utilisateur est connecté_________#
            if current_user.is_authenticated:
                user=session["username"]
                if mode_de_jeu == 'classique':
                    if etat_lettres == '2'*nb_lettres:
                        nb_victoires=cur.execute("SELECT Nb_victoires_classique FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        nb_victoires=nb_victoires.fetchall()[0][0]
                        #print("nb_victoires",nb_victoires)
                        nb_victoires+=1
                        experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        experience=experience.fetchall()[0][0]
                        #print("experience",experience)
                        experience+=250*(nb_lettres/5)
                        #print("experience",experience)
                        cur.execute("UPDATE Utilisateur SET Nb_victoires_classique = (?), Experience = (?) WHERE Nom_utilisateur=(?)",(nb_victoires,experience,user))
                        id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                        id_partie=id_partie.fetchall()[0][0]
                        date_partie=str(date.today())[5:]+"-"+str(date.today())[:4]
                        Partie=[id_partie,user,'Vrai',nb_essais[0]-nb_essais[-1],date_partie,'Classique',mot_cherche]  #ajout a la table historique
                        cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                        con.commit()
                        #Mise à jour des succès classiques
                        nb_coups = nb_essais[0]-nb_essais[-1]
                        score_survie = score_survie[-1]
                        maj_succes(experience, user, vie, score_big50, nb_coups, nb_victoires, score_survie)
                        
                    else:
                        if nb_essais[-1]==0:
                            nb_defaites=cur.execute("SELECT Nb_defaites_classique FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                            nb_defaites=nb_defaites.fetchall()[0][0]
                            #print("nb_defaites",nb_defaites)
                            nb_defaites+=1

                            experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                            experience=experience.fetchall()[0][0]
                            #print("experience",experience)
                            experience+=10*(nb_lettres/5)

                            cur.execute("UPDATE Utilisateur SET Nb_defaites_classique = (?), Experience = (?) WHERE Nom_utilisateur=(?)",(nb_defaites,experience,user))
                            id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                            id_partie=id_partie.fetchall()[0][0]
                            date_partie=str(date.today())[5:]+"-"+str(date.today())[:4]
                            Partie=[id_partie,user,'Faux',nb_essais[0]-nb_essais[-1],date_partie,'Classique',mot_cherche]  #ajout a la table historique
                            cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                            con.commit()

                if mode_de_jeu == 'survie':
                    if vie == 0:
                        experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        experience=experience.fetchall()[0][0]
                        #print("experience",experience)
                        experience+=75*score_survie[-1]
                        #print("experience",experience)
                        cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,user))                       
                        id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                        id_partie=id_partie.fetchall()[0][0]
                        date_partie=str(date.today())[5:]+"-"+str(date.today())[:4]
                        Partie=[id_partie,user,'Vrai',score_survie[-1],date_partie,'Survie',"NOPE"]  #ajout a la table historique
                        cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                        con.commit()
                        #Mise à jour des succès survie
                        nb_victoires, nb_coups = 0, 0#Initialisation
                        score_survie = score_survie[-1]
                        maj_succes(experience, user, vie, score_big50, nb_coups, nb_victoires, score_survie)
                        
                if mode_de_jeu == 'big50':
                    if nb_essais_big50[-1] == 0:
                        experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        experience=experience.fetchall()[0][0]
                        #print("experience",experience)
                        experience+=250*score_big50
                        #print("experience",experience)
                        cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,user))
                        id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                        id_partie=id_partie.fetchall()[0][0]
                        date_partie=str(date.today())[5:]+"-"+str(date.today())[:4]
                        Partie=[id_partie,user,'Vrai',score_big50,date_partie,'Big 50',"NOPE"]  #ajout a la table historique
                        cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                        con.commit()
                        #Mise à jour des succès big50
                        nb_victoires, nb_coups = 0, 0#Initialisation
                        score_survie = score_survie[-1]
                        maj_succes(experience, user, vie, score_big50, nb_coups, nb_victoires, score_survie)
        
            #_______________________________________________________________________#
            if etat_lettres == '2'*nb_lettres:
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)
            else:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)
        
        #La distrubution d'expérience/succès pour les Partie avec timer doit se faire en dehors de la vérification des mots
        if current_user.is_authenticated and mode_de_jeu == 'clm' and chrono(depart_clm)[0] == '00:00':
            #print('oui')
            user=session["username"]
            experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
            experience=experience.fetchall()[0][0]
            #print("experience",experience)
            experience+=250*score_clm
            #print("experience",experience)
            cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,user))
            con.commit()
            #Mise à jour des succès clm
            maj_succes_clm(user, experience,score_clm)
            #Renvoi vers l'accueil
            if etat_lettres == '2'*nb_lettres:
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)
            else:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)

        else:
            #print("mot non valide")
            print("Le mot proposé est : ", mot_propose)
            print("##############################\n")
            return render_template("accueil_fail.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)
        
    else:
        print("Le mot à trouver est : ",mot_cherche)
        print("##############################\n")
        if len(etat_lettres)!=0:
            etat_lettres = etat_lettres[0][0]
        
        if mode_de_jeu == 'classique' or mode_de_jeu =='survie':
            if etat_lettres != '2'*nb_lettres:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
        if mode_de_jeu == 'big50' and nb_essais_big50 !=0:
            if etat_lettres != '2'*nb_lettres:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
        if mode_de_jeu == 'clm' and chrono(depart_clm)[0] == '00:00':
            if etat_lettres != '2'*nb_lettres:
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
        return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50,timer1=timer,timer2=json.dumps(timer_dyn),score_clm=score_clm, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp)








#Fonction qui permet de rejouer
@app.route('/rejouer',methods=['GET','POST'])
def rejouer():
    connection = sqlite3.connect('wordle.sql')
    cur = connection.cursor()
    #________________Récupération depuis la base de données________________#
    nb_essais = recup_table()[0]
    nb_essais = nb_essais[-1][0] 

    nb_lettres = recup_table()[1]
    nb_lettres = nb_lettres[0][0]                                         

    mot_cherche = recup_table()[2]
    mot_cherche = mot_cherche[0][0]                                        
    
    mode_de_jeu = recup_table()[5]
    mode_de_jeu =  mode_de_jeu[0][0]

    vie = recup_table()[6]
    vie =  vie[0][0]

    score_survie = recup_table()[7]
    score_survie = score_survie[0][0]

    nb_essais_big50 = recup_table()[8]
    nb_essais_big50 =  nb_essais_big50[0][0]

    score_big50 = recup_table()[9]
    score_big50 = score_big50[0][0]

    depart_clm = recup_table()[10]
    depart_clm =  depart_clm[0][0]

    score_clm = recup_table()[11]
    score_clm =  score_clm[0][0]
    #______________________________________________________________________#

    #_____________________On supprime la table de Jeu______________________#
    cur.execute('''DELETE FROM Partie;''')
    #______________________________________________________________________#

    #_____________On actualise la table selon le mode de jeu_______________#
    if mode_de_jeu == 'classique' or (mode_de_jeu == 'survie' and vie == 0) or (mode_de_jeu == 'big50' and nb_essais_big50 == 0) or (mode_de_jeu == 'clm' and chrono(depart_clm)[0]) == '00:00':
        cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,3,0,50,0,'',0))
        connection.commit()
    if mode_de_jeu == 'survie' and vie !=0 :
        nb_lettres = random.randint(5, 8)
        cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,vie,score_survie,50,0,'',0))
        connection.commit()
    if mode_de_jeu == 'big50' and nb_essais_big50 !=0 :
        nb_lettres = random.randint(5, 8)
        cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,3,0,nb_essais_big50,score_big50,'',0))
        connection.commit()
    if mode_de_jeu == 'clm' and chrono(depart_clm)[0] != '00:00':
        nb_lettres = random.randint(5, 8)
        cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,3,0,50,0,depart_clm,score_clm))
        connection.commit()
    #______________________________________________________________________#

    return redirect("accueil")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comment jouer
@app.route('/comment-jouer')
def regle():
    return render_template("comment-jouer.html")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Statistiques Classique
@app.route('/statistiques')
@app.route('/statistiques-classique')
@login_required
def stat():
    user=session["username"]
    #Connection a la bdd
    data=recup_data(user)
    #Selection des stats d'un joueur en particulier
    nb_vict,nb_parties,xp,taux_vict=selection_joueur(user,data)
    #Tracer histogramme
    moyenne,meilleur,inutile,inutile=trace_histo(user,"Classique")
    histo_histo(user,"Classique")

    return render_template("statistiques.html", liste=[nb_parties,nb_vict,taux_vict,xp,moyenne,meilleur])



#Statistiques Survie
@app.route('/statistiques-survie')
@login_required
def stat_survie():
    user=session["username"]
    #Connection a la bdd
    data=recup_data(user)
    #Selection des stats d'un joueur en particulier
    nb_vict,nb_parties,xp,taux_vict=selection_joueur(user,data)
    #Tracer histogramme
    moyenne,inutile,meilleur,nb_parties=trace_histo(user,"Survie")
    histo_histo(user,"Survie")

    return render_template("statistiques-survie.html", liste=[nb_parties,nb_vict,taux_vict,xp,moyenne,meilleur])

#Statistiques Big50
@app.route('/statistiques-big50')
@login_required
def stat_big50():
    user=session["username"]
    #Connection a la bdd
    data=recup_data(user)
    #Selection des stats d'un joueur en particulier
    nb_vict,nb_parties,xp,taux_vict=selection_joueur(user,data)
    #Tracer histogramme
    moyenne,inutile,meilleur,nb_parties=trace_histo(user,"Big50")
    histo_histo(user,"Big50")

    return render_template("statistiques-big50.html", liste=[nb_parties,nb_vict,taux_vict,xp,moyenne,meilleur])


#Statistiques CLM
@app.route('/statistiques-clm')
@login_required
def stat_clm():
    user=session["username"]
    #Connection a la bdd
    data=recup_data(user)
    #Selection des stats d'un joueur en particulier
    nb_vict,nb_parties,xp,taux_vict=selection_joueur(user,data)
    #Tracer histogramme
    moyenne,inutile,meilleur,nb_parties=trace_histo(user,"CLM")
    histo_histo(user,"CLM")

    return render_template("statistiques-clm.html", liste=[nb_parties,nb_vict,taux_vict,xp,moyenne,meilleur])


#Historique
@app.route('/historique', methods=['GET', 'POST'])
@login_required
def histo():
    user=session["username"]
    histo=[]
    histo_perso=[]

    #Connection a la bdd
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Historique"):
        histo.append(i)
    con.commit()
    con.close()

    #Trie dans les donnees
    for u in histo:
        if u[1]==user:
            histo_perso.append(list(u))
    for u in histo_perso:                       #Change le valeur "Vrai" en "Victoire" pour affichage
        if u[2]=="Vrai":
            u[2]="Victoire"
        else:
            u[2]="Défaite"
    histo_perso.reverse()
    return render_template("historique.html",histo=histo_perso)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Succès
@app.route('/succes')
@login_required
def succes():
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    req = cur.execute("SELECT * FROM Quetes")
    quetes = req.fetchall()
    #print(quetes)
    req = cur.execute("SELECT * FROM Quetes_rea WHERE Identifiant = (?)", ([session['username']]))
    quetes_rea = req.fetchall()
    #print(quetes_rea)
    length = len(quetes)
    return render_template("succes.html", length=length, quetes=quetes, quetes_rea=quetes_rea)


#Mode de jeu/Paramètres
@app.route('/parametres',methods=['GET','POST'])
def parametres():
    if request.method == "POST":
        #Informations du formulaire
        select_essais=request.form.get("select_essais")
        select_lettres=request.form.get("select_lettres")
        select_mode_de_jeu=request.form.get("select_mode_de_jeu")
        solo = request.form.get("solo")
        multi = request.form.get("multi")
        #Connexion base de données
        con=sqlite3.connect('wordle.sql')
        cur = con.cursor()
        cur.execute('''DELETE FROM Partie;''')
        #print(nb_essais,nb_lettres,mode_de_jeu)
        if select_mode_de_jeu == 'classique':
            cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(select_essais,select_lettres,'','','',select_mode_de_jeu,3,0,50,0,'',0))
            con.commit()
        else:
            select_essais = 6
            select_lettres = random.randint(5, 8)
            cur.execute("INSERT INTO Partie VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(select_essais,select_lettres,'','','',select_mode_de_jeu,3,0,50,0,'',0))
            con.commit()
        if not multi == None:
            return render_template("construction.html")
        if not solo == None:
            return redirect("accueil")
    return render_template("parametres.html")

#Inscription/Connexion/Déconnexion ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == "POST":
        #Informations du formulaire
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        #Encodage du mot de passe
        password = hashlib.sha224(bytes(password,encoding='utf-8')).hexdigest()
        #Connexion base de données•••••••••••••••
        con = sqlite3.connect('wordle.sql')
        cur = con.cursor()
        #Vérification de l'unicité de l'utilisateur
        req = cur.execute("SELECT COUNT(Nom_utilisateur) FROM Utilisateur WHERE Nom_utilisateur = (?)", ([username]))
        count = req.fetchone()[0]
        if count != 0:
            flash("Ce nom d'utilisateur est déjà utilisé. Choisissez en un autre.")
        else:
            #Vérification de l'unicité de l'adresse email
            req = cur.execute("SELECT COUNT(Email) FROM utilisateur WHERE Email = (?)", ([email]))
            count = req.fetchone()[0]
            if count != 0:
                flash("Cet email est déjà utilisé. Choisissez en un autre.")
            else:
                #Comptage du nombre d'utilisateurs
                req = cur.execute("SELECT COUNT(Nom_utilisateur) FROM utilisateur")
                num = req.fetchone()[0] + 1
                #Sélection au hasard de la photo de profil
                photo = 'profil'+str(random.randint(1,10))
                #Insertion de l'utilisateur dans la BD
                cur.execute("INSERT INTO utilisateur(Id, Nom_utilisateur, Mot_de_passe, Email, Nb_victoires_classique, Nb_defaites_classique, Experience, Photo) VALUES (?,?,?,?,?,?,?,?)", (num, username, password, email, 0, 0, 0,photo))#Certaines données s'initialisent à zéro (nb parties, xp...)
                con.commit()
                #Création du compte et connexion
                session['username'] = username
                user = User(id = num)
                login_user(user)
                flash("Votre nouveau compte a été créé avec succès !")
                #Initialisation des quêtes dans la base de données
                req = cur.execute("SELECT COUNT(Id_quete_rea) FROM Quetes_rea")
                nb_quetes_rea = req.fetchone()[0] + 1
                req = cur.execute("SELECT COUNT(Id_quete) FROM Quetes")
                nb_quetes = req.fetchone()[0]
                for k in range(nb_quetes):
                    cur.execute("INSERT INTO Quetes_rea VALUES(?, ?, ?,FALSE)", ([nb_quetes_rea+k, k, session['username']]))
                con.commit()
                return redirect("accueil")

    return render_template('inscription.html')

#Connexion
@app.route('/login')
def login():
    return redirect("connexion")

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == "POST":
        #Informations du formulaire
        username = request.form.get("username")
        password = request.form.get("password")
        #Encodage du mot de passe
        password = hashlib.sha224(bytes(password,encoding='utf-8')).hexdigest()
        #Connexion base de données
        con = sqlite3.connect('wordle.sql')
        cur = con.cursor()
        #Vérification de la validité username + pwd
        req = cur.execute("SELECT COUNT(Nom_utilisateur) FROM Utilisateur WHERE Nom_utilisateur = (?)", ([username]))
        count = req.fetchone()[0]
        if count == 0:
            flash("Ce nom d'utilisateur n'existe pas. Veuillez réessayer.")
        else:
            req = cur.execute("SELECT Mot_de_passe FROM Utilisateur WHERE Nom_utilisateur = (?)", ([username]))
            pwd = req.fetchone()[0]
            if password != pwd:
                flash("Mauvais mot de passe. Veuillez réessayer.")
            else:
                #Récupération de l'identifiant associé à l'utilisateur
                req = cur.execute("SELECT Id FROM Utilisateur WHERE Nom_utilisateur = (?)", ([username]))
                num = req.fetchone()[0]
                #Connexion de l'utilisateur
                session['username'] = username
                user = User(id = num)
                login_user(user)
                flash("Vous vous êtes connecté avec succès !")
                return redirect("accueil")

    return render_template('connexion.html')

#Déconnexion
@app.route("/deconnexion")
@login_required
def deconnexion():
    session.pop('username', None)
    logout_user()
    flash("Vous vous êtes déconnecté avec succès. A la prochaine !")
    return redirect("accueil")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Profil
@app.route("/profil")
@login_required
def profil():
    #Connexion BD
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    #Expérience joueur
    req = cur.execute("SELECT Email, Experience, Photo FROM Utilisateur WHERE Nom_utilisateur = (?)", ([session['username']]))
    elements = req.fetchall()
    email, xp, photo = elements[0][0], elements[0][1], elements[0][2]
    #print("photo",photo)
    #Calcul niveau joueur
    lvl = level_function(xp)
    #Infos expériences
    L_info_xp = lvl_info(xp)
    #Pourcentage de progression
    progress = int(L_info_xp[1]/L_info_xp[2]*100)
    return render_template('profil.html', email=email, lvl=lvl, L_info_xp=L_info_xp, progress=progress, xp=xp, photo=photo)
