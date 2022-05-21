#include "solveur.h"

int main()
{
    list_t* liste_mots = list_create();
    printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    printf("LIST PRINT\n");
    list_print(liste_mots);
    list_destroy(liste_mots);
    return 0;
}


