from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3
from selection import *
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
def accueil(nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[]):
    #Connexion base de données
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()

    #________________Récupération depuis la base de données________________#
    nb_essais=cur.execute("SELECT Nb_essais FROM Modes ")
    nb_essais=nb_essais.fetchall()
    #print("nb_essais :",nb_essais)

    nb_lettres=cur.execute("SELECT Nb_caracteres FROM Modes ")
    nb_lettres=nb_lettres.fetchall()[0]
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
    mode_de_jeu=mode_de_jeu.fetchall()[0][0]
    #print(mode_de_jeu)

    #______________________________________________________________________#

    #__________________Mise des tuples sous forme de liste_________________#
    mot_cherche=mot_cherche[0][0]
    for i in range(len(nb_essais)):
        nb_essais[i]=nb_essais[i][0]
    nb_essais.reverse()
    #print("nb_essais :",nb_essais)
    nb_lettres=nb_lettres[0]

    liste_mot_propose=[]
    for i in range(len(mots_proposes)):
        liste_mot_propose.append(mots_proposes[i][0])
    #print('avant test',liste_mot_propose)
    if liste_mot_propose[0]=='':
        remplissage = nb_lettres-len(liste_mot_propose)
        for j in range(remplissage):
            liste_mot_propose.append('')
        for k in range (len(liste_mot_propose)):
            if liste_mot_propose[k]=='':
                liste_mot_propose[k]=point*nb_lettres
    else:
        #print('else',liste_mot_propose)
        liste_mot_propose.reverse()
        liste_mot_propose.pop(0)
        #print(liste_mot_propose)
        remplissage = nb_lettres-len(liste_mot_propose)
        for i in range(remplissage):
            liste_mot_propose.append('')
        for k in range (len(liste_mot_propose)):
            if liste_mot_propose[k]=='':
                liste_mot_propose[k]=point*nb_lettres
    print(liste_mot_propose)


    liste_etat_lettres=[]
    for i in range(len(etat_lettres)):
        liste_etat_lettres.append(etat_lettres[i][0])
    #print('avant test',liste_etat_lettres)
    if liste_etat_lettres[0]=='':
        remplissage = nb_lettres-len(liste_etat_lettres)
        for j in range(remplissage):
            liste_etat_lettres.append('')
        for k in range (len(liste_etat_lettres)):
            if liste_etat_lettres[k]=='':
                liste_etat_lettres[k]=zero*nb_lettres
        #print('if',liste_etat_lettres)
    else:
        liste_etat_lettres.reverse()
        liste_etat_lettres.pop(0)
        #print(liste_mot_propose)
        remplissage = nb_lettres-len(liste_etat_lettres)
        for i in range(remplissage):
            liste_etat_lettres.append('')
        for k in range (len(liste_etat_lettres)):
            if liste_etat_lettres[k]=='':
                liste_etat_lettres[k]=zero*nb_lettres
    #print('else',liste_etat_lettres)


    #______________________________________________________________________#

    #___________________________Si la partie commmence_____________________#
    if mot_cherche=='':
        mot_propose = ''
        etat_lettres = ''
        print("etat_lettres",etat_lettres)
        mot_cherche=choisir_mot(nb_lettres)
        cur.execute("DELETE FROM Modes WHERE mot_cherche=('') ")
        cur.execute("INSERT INTO Modes (Nb_essais,Nb_caracteres,mot_cherche,mots_proposes,etat_lettres,Mode_de_jeu) VALUES (?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu)) 
        con.commit()
    #______________________________________________________________________#
    
    if request.method == "POST":
        #_______________________Place la première lettre_______________________#
        test=True
        print(test,liste_mot_propose)
        for i in range(len(liste_mot_propose)):
            if liste_mot_propose[i] == point*nb_lettres and test:
                liste_mot_propose[i]=mot_cherche[0]+point*(nb_lettres-1)
                test=False
                print('ca passe')
        print(liste_mot_propose)
        #______________________________________________________________________#
        if nb_essais[-1]>0:
            print("Le mot à trouver est : ",mot_cherche)
            mot_propose=request.form.get("mot_propose")
            if verif_mot(mot_propose,mot_cherche):
                mot_propose = mot_propose.upper()
                #print(nb_essais[0],nb_essais[-1], nb_essais[0]-nb_essais[-1])
                liste_mot_propose[nb_essais[0]-nb_essais[-1]] = mot_propose
                #print(nb_essais)
                print(liste_mot_propose)

                print("Le mot proposé est : ",mot_propose)

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
                
                liste_etat_lettres[nb_essais[0]-nb_essais[-1]] = etat_lettres
    
                nb_essais.append(nb_essais[-1]-1)
                #_____________________Mise à jour de la BD_______________________#
                cur.execute("INSERT INTO Modes (Nb_essais,Nb_caracteres,mot_cherche,mots_proposes,etat_lettres,Mode_de_jeu) VALUES (?,?,?,?,?,?) ",(nb_essais[-1],nb_lettres,mot_cherche,mot_propose,etat_lettres,mode_de_jeu)) 
                con.commit()
                #________________________________________________________________#
                if etat_lettres == '2'*nb_lettres:
                    return render_template("accueil_win.html",nb_lettres=nb_lettres, nb_essais=nb_essais[-1],mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres)
                else:
                    #_______________________Place la première lettre_______________________#
                    test=True
                    #print(test,liste_mot_propose)
                    for i in range(len(liste_mot_propose)):
                        if liste_mot_propose[i] == point*nb_lettres and test:
                            liste_mot_propose[i]=mot_cherche[0]+point*(nb_lettres-1)
                            test=False
                            #print('ca passe')
                    #print(liste_mot_propose)
                    #______________________________________________________________________#
                    return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais[-1],mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres)
            else:
                print("mot non valide")
                return render_template("accueil_fail.html",nb_lettres=nb_lettres, nb_essais=nb_essais[-1],mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres)
        else:
                print("plus d'essais")
                return render_template("accueil_lose.html",nb_lettres=nb_lettres, nb_essais=nb_essais[-1],mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres)
    else:
        print("Le mot à trouver est : ",mot_cherche)
        #_______________________Place la première lettre_______________________#
        test=True
        #print(test,liste_mot_propose)
        for i in range(len(liste_mot_propose)):
            if liste_mot_propose[i] == point*nb_lettres and test:
                liste_mot_propose[i]=mot_cherche[0]+point*(nb_lettres-1)
                test=False
                #print('ca passe')
        #print(liste_mot_propose)
        #______________________________________________________________________#
        return render_template("accueil.html",nb_lettres=nb_lettres, nb_essais=nb_essais[-1],mode_de_jeu=mode_de_jeu,mot_cherche=mot_cherche, liste_mot_propose=liste_mot_propose,liste_etat_lettres=liste_etat_lettres)


#Statistiques
@app.route('/statistiques')
def stat():
    id=0
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
        if u[0]==id:
            info=u
    nb_vict=info[4]
    nb_parties=info[4]+info[5]
    taux_vict=str((nb_vict/nb_parties)*100)+"%"
    xp=info[6]

    return render_template("statistiques.html", liste=[nb_vict,nb_parties,taux_vict,xp])


#Mode de jeu/Paramètres
@app.route('/parametres',methods=['GET','POST'])
def parametres():
    if request.method == "POST":
        #Informations du formulaire
        select_lettres=request.form.get("select_lettres")
        select_essais=request.form.get("select_essais")
        select_mode_de_jeu=request.form.get("select_mode_de_jeu")
        solo = request.form.get("solo")
        multi = request.form.get("multi")
        #Connexion base de données
        con=sqlite3.connect('wordle.db')
        cur = con.cursor()
        if not multi == None:
            return render_template("construction.html")
        if not solo == None:
            return render_template("accueil.html",nb_lettres=select_lettres,nb_essais=select_essais,mode_de_jeu=select_mode_de_jeu)
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
        #Connexion base de données
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
                cur.execute("INSERT INTO utilisateur(Id, Nom_utilisateur, Mot_de_passe, Email) VALUES (?,?,?,?)", (num, username, password, email))
                con.commit()
                #Création du compte et connexion
                session['username'] = username
                user = User(id = num)
                login_user(user)
                flash("Votre nouveau compte a été créé avec succès !")
                return render_template("accueil",nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[])

    return render_template('inscription.html')

#Connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == "POST":
        #Informations du formulaire
        username = request.form.get("username")
        password = request.form.get("password")
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
                return render_template("accueil",nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[])

    return render_template('connexion.html')

#Déconnexion
@app.route("/deconnexion")
@login_required
def deconnexion():
    session.pop('username', None)
    logout_user()
    flash("Vous vous êtes déconnecté avec succès. A la prochaine !")
    return render_template("accueil",nb_lettres=None, nb_essais=None,mode_de_jeu=None,mot_cherche=None, liste_mot_propose=[],liste_etat_lettres=[])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++