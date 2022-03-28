import sqlite3

connection = sqlite3.connect("wordle.db")
cursor = connection.cursor()

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
Utilisateur_list = [
    (0, "Adrien", "test12", "christiaen.adrien@gmail.com", 10, 10, "10%")
]
cursor.executemany("insert into Utilisateur values(?,?,?,?,?,?,?)", Utilisateur_list)


#Table Historique
cursor.execute("""create table Historique(
    Id_partie integer, 
    Identifiant varchar, 
    Etat boolean, 
    Nb_coups integer, 
    Date varchar, 
    Mode_de_jeu varchar, 
    PRIMARY KEY(Id_partie))""")
Historique_list = [
    (0, "Adrien", "Vrai", 10, "10/03/2022", "Survival")
]
cursor.executemany("insert into Historique values(?,?,?,?,?,?)", Historique_list)

#Table Quetes
cursor.execute("""create table Quetes(
    Id_quete integer, 
    Nom varchar, 
    Objectif varchar, 
    Valeur_xp integer, 
    PRIMARY KEY(Id_quete))""")
Quetes_list = [
    (0, "Wordle episode 1", "4 Essais max", 10)
]
cursor.executemany("insert into Quetes values(?,?,?,?)", Quetes_list)

#Table Quetes_rea
cursor.execute("""create table Quetes_rea(
    Id_quete integer, 
    Identifiant varchar, 
    Etat boolean, 
    PRIMARY KEY(Id_quete))""")
Quetes_rea_list = [
    (0, "Adrien", "Vrai")
]
cursor.executemany("insert into Quetes_rea values(?,?,?)", Quetes_rea_list)

#Table Modes
cursor.execute("""create table Modes(
    Mode_de_jeu varchar, 
    Nb_caracteres integer, 
    Nb_essais integer, 
    PRIMARY KEY(Mode_de_jeu))""")
Modes_list = [
    ("Multiplayer", 8, 10)
]
cursor.executemany("insert into Modes values(?,?,?)", Modes_list)


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