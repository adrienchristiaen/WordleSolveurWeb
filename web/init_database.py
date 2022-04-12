import sqlite3,hashlib
connection = sqlite3.connect('wordle.sql')
cursor = connection.cursor()

#Delete table
cursor.execute('''DROP TABLE Utilisateur;''')
cursor.execute('''DROP TABLE Historique;''')
cursor.execute('''DROP TABLE Quetes;''')
cursor.execute('''DROP TABLE Quetes_rea;''')
cursor.execute('''DROP TABLE Modes;''')



#Table Utilisateur
cursor.execute("""create table Utilisateur(
    Id integer, 
    Nom_utilisateur text,
    Mot_de_passe varchar, 
    Email varchar, 
    Nb_victoires integer, 
    Nb_défaites integer, 
    Experience varchar, 
    PRIMARY KEY(Id))""")



#Table Historique
cursor.execute("""create table Historique(
    Id_partie integer, 
    Identifiant varchar, 
    Etat boolean, 
    Nb_coups integer, 
    Date varchar, 
    Mode_de_jeu varchar, 
    PRIMARY KEY(Id_partie))""")


#Table Quetes
cursor.execute("""create table Quetes(
    Id_quete integer, 
    Nom varchar, 
    Objectif varchar, 
    Valeur_xp integer, 
    PRIMARY KEY(Id_quete))""")


#Table Quetes_rea
cursor.execute("""create table Quetes_rea(
    Id_quete integer, 
    Identifiant varchar, 
    Etat boolean, 
    PRIMARY KEY(Id_quete))""")


#Table Modes
cursor.execute("""create table Modes(
    Nb_essais integer,
    Nb_caracteres integer,
    mot_cherche varchar,
    mots_proposes varchar, 
    etat_lettres  varchar,
    Mode_de_jeu varchar, 
    PRIMARY KEY(Nb_essais))""")


#Encodage du mot de passe
password = hashlib.sha224(bytes('test12',encoding='utf-8')).hexdigest()

cursor.execute("INSERT INTO Utilisateur VALUES(0,'Adrien',?,'christiaen.adrien@gmail.com',10,10,'10%')", ([password]))

cursor.execute("INSERT INTO Historique VALUES(0,'Adrien','Vrai',10,'10/03/2022','Survival%')")

cursor.execute("INSERT INTO Quetes VALUES(0,'Wordle episode 1','4 Essais max',10)")

cursor.execute("INSERT INTO Quetes_rea VALUES(0,'Adrien','Vrai')")

cursor.execute("INSERT INTO Modes VALUES(6,6,'','','','Classique')")



#Afficher les différentes tables pour test
for util in cursor.execute("select * from Utilisateur"):
    print(util)
for hist in cursor.execute("select * from Historique"):
    print(hist)
for quet in cursor.execute("select * from Quetes"):
    print(quet)
for quet_rea in cursor.execute("select * from Quetes_rea"):
    print(quet_rea)
for mod in cursor.execute("select * from Modes"):
    print(mod)

connection.commit()
connection.close()