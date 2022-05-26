#include "solveur.h"
#include "frequency.h"
#include <time.h>

int main()
{
    //Gestionnaire de temps
    double time_spent = 0.0;
    clock_t begin = clock();
    
    /* TEST CREATION LISTE */
    list_t* liste_mots = list_create();
    //printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    //printf("LIST PRINT\n");
    //list_print(liste_mots);
    
    

    /* TEST FREQUENCE
    listinfo_t *infoList = createListInfo();
    initListInfo(infoList);
    listInfo_print(infoList);
    int len = lengthListInfo(infoList);
    printf("My length is: %d\n",len);

    getMatches(infoList, liste_mots, "POULE");
    listInfo_print(infoList);
    */

    //Information
    printf("\nINFORMATION:\n\n");
    //getBits(3,7645);
    allinfo_t *myAllInfo = getAllInfoForAllWords(liste_mots);
    
    //Suppression des listes
    destroyAllInfo(myAllInfo);
    //listInfo_destroy(infoList);
    list_destroy(liste_mots);

    //Gestionnaire de temps
    clock_t end = clock();
    time_spent = (double)(end - begin) / CLOCKS_PER_SEC / 60;
    printf("Temps de résolution : %lf min.\n", time_spent);

    return 0;
}
