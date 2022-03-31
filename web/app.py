from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import sqlite3

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

#Accueil
@app.route('/')
@app.route('/accueil')
def accueil():
    return render_template("accueil.html")

#Statistiques
@app.route('/statistiques')
def stat():
    liste=["25","20","80%","10","7","70%"]
    return render_template("statistiques.html", liste=liste)

#Mode de jeu/Paramètres
#Statistiques
@app.route('/parametres')
def parametres():
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
        con = sqlite3.connect('wordle.db')
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
                return redirect("accueil")

    return render_template('inscription.html')

#Connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == "POST":
        #Informations du formulaire
        username = request.form.get("username")
        password = request.form.get("password")
        #Connexion base de données
        con = sqlite3.connect('wordle.db')
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