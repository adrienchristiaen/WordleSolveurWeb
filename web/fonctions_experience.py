import sqlite3

def level_function(xp):
    return int((xp/100)**(1/2) + 1)

# def updatelevel(xp):
#     if xp >= 1000000:
#         return 100
#     lvl = level_function(xp)
#     return lvl

def xp_function(lvl):
    return (lvl-1)**2*100

def lvl_info(xp):
    lvl = level_function(xp)
    lower_xp = xp_function(lvl)
    upper_xp = xp_function(lvl + 1)
    road_to_next_level = xp - lower_xp
    xp_needed_for_next_level = upper_xp - lower_xp
    return 0, road_to_next_level, xp_needed_for_next_level

def maj_succes(experience,utilisateur, vie, score_big50, nb_coups=0, nb_victoires=0, score_survie=0):
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    #Succès réussite partie en 4 coups
    if nb_coups == 4:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
            experience += 1000
    #Succès réussite partie en 3 coups
    if nb_coups == 3:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
            experience += 5000
    #Succès réussite partie en 2 coups
    if nb_coups == 2:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
            experience += 5000
        #Succès pour 2 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(2)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(2)",([utilisateur]))
            experience += 10000
    #Succès réussite partie en 1 coup
    if nb_coups == 1:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",([utilisateur]))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",([utilisateur]))
            experience += 5000
        #Succès pour 2 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(2)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(2)",([utilisateur]))
            experience += 10000
        #Succès pour 1 coup
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(3)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(3)",([utilisateur]))
            experience += 100000
    #Succès pour 5 victoires
    if nb_victoires == 5:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(4)",([utilisateur]))
        experience += 1000
    #Succès pour 10 victoires
    if nb_victoires == 10:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(5)",([utilisateur]))
        experience += 2000
    #Succès pour 20 victoires
    if nb_victoires == 20:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(6)",([utilisateur]))
        experience += 3000
    #Succès pour 50 victoires
    if nb_victoires == 50:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(7)",([utilisateur]))
        experience += 5000
    #Succès pour 100 victoires
    if nb_victoires == 100:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(8)",([utilisateur]))
        experience += 10000
    #Succès pour 1000 victoires
    if nb_victoires == 1000:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(9)",([utilisateur]))
        experience += 100000
    #Succès score en mode survie
    if score_survie >= 10:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(10)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(10)",([utilisateur]))
            experience += 10000
    if score_survie >= 25:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(11)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(11)",([utilisateur]))
            experience += 25000
    if score_survie >= 50:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(12)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(12)",([utilisateur]))
            experience += 50000
    if score_survie >= 100:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(13)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(13)",([utilisateur]))
            experience += 100000
    #Obtenir un score de 100 ou plus en mode survie, sans perdre une seule vie
    if score_survie >= 100 and vie == 3:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(14)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(14)",([utilisateur]))
            experience += 1000000
    #Scores en mode Big50
    if score_big50 >= 5:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(15)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(15)",([utilisateur]))
            experience += 5000
    if score_big50 >= 10:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(16)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(16)",([utilisateur]))
            experience += 20000
    if score_big50 >= 15:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(17)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(17)",([utilisateur]))
            experience += 100000
    if score_big50 >= 20:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(18)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(18)",([utilisateur]))
            experience += 1000000

    #Mise à jour de la base de données
    cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,utilisateur))
    con.commit()
    cur.close()

def maj_succes_clm(utilisateur, experience, score_clm):
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    #Ne trouver aucun mot en mode contre la montre
    if score_clm == 0:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(19)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(19)",([utilisateur]))
            experience += 5000
    #Ne trouver qu un seul mot en mode contre la montre
    if score_clm == 1:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(20)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(20)",([utilisateur]))
            experience += 5000
    #Succès scores en mode contre la montre
    if score_clm >= 5:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(21)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(21)",([utilisateur]))
            experience += 10000
    if score_clm >= 10:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(22)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(22)",([utilisateur]))
            experience += 20000
    if score_clm >= 15:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(23)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(23)",([utilisateur]))
            experience += 40000
    if score_clm >= 20:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(24)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(24)",([utilisateur]))
            experience += 50000
    if score_clm >= 25:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(25)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(25)",([utilisateur]))
            experience += 75000
    if score_clm >= 30:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(26)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(26)",([utilisateur]))
            experience += 100000
    if score_clm >= 35:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(27)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(27)",([utilisateur]))
            experience += 200000
    if score_clm >= 40:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(28)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(28)",([utilisateur]))
            experience += 500000
    if score_clm >= 45:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(29)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(29)",([utilisateur]))
            experience += 1000000
    if score_clm >= 50:
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(30)",([utilisateur]))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(30)",([utilisateur]))
            experience += 10000000

    #Mise à jour de la base de données
    cur.execute("UPDATE Utilisateur SET Experience = (?) WHERE Nom_utilisateur=(?)",(experience,utilisateur))
    con.commit()
    cur.close()