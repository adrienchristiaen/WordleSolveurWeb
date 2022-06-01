#include "solveur.h"

int main()
{
    /* Test fonction presentXfois :
    La fonction renvoie 1 si le caractère à vérifier est présent X fois, 0 sinon.
    */
    
    char croix[20] = "CROIX";
    char serrure[20] = "SERRURE";
    char infinitif[20] = "INFINITIF";
    char lamas[20] = "LAMAS";
    char clics[20] = "CLICS";

    //Caractère présent bon nombre de fois
    assert(presentXfois(croix, 1, 'C') == 1);
    assert(presentXfois(croix, 1, 'I') == 1);
    assert(presentXfois(croix, 1, 'X') == 1);
    assert(presentXfois(serrure, 3, 'R') == 1);
    assert(presentXfois(infinitif, 4, 'I') == 1);

    //Caractère non présent
    assert(presentXfois(lamas, 1, 'R') == 0);
    assert(presentXfois(lamas, 1, 'D') == 0);

    //Caractère présent trop de fois
    assert(presentXfois(croix, 0, 'C') == 0);
    assert(presentXfois(clics, 1, 'C') == 0);

    //Caractère présent pas assez de fois
    assert(presentXfois(infinitif, 3, 'F') == 0);
    assert(presentXfois(infinitif, 6, 'I') == 0);

    /* Test fonction supprimeMot : */

    //Initialisation de la liste
    list_t* listeMots = list_create();
    list_append(listeMots, croix, 0.0);
    list_append(listeMots, serrure, 0.0);
    list_append(listeMots, infinitif, 0.0);
    list_append(listeMots, lamas, 0.0);
    list_append(listeMots, clics, 0.0);

    //Affichage de la liste initiale
    printf("Liste initiale:\n");
    list_print(listeMots);

    //Supression premier élément
    supprimeMot(listeMots, croix);
    printf("\nSupression du mot CROIX:\n");
    list_print(listeMots);

    //Supression dernier élément
    supprimeMot(listeMots, "CLICS");
    printf("\nSupression du mot CLICS:\n");
    list_print(listeMots);

    //Supression élément quelconque
    supprimeMot(listeMots, "INFINITIF");
    printf("\nSupression du mot INFINITIF:\n");
    list_print(listeMots);

    /* Libération mémoire */

    //Supression liste de mots
    list_destroy(listeMots);

    return EXIT_SUCCESS;
}