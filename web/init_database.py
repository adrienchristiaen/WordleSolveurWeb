import sqlite3,hashlib
connection = sqlite3.connect('wordle.sql')
cursor = connection.cursor()

#Delete table

cursor.execute('''DROP TABLE Utilisateur;''')
cursor.execute('''DROP TABLE Historique;''')
cursor.execute('''DROP TABLE Quetes;''')
cursor.execute('''DROP TABLE Quetes_rea;''')
cursor.execute('''DROP TABLE Partie;''')



#Table Utilisateur
cursor.execute("""create table Utilisateur(
    Id integer, 
    Nom_utilisateur text,
    Mot_de_passe varchar, 
    Email varchar, 
    Nb_victoires_classique integer, 
    Nb_defaites_classique integer, 
    Experience integer,
    Photo varchar, 
    PRIMARY KEY(Id))""")


#Table Historique                                  
cursor.execute("""create table Historique(
    Id_partie integer, 
    Identifiant varchar, 
    Etat boolean, 
    Score integer,       
    Date varchar, 
    Mode_de_jeu varchar,
    Mot varchar, 
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


#Table Partie
cursor.execute("""create table Partie(
    Nb_essais integer,
    Nb_caracteres integer,
    mot_cherche varchar,
    mots_proposes varchar, 
    etat_lettres  varchar,
    Mode_de_jeu varchar, 
    Survie_vie integer,
    Survie_score integer,
    Big50_nb_essais integer,
    Big50_score integer,
    Clm_depart varchar,
    Clm_score integer,
    PRIMARY KEY(Nb_essais))""")


#Encodage du mot de passe
password = hashlib.sha224(bytes('test12',encoding='utf-8')).hexdigest()

cursor.execute("INSERT INTO Utilisateur VALUES(0,'Adrien',?,'christiaen.adrien@gmail.com',7,3,0,'profil3')", ([password]))

#Historique
cursor.execute("INSERT INTO Historique VALUES(0, 'Adrien', 'Vrai', 6, '10-03-2022', 'Classique', 'muret')")
cursor.execute("INSERT INTO Historique VALUES(1, 'Adrien', 'Faux', 0, '10-03-2022', 'Classique', 'table')")
cursor.execute("INSERT INTO Historique VALUES(2, 'Adrien', 'Faux', 6, '21-04-2022', 'Classique', 'flute')")
cursor.execute("INSERT INTO Historique VALUES(3, 'Adrien', 'Vrai', 4, '21-04-2022', 'Classique', 'carte')")
cursor.execute("INSERT INTO Historique VALUES(4, 'Adrien', 'Vrai', 4, '21-04-2022', 'Classique', 'roues')")
cursor.execute("INSERT INTO Historique VALUES(5, 'Adrien', 'Faux', 6, '22-04-2022', 'Classique', 'bouee')")
cursor.execute("INSERT INTO Historique VALUES(6, 'Adrien', 'Vrai', 3, '22-04-2022', 'Classique', 'jouets')")
cursor.execute("INSERT INTO Historique VALUES(7, 'Adrien', 'Vrai', 2, '22-04-2022', 'Classique', 'rares')")
cursor.execute("INSERT INTO Historique VALUES(8, 'Adrien', 'Vrai', 2, '22-04-2022', 'Classique', 'lapin')")
cursor.execute("INSERT INTO Historique VALUES(9, 'Adrien', 'Vrai', 5, '22-04-2022', 'Classique', 'rires')")
cursor.execute("INSERT INTO Historique VALUES(10, 'Adrien', 'Vrai', 14, '23-04-2022', 'Survie', 'rosee')")
cursor.execute("INSERT INTO Historique VALUES(11, 'Adrien', 'Vrai', 23, '23-04-2022', 'Survie', 'pizza')")
cursor.execute("INSERT INTO Historique VALUES(12, 'Adrien', 'Vrai', 12, '23-04-2022', 'Survie', 'loupe')")
cursor.execute("INSERT INTO Historique VALUES(13, 'Adrien', 'Vrai', 27, '23-04-2022', 'Survie', 'chats')")
cursor.execute("INSERT INTO Historique VALUES(14, 'Adrien', 'Vrai', 11, '23-04-2022', 'Survie', 'tarif')")
cursor.execute("INSERT INTO Historique VALUES(15, 'Adrien', 'Vrai', 18, '23-04-2022', 'Survie', 'trauma')")
cursor.execute("INSERT INTO Historique VALUES(16, 'Adrien', 'Vrai', 31, '23-04-2022', 'Survie', 'panda')")
cursor.execute("INSERT INTO Historique VALUES(17, 'Adrien', 'Vrai', 14, '23-04-2022', 'Survie', 'rateau')")
cursor.execute("INSERT INTO Historique VALUES(18, 'Adrien', 'Vrai', 37, '23-04-2022', 'Survie', 'pelle')")
cursor.execute("INSERT INTO Historique VALUES(19, 'Adrien', 'Vrai', 8, '23-04-2022', 'Big50', 'joues')")
cursor.execute("INSERT INTO Historique VALUES(20, 'Adrien', 'Vrai', 11, '23-04-2022', 'Big50', 'travail')")
cursor.execute("INSERT INTO Historique VALUES(21, 'Adrien', 'Vrai', 6, '23-04-2022', 'Big50', 'tenue')")
cursor.execute("INSERT INTO Historique VALUES(22, 'Adrien', 'Vrai', 13, '23-04-2022', 'Big50', 'lamas')")
cursor.execute("INSERT INTO Historique VALUES(23, 'Adrien', 'Vrai', 12, '24-04-2022', 'Big50', 'trouve')")
cursor.execute("INSERT INTO Historique VALUES(24, 'Adrien', 'Vrai', 7, '24-04-2022', 'Big50', 'loups')")
cursor.execute("INSERT INTO Historique VALUES(25, 'Adrien', 'Vrai', 11, '24-04-2022', 'CLM', 'rager')")
cursor.execute("INSERT INTO Historique VALUES(26, 'Adrien', 'Vrai', 4, '24-04-2022', 'CLM', 'crier')")
cursor.execute("INSERT INTO Historique VALUES(27, 'Adrien', 'Vrai', 21, '24-04-2022', 'CLM', 'nulle')")
cursor.execute("INSERT INTO Historique VALUES(28, 'Adrien', 'Vrai', 14, '24-04-2022', 'CLM', 'boules')")
cursor.execute("INSERT INTO Historique VALUES(29, 'Adrien', 'Vrai', 14, '24-04-2022', 'CLM', 'rouge')")
cursor.execute("INSERT INTO Historique VALUES(30, 'Adrien', 'Vrai', 12, '24-04-2022', 'CLM', 'hates')")
cursor.execute("INSERT INTO Historique VALUES(31, 'Adrien', 'Vrai', 18, '24-04-2022', 'CLM', 'mousse')")


#Quêtes
cursor.execute("INSERT INTO Quetes VALUES(0,'Stratège','Trouver le mot cherché en 4 coups ou moins',1000)")
cursor.execute("INSERT INTO Quetes VALUES(1,'Mentaliste','Trouver le mot cherché en 3 coups ou moins',5000)")
cursor.execute("INSERT INTO Quetes VALUES(2,'Bingo','Trouver le mot cherché en 2 coups ou moins',10000)")
cursor.execute("INSERT INTO Quetes VALUES(3,'Bouum','Trouver le mot cherché du premier coup',100000)")
cursor.execute("INSERT INTO Quetes VALUES(4,'Rookie','Gagner 5 parties classiques',1000)")
cursor.execute("INSERT INTO Quetes VALUES(5,'Rookie doué','Gagner 10 parties classiques',2000)")
cursor.execute("INSERT INTO Quetes VALUES(6,'Rookie distingué','Gagner 20 parties classiques',3000)")
cursor.execute("INSERT INTO Quetes VALUES(7,'Joueur accompli','Gagner 50 parties classiques',5000)")
cursor.execute("INSERT INTO Quetes VALUES(8,'Professionnel du mot','Gagner 100 parties classiques',10000)")
cursor.execute("INSERT INTO Quetes VALUES(9,'Inarrêtable','Gagner 1000 parties classiques',100000)")
cursor.execute("INSERT INTO Quetes VALUES(10,'Survivaliste','Obtenir un score de 10 ou plus en mode survie',10000)")
cursor.execute("INSERT INTO Quetes VALUES(11,'Pro de la survie','Obtenir un score de 25 ou plus en mode survie',25000)")
cursor.execute("INSERT INTO Quetes VALUES(12,'Expert survivaliste','Obtenir un score de 50 ou plus en mode survie',50000)")
cursor.execute("INSERT INTO Quetes VALUES(13,'Maître sacré de la survie','Obtenir un score de 100 ou plus en mode survie',100000)")
cursor.execute("INSERT INTO Quetes VALUES(14,'Son nom est Robinson','Obtenir un score de 100 ou plus en mode survie, sans perdre une seule vie',1000000)")
cursor.execute("INSERT INTO Quetes VALUES(15,'The big rookie','Obtenir un score de 5 ou plus en mode Big50',5000)")
cursor.execute("INSERT INTO Quetes VALUES(16,'The big boss','Obtenir un score de 10 ou plus en mode Big50',20000)")
cursor.execute("INSERT INTO Quetes VALUES(17,'The big master','Obtenir un score de 15 ou plus en mode Big50',100000)")
cursor.execute("INSERT INTO Quetes VALUES(18,'The big bang','Obtenir un score de 20 ou plus en mode Big50',1000000)")
cursor.execute("INSERT INTO Quetes VALUES(19,'La tortue','Ne trouver aucun mot en mode contre la montre',5000)")
cursor.execute("INSERT INTO Quetes VALUES(20,'Escargot','Ne trouver qu un seul mot en mode contre la montre',5000)")
cursor.execute("INSERT INTO Quetes VALUES(21,'Le petit loup','Obtenir un score de 5 ou plus en mode contre la montre',10000)")
cursor.execute("INSERT INTO Quetes VALUES(22,'Le lièvre','Obtenir un score de 10 ou plus en mode contre la montre',20000)")
cursor.execute("INSERT INTO Quetes VALUES(23,'Le grand gentil loup','Obtenir un score de 15 ou plus en mode contre la montre',40000)")
cursor.execute("INSERT INTO Quetes VALUES(24,'Ours rapide','Obtenir un score de 20 ou plus en mode contre la montre',50000)")
cursor.execute("INSERT INTO Quetes VALUES(25,'Le tigre','Obtenir un score de 25 ou plus en mode contre la montre',75000)")
cursor.execute("INSERT INTO Quetes VALUES(26,'Le roi lion','Obtenir un score de 30 ou plus en mode contre la montre',100000)")
cursor.execute("INSERT INTO Quetes VALUES(27,'Le guépard','Obtenir un score de 35 ou plus en mode contre la montre',200000)")
cursor.execute("INSERT INTO Quetes VALUES(28,'La fusée','Obtenir un score de 40 ou plus en mode contre la montre',500000)")
cursor.execute("INSERT INTO Quetes VALUES(29,'Alien','Obtenir un score de 45 ou plus en mode contre la montre',1000000)")
cursor.execute("INSERT INTO Quetes VALUES(30,'La lumière','Obtenir un score de 50 ou plus en mode contre la montre',10000000)")


for k in range(31):
    cursor.execute("INSERT INTO Quetes_rea VALUES("+str(k)+", "+str(k)+", 'Adrien',FALSE)")

cursor.execute("INSERT INTO Partie VALUES(6,6,'','','','classique',3,0,50,0,'',0)")

#Afficher les différentes tables pour test
for util in cursor.execute("select * from Utilisateur"):
    print(util)
for hist in cursor.execute("select * from Historique"):
    print(hist)
for quet in cursor.execute("select * from Quetes"):
    print(quet)
for quet_rea in cursor.execute("select * from Quetes_rea"):
    print(quet_rea)
for mod in cursor.execute("select * from Partie"):
    print(mod)

connection.commit()
connection.close()