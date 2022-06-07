#include "solveur.h"

int main()
{
    /* Test fonction freq_letters :
    La fonction calcule la fréquence d'apparition des lettres
    */

    //Choix de différents mots pour les tests

    char croix[20] = "CROIX";
    char serrure[20] = "SERRURE";
    char infinitif[20] = "INFINITIF";
    char lamas[20] = "LAMAS";
    char clics[20] = "CLICS";

    //Initialisation de la liste
    list_t *liste_mots = list_create();
    list_append(liste_mots, croix, 0.0);
    list_append(liste_mots, serrure, 0.0);
    list_append(liste_mots, infinitif, 0.0);
    list_append(liste_mots, lamas, 0.0);
    list_append(liste_mots, clics, 0.0);

    //Vérification que le calcul de fréquence d'apparition de la lettre dans la liste de mots est bonne
    //La liste "liste_mots" est composé de 31 caracères. On divise toujours par 31 pour trouver la fréquence supposée.

    assert(freq_letters(liste_mots,'E') == 2/31); // 2 fois "E" dans la liste liste_mots
    assert(freq_letters(liste_mots,'X') == 1/31); // 1 fois "X" dans la liste liste_mots
    assert(freq_letters(liste_mots,'R') == 4/31); // 4 fois "R" dans la liste liste_mots
    assert(freq_letters(liste_mots,'L') == 2/31); // 2 fois "L" dans la liste liste_mots
    assert(freq_letters(liste_mots,'I') == 6/31); // 5 fois "I" dans la liste liste_mots
    assert(freq_letters(liste_mots,'A') == 2/31); // 2 fois "A" dans la liste liste_mots
    assert(freq_letters(liste_mots,'S') == 3/31); // 3 fois "S" dans la liste liste_mots
    assert(freq_letters(liste_mots,'F') == 2/31); // 2 fois "F" dans la liste liste_mots
    assert(freq_letters(liste_mots,'O') == 1/31); // 1 fois "O" dans la liste liste_mots
    assert(freq_letters(liste_mots,'C') == 3/31); // 3 fois "E" dans la liste liste_mots
    assert(freq_letters(liste_mots,'U') == 1/31); // 1 fois "U" dans la liste liste_mots
    assert(freq_letters(liste_mots,'N') == 2/31); // 1 fois "N" dans la liste liste_mots
    assert(freq_letters(liste_mots,'M') == 1/31); // 1 fois "M" dans la liste liste_mots
    assert(freq_letters(liste_mots,'T') == 1/31); // 1 fois "T" dans la liste liste_mots

    /* Test fonction freqScore :
    La fonction calcule le score fréquence total de chaque mot de la liste
    */

    freqScore(list_t *liste_mots)

    //Vérification que la fréquence totale de chaque mot est bien l'addition des différentes fréquences des caractères composant ce mot
    
    assert((liste_mots->premier->freqScore) == 15/31); // Somme des fréquences des lettres du mot "CROIX"
    assert((liste_mots->premier->suivant->freqScore) == 20/31); // Somme des fréquences des lettres du mot "SERRURE"
    assert((liste_mots->premier->suivant->suivant->freqScore) == 33/31); // Somme des fréquences des lettres du mot "INFINITIF"
    assert((liste_mots->premier->suivant->suivant->suivant->freqScore) == 10/31); // Somme des fréquences des lettres du mot "LAMAS"
    assert((liste_mots->premier->suivant->suivant->suivant->suivant->freqScore) == 17/31); // Somme des fréquences des lettres du mot "CLICS"

}