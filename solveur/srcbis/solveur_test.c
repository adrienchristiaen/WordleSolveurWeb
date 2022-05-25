#include "solveur.h"

int main()
{
    /* TEST CREATION LISTE */
    list_t* liste_mots = list_create();
    //printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    //printf("LIST PRINT\n");
    //list_print(liste_mots);
    int combinaison = getResult(strlen(liste_mots->premier->mot));
    while (combinaison != -1)
    {
        printf("%d  \n",combinaison);
        combinaison = getResult(strlen(liste_mots->premier->mot));
    }

    /* TEST FREQUENCE */
    listinfo_t *infoList = createListInfo();
    initListInfo(infoList);
    //listInfo_print(infoList);
    int len = lengthListInfo(infoList);
    printf("My length is: %d\n",len);

    getMatches(infoList, liste_mots, "POULE");
    //listInfo_print(infoList);

    //Suppression des listes
    listInfo_destroy(infoList);
    list_destroy(liste_mots);
    return 0;
}
