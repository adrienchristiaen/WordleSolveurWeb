#include "solveur.h"

int main()
{
    /* Test fonction updateList :
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
  
    //Vérification de la fonctionnalité d'updateList avec les différentes combinaison

    //Affichage de la liste initiale
    printf("Liste initiale:\n");
    list_print(liste_mots);

    //Premier cas avec le mot clics en combinaison 2
    updateList(liste_mots, clics, 2);
    printf("\nSupression des mots CROIX, SERRURE, INFINITIF et LAMAS de la liste:\n");
    list_print(liste_mots);

    //Deuxième cas avec le mot clics en combinaison 1
    updateList(liste_mots, clics, 1);
    printf("\nSupression du mot CLIC de la liste:\n");
    list_print(liste_mots);

    //Troisième cas avec le mot clics en combinaison 0
    updateList(liste_mots, clics, 1);
    printf("\nSupression du mot CLIC de la liste:\n");
    list_print(liste_mots);

}