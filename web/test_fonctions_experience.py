from fonctions_experience import *

def test_level_function():
    #Le joueur est de niveau 1 quand il n'a pas d'expérience
    assert level_function(0) == 1
    #Le joueur est de niveau 101 quand il a 1000000 points d'expérince
    assert level_function(1000000) == 101
    #Fonction croissante
    L_lvl = []
    for xp in range(1000000):
        L_lvl.append(level_function(xp))
    for i in range(1,1000000):
        assert L_lvl[i-1] <= L_lvl[i]

def test_xp_function():
    #Fonction inverse de level_function
    #Un joueur de niveau 1 a 0 points d'expérience
    assert xp_function(1) == 0
    #Un joueur de niveau 101 a 1000000 points d'expérience
    assert xp_function(101) == 1000000
    #Fonction croissante
    L_xp = []
    for lvl in range(1, 100):
        L_xp.append(xp_function(lvl))
    for i in range(1,99):
        assert L_xp[i-1] <= L_xp[i]