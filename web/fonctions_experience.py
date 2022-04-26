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


def maj_succes(nb_coups,nb_victoires,experience,utilisateur):
    #Gestion des succès ----------------------------------------
    con=sqlite3.connect('wordle.sql')
    cur = con.cursor()
    #Succès réussite partie en 4 coups
    if nb_coups == 4:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
            experience += 1000
    #Succès réussite partie en 3 coups
    if nb_coups == 3:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
            experience += 5000
    #Succès réussite partie en 2 coups
    if nb_coups == 2:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
            experience += 5000
        #Succès pour 2 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(2)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(2)",(utilisateur))
            experience += 10000
    #Succès réussite partie en 1 coup
    if nb_coups == 1:
        #Succès pour 4 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(0)",(utilisateur))
            experience += 1000
        #Succès pour 3 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(1)",(utilisateur))
            experience += 5000
        #Succès pour 2 coups ou moins
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(2)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(2)",(utilisateur))
            experience += 10000
        #Succès pour 1 coup
        req = cur.execute("SELECT Etat FROM Quetes_rea WHERE Identifiant=(?) AND Id_quete=(3)",(utilisateur))
        req = req.fetchall()
        etat_quete = req[0][0]
        if etat_quete == 0:
            cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(3)",(utilisateur))
            experience += 100000
    if nb_victoires == 5:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(4)",(utilisateur))
        experience += 1000
    if nb_victoires == 10:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(5)",(utilisateur))
        experience += 2000
    if nb_victoires == 20:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(6)",(utilisateur))
        experience += 3000
    if nb_victoires == 50:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(7)",(utilisateur))
        experience += 5000
    if nb_victoires == 100:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(8)",(utilisateur))
        experience += 10000
    if nb_victoires == 1000:
        cur.execute("UPDATE Quetes_rea SET Etat =(TRUE) WHERE Identifiant=(?) AND Id_quete=(9)",(utilisateur))
        experience += 100000
    con.commit()
    #------------------------------------------------------------