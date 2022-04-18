from pydoc import visiblename
from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3, hashlib
from fonctions_wordle_flask import *
from fonctions_experience import *
import matplotlib.pyplot as plt
app = Flask(__name__)

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

def verif_mot(mot_propose,mot_cherche):     #L'argument mot_complet sert uniquement pour le test de longueur
    #Regarde si le mot proposé est de la même taille que le mot à trouver
    #Il faudra également regarder si le mot fait partie de la liste_mots
    if len(mot_propose)!=len(mot_cherche):              
        return False
    for i in range(len(mot_propose)):
        if not mot_propose[i].isalpha():    #Regarde si l'on a bien que des lettres
            return False
    return True


#Accueil
@app.route('/')
@app.route('/accueil',methods=['GET','POST'])
def accueil(nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[],vie=None,score_survie=None,nb_essais_big50=None,score_big50=None):
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
    #______________________________________________________________________#
    
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
    

    #__________________Mise des tuples sous forme de liste_________________#
    liste_mot_propose = creation_liste_mots_proposes(nb_lettres,nb_essais,mots_proposes,point)
    print('liste_mot_propose :',liste_mot_propose)

    liste_etat_lettres = creation_liste_etat_lettres(nb_lettres,nb_essais,etat_lettres,zero)
    print('liste_etat_lettres :',liste_etat_lettres)
    #______________________________________________________________________#

    #___________________________Si la partie commmence_____________________#
    if mot_cherche=='':
        mot_propose = ''
        etat_lettres = ''
        #print("etat_lettres",etat_lettres)
        mot_cherche=choisir_mot(nb_lettres)
        cur.execute("DELETE FROM Modes WHERE mot_cherche=('') ")
        cur.execute("INSERT INTO Modes VALUES (?,?,?,?,?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu,vie,score_survie[-1],nb_essais_big50[-1],score_big50)) 
        con.commit()
    #______________________________________________________________________#
    
    if request.method == "POST":
        liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point)       #On place la première lettre dans le mot a deviné
        print("Le mot à trouver est : ",mot_cherche)
        mot_propose=request.form.get("mot_propose")
        if verif_mot(mot_propose,mot_cherche):                                  #Voir fonction verif_mot
            mot_propose = mot_propose.upper()
            #print(nb_essais[0],nb_essais[-1], nb_essais[0]-nb_essais[-1])
            liste_mot_propose[nb_essais[0]-nb_essais[-1]] = mot_propose         #Ajoute le mot proposé dans la liste liste_mot_propose
            print(nb_essais)
            #print(liste_mot_propose)

            print("Le mot proposé est : ",mot_propose)

            etat_lettres = calcul_etat_lettres(mot_cherche, mot_propose)        #Calcul de l'état des lettres
            
            liste_etat_lettres[nb_essais[0]-nb_essais[-1]] = etat_lettres       #On ajoute l'état des lettres du mot dans la liste liste_etat_lettres
            print(liste_etat_lettres)
            nb_essais.append(nb_essais[-1]-1)                                   #On décrémente le nombre d'essai restant
            print(liste_etat_lettres[nb_essais[0]-nb_essais[-1]-1])
            if mode_de_jeu=='big50':
                nb_essais_big50.append(nb_essais_big50[-1]-1)

            #_____________________Mise à jour de la BD_______________________#
            #Recherche nom d'utilisateur
            if current_user.is_authenticated:
                user=session["username"]
            #Fin de vie et fin de partie du mode survie
            if nb_essais[-1]==0 and mode_de_jeu=='survie':
                vie-=1
                #MAJ de l'expérience
                if vie == 0 and current_user.is_authenticated:
                    experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                    experience=experience.fetchall()[0][0]
                    print("experience",experience)
                    experience+=75*score_survie[-1]
                    print("experience",experience)
                    cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,user))
                    con.commit()
            if etat_lettres == '2'*nb_lettres and mode_de_jeu=='survie': 
                score_survie.append(score_survie[-1]+nb_essais[-1]+1)
                print(score_survie[-1])
            if etat_lettres == '2'*nb_lettres and mode_de_jeu == 'big50':
                score_big50+=1
            #Fin de partie du mode big50, MAJ du score
            if nb_essais_big50[-1] == 0 and mode_de_jeu=='big50' and current_user.is_authenticated:
                experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                experience=experience.fetchall()[0][0]
                print("experience",experience)
                experience+=250*score_big50
                print("experience",experience)
                cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,user))
                con.commit()
            cur.execute("INSERT INTO Modes VALUES (?,?,?,?,?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu,vie,score_survie[-1],nb_essais_big50[-1],score_big50)) 
            con.commit()
            #________________________________________________________________#
            if etat_lettres == '2'*nb_lettres:                                  #Si le dernier etat_lettres = '2222222222' par exemple c'est que le mot est trouvé
                if mode_de_jeu == 'classique':
                    if current_user.is_authenticated:
                        user=session["username"]
                        nb_victoires=cur.execute("SELECT Nb_victoires FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        nb_victoires=nb_victoires.fetchall()[0][0]
                        #print("nb_victoires",nb_victoires)
                        nb_victoires+=1

                        experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                        experience=experience.fetchall()[0][0]
                        #print("experience",experience)
                        experience+=250

                        cur.execute("UPDATE Utilisateur SET Nb_victoires = (?), Experience = (?) WHERE Nom_utilisateur=(?)",(nb_victoires,experience,user))
                        id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                        id_partie=id_partie.fetchall()[0][0]
                        Partie=[id_partie,user,'Vrai',nb_essais[0]-nb_essais[-1],'25/01/2022','classique',mot_cherche]
                        cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                        con.commit()
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50)
            else:
                if nb_essais[-1]==0:
                    if mode_de_jeu == 'classique':
                        if current_user.is_authenticated:
                            user=session["username"]
                            nb_defaites=cur.execute("SELECT Nb_defaites FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                            nb_defaites=nb_defaites.fetchall()[0][0]
                            #print("nb_defaites",nb_defaites)
                            nb_defaites+=1

                            experience=cur.execute("SELECT Experience FROM Utilisateur WHERE Nom_utilisateur=(?) ",([user]))
                            experience=experience.fetchall()[0][0]
                            #print("experience",experience)
                            experience+=25

                            cur.execute("UPDATE Utilisateur SET Nb_defaites = (?), Experience = (?) WHERE Nom_utilisateur=(?)",(nb_defaites,experience,user))
                            id_partie=cur.execute("SELECT COUNT(*) FROM Historique")
                            id_partie=id_partie.fetchall()[0][0]
                            Partie=[id_partie,user,'Faux',0,'25/01/2022','classique',mot_cherche]
                            cur.execute("insert into Historique values(?,?,?,?,?,?,?)", Partie)
                            con.commit()
                liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
                return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50)
        else:
            #print("mot non valide")
            return render_template("accueil_fail.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50)
        
    else:
        print("Le mot à trouver est : ",mot_cherche)
        liste_mot_propose = place_premiere_lettre(nb_lettres,liste_mot_propose,mot_cherche,point) #On place la première lettre dans le mot a deviné
        return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais,mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres,vie=vie,score_survie=score_survie,nb_essais_big50=nb_essais_big50,score_big50=score_big50)


#Rejouer si mode de jeu est classique
@app.route('/rejouer_classique',methods=['GET','POST'])
def rejouer_classique():
    connection = sqlite3.connect('wordle.sql')
    cur = connection.cursor()

    nb_essais = recup_table()[0]
    nb_essais = nb_essais[-1][0] 


    nb_lettres = recup_table()[1]
    nb_lettres = nb_lettres[0][0]                                          #Idem mot_cherche

    mot_cherche = recup_table()[2]
    mot_cherche = mot_cherche[0][0]                                        #On prend le premier élément de la liste mot_cherche (tous les éléments sont identiques)
    
    mode_de_jeu = recup_table()[5]
    mode_de_jeu =  mode_de_jeu[0][0]

    cur.execute('''DELETE FROM Modes;''')
    #print(nb_essais,nb_lettres,mode_de_jeu)
    cur.execute("INSERT INTO Modes VALUES(?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,3,0,50,0))
    connection.commit()
    return redirect("accueil")


#Rejouer si mode de jeu est survie
@app.route('/rejouer_survie',methods=['GET','POST'])
def rejouer_survie():
    connection = sqlite3.connect('wordle.sql')
    cur = connection.cursor()

    nb_essais = recup_table()[0]
    nb_essais = nb_essais[-1][0] 


    nb_lettres = recup_table()[1]
    nb_lettres = nb_lettres[0][0]                                          #Idem mot_cherche

    mot_cherche = recup_table()[2]
    mot_cherche = mot_cherche[0][0]                                        #On prend le premier élément de la liste mot_cherche (tous les éléments sont identiques)
    
    mode_de_jeu = recup_table()[5]
    mode_de_jeu =  mode_de_jeu[0][0]

    vie = recup_table()[6]
    vie =  vie[0][0]

    score_survie = recup_table()[7]
    score_survie = score_survie[0][0]
    
    cur.execute('''DELETE FROM Modes;''')
    #print(nb_essais,nb_lettres,mode_de_jeu)
    cur.execute("INSERT INTO Modes VALUES(?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,vie,score_survie,50,0))
    connection.commit()
    return redirect("accueil")



#Rejouer si mode de jeu est Big50
@app.route('/rejouer_big50',methods=['GET','POST'])
def rejouer_big50():
    connection = sqlite3.connect('wordle.sql')
    cur = connection.cursor()

    nb_essais = recup_table()[0]
    nb_essais = nb_essais[-1][0] 


    nb_lettres = recup_table()[1]
    nb_lettres = nb_lettres[0][0]                                          #Idem mot_cherche

    mot_cherche = recup_table()[2]
    mot_cherche = mot_cherche[0][0]                                        #On prend le premier élément de la liste mot_cherche (tous les éléments sont identiques)
    
    mode_de_jeu = recup_table()[5]
    mode_de_jeu =  mode_de_jeu[0][0]

    nb_essais_big50 = recup_table()[8]
    nb_essais_big50 =  nb_essais_big50[0][0]

    score_big50 = recup_table()[9]
    score_big50 = score_big50[0][0]
    
    cur.execute('''DELETE FROM Modes;''')
    #print(nb_essais,nb_lettres,mode_de_jeu)
    cur.execute("INSERT INTO Modes VALUES(?,?,?,?,?,?,?,?,?,?)",(nb_essais,nb_lettres,'','','',mode_de_jeu,3,0,nb_essais_big50,score_big50))
    connection.commit()
    return redirect("accueil")


#Statistiques
@app.route('/statistiques')
@login_required
def stat():
    user=session["username"]
    data=[]

    #Connection a la bdd
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Utilisateur"):
        data.append(i)
    con.commit()
    con.close()

    #Selection des stats d'un joueur en particulier
    for u in data:
        if u[1]==user:
            info=u
    nb_vict=info[4]
    nb_parties=info[4]+info[5]
    if nb_vict==0 or nb_parties==0:
        taux_vict ='0%'
    else:
        taux_vict=str((nb_vict/nb_parties)*100)+"%"
    xp=info[6]
    lvl = level_function(xp)

    #Tracer courbe
    histo=[]
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Historique"):
        histo.append(i)
    con.commit()
    con.close()

    y=[0 for i in range(15)]
    x=[i for i in range (15)]

    for u in histo:
        if u[1]==user:
            y[int(u[3])]+=1
    y[0]=0
    plt.clf()
    plt.plot(x, y)
    plt.title("Nombres de parties gagnées en X coups")
    plt.xlabel("Nombre de coups", size = 16,)
    plt.ylabel("Nombres de parties", size = 16)
    plt.savefig('static/image.png')

    return render_template("statistiques.html", liste=[nb_parties,nb_vict,taux_vict,xp,lvl])

#Historique
@app.route('/historique')
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

    for u in histo:
        if u[1]==user:
            histo_perso.append(list(u))
    for u in histo_perso:
        if u[2]=="Vrai":
            u[2]="Victoire"
        else:
            u[2]="Défaite"
    

    
    return render_template("historique.html",histo=histo_perso)


#Succès
@app.route('/succes')
@login_required
def succes():
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    req = cur.execute("SELECT * FROM Quetes")
    quetes = req.fetchall()
    print(quetes)
    req = cur.execute("SELECT * FROM Quetes_rea WHERE Identifiant = (?)", ([session['username']]))
    quetes_rea = req.fetchall()
    print(quetes_rea)
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
        cur.execute('''DELETE FROM Modes;''')
        #print(nb_essais,nb_lettres,mode_de_jeu)
        cur.execute("INSERT INTO Modes VALUES(?,?,?,?,?,?,?,?,?,?)",(select_essais,select_lettres,'','','',select_mode_de_jeu,3,0,50,0))
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
                #Insertion de l'utilisateur dans la BD
                cur.execute("INSERT INTO utilisateur(Id, Nom_utilisateur, Mot_de_passe, Email, Nb_victoires, Nb_defaites, Experience) VALUES (?,?,?,?,?,?,?)", (num, username, password, email, 0, 0, 0))#Certaines données s'initialisent à zéro (nb parties, xp...)
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
    req = cur.execute("SELECT Email, Experience FROM Utilisateur WHERE Nom_utilisateur = (?)", ([session['username']]))
    elements = req.fetchall()
    email, xp = elements[0][0], elements[0][1]
    #Calcul niveau joueur
    lvl = get_level(xp)
    return render_template('profil.html', email=email, lvl=lvl)