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

#Statistiques

#Mode de jeu/Paramètres

#Inscription/Connexion
