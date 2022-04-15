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
    Experience integer, 
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


#Table Quetes
cursor.execute("""create table Quetes(
    Id_quete integer, 
    Nom varchar, 
    Objectif varchar, 
    Valeur_xp integer, 
    PRIMARY KEY(Id_quete))""")


#Table Quetes_rea
cursor.execute("""create table Quetes_rea(
    Id_quete_rea integer,
    Id_quete integer,
    Identifiant varchar, 
    Etat boolean, 
    PRIMARY KEY(Id_quete_rea))""")


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

cursor.execute("INSERT INTO Quetes VALUES(0,'Stratège','Trouver le mot cherché en 4 coups ou moins',1000)")
cursor.execute("INSERT INTO Quetes VALUES(1,'Mentaliste','Trouver le mot cherché en 3 coups ou moins',5000)")
cursor.execute("INSERT INTO Quetes VALUES(2,'Bingo','Trouver le mot cherché en 2 coups ou moins',10000)")
cursor.execute("INSERT INTO Quetes VALUES(3,'Bouum','Trouver le mot cherché du premier coup',100000)")
cursor.execute("INSERT INTO Quetes VALUES(4,'Rookie','Gagner 5 parties',1000)")
cursor.execute("INSERT INTO Quetes VALUES(5,'Rookie doué','Gagner 10 parties',2000)")
cursor.execute("INSERT INTO Quetes VALUES(6,'Rookie distingué','Gagner 20 parties',3000)")
cursor.execute("INSERT INTO Quetes VALUES(7,'Joueur accompli','Gagner 50 parties',5000)")
cursor.execute("INSERT INTO Quetes VALUES(8,'Professionnel du mot','Gagner 100 parties',10000)")
cursor.execute("INSERT INTO Quetes VALUES(9,'Inarrêtable','Gagner 1000 parties',100000)")

cursor.execute("INSERT INTO Quetes_rea VALUES(0, 0, 'Adrien',TRUE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(1, 1, 'Adrien',FALSE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(2, 2, 'Adrien',FALSE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(3, 3, 'Adrien',FALSE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(4, 4, 'Adrien',TRUE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(5, 5, 'Adrien',TRUE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(6, 6, 'Adrien',TRUE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(7, 7, 'Adrien',FALSE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(8, 8, 'Adrien',FALSE)")
cursor.execute("INSERT INTO Quetes_rea VALUES(9, 9, 'Adrien',FALSE)")

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