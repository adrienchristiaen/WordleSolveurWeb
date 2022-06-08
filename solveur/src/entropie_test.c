#include "solveur.h"

int main()
{
    /* Test fonction createListInfo :
    La fonction créée une liste chainée contenant les bits des différents mots
    */
    listinfo_t* ListeTests = createListInfo();
    listinfo_t* ListePaterns = createListInfo();
    listinfo_t* ListeVide = createListInfo();
    assert(ListeTests->premier == NULL);
    assert(ListePaterns->premier == NULL);
    assert(ListeVide->premier == NULL);


    /* Test fonction listInfo_append :
    La fonction créée une liste chainée contenant les bits des différents mots
    */
    listInfo_append(ListeTests,"tests");
    assert(strcmp(ListeTests->premier->result,"tests")==0);
    listInfo_append(ListeTests,"testa");
    assert(strcmp(ListeTests->premier->suivant->result,"testa")==0);

    /* Test fonction infoPrint :
    La fonction affiche un élément de la liste d'informations
    */
    info_print(ListeTests->premier);
    printf("\n");
    info_print(ListeTests->premier->suivant);
    printf("\n");
    //info_print(ListeVide->premier);   erreur !


    /* Test fonction listInfo_print :
    La fonction affiche toute la liste d'informations
    */
    listInfo_print(ListeTests);
    //listInfo_print(ListeVide);     erreur ! car la liste est vide


    /* Test fonction initListInfo :
    La fonction rempli la liste chaînée contenant les bits avec tous les patterns possibles
    */
    initListInfo(ListeTests,5);
    initListInfo(ListePaterns,5);
    listInfo_print(ListePaterns);
    //assert(strcmp(ListeTests->premier->result,"00000")==0); erreur si la liste n'est pas vide
    assert(strcmp(ListePaterns->premier->result,"00000")==0);
    
    /* Test fonction infoPrint :
    La fonction créée une liste chainée contenant les bits des différents mots
    */
    info_print(ListePaterns->premier);
    printf("\n");
    info_print(ListePaterns->premier->suivant->suivant->suivant->suivant->suivant->suivant->suivant->suivant);
    printf("\n");
    //info_print(ListeVide->premier);   erreur !

    /* Test fonction lengthListInfo :
    La fonction renvoit la taille de la liste chaînée
    */
    assert(lengthListInfo(ListePaterns)==(int)pow(3,5));   
    assert(lengthListInfo(ListeVide)==0); 


    /* Test fonction getMatches :
    La fonction calcule le nombre de "match" possibles avec un mot donné pour chaque pattern
    */
    list_t* listeMots = list_create();
    info_t* actuel = ListePaterns->premier;
    ajout_mots(listeMots);
    getMatches(ListePaterns, listeMots, "ZLOTY");
    while (actuel->suivant!=NULL && (actuel->match>40 || actuel->match<0))
    {
        actuel = actuel->suivant;
    }
    // MOTS POSSIBLES pour le patern 00012 : satay, tokay, tommy, torcy
    assert(actuel->match == 4);
    //printf("%s %d\n",actuel->result,actuel->match);

    actuel = ListePaterns->premier;
    getMatches(ListePaterns, listeMots, "YUZUS");
    while (actuel->suivant!=NULL && (actuel->match>20 || actuel->match<0))
    {
        actuel = actuel->suivant;
    }
    // MOTS POSSIBLES pour le patern 00122 : zebus, zamus
    assert(actuel->match == 2);
    //printf("%s %d\n",actuel->result,actuel->match);

    actuel = ListePaterns->premier;
    getMatches(ListePaterns, listeMots, "EQUIN");
    while (actuel->suivant!=NULL && (actuel->match>15 || actuel->match<0))
    {
        actuel = actuel->suivant;
    }
    // MOTS POSSIBLES pour le patern 00112 : union, immun
    assert(actuel->match == 2);
    //printf("%s %d\n",actuel->result,actuel->match);

    /* Test fonction listInfo_destroy :
    La fonction détruit une liste chainée contenant les bits des différents mots
    */
    listInfo_destroy(ListeTests);
    listInfo_destroy(ListePaterns);
    listInfo_destroy(ListeVide);


    /* Test fonction createAllInfoList :
    La fonction créée une liste chainée contenant les listes chainées des différentes informations
    */
    // allinfo_t* ListeTests2 = createAllInfoList();
    // allinfo_t* ListePaterns2 = createAllInfoList();
    // allinfo_t* ListeVide2 = createAllInfoList();
    // assert(ListeTests2->first == NULL);
    // assert(ListePaterns2->first == NULL);
    // assert(ListeVide2->first == NULL);



    /* Test fonction destroyAllInfo :
    La fonction détruit une liste chainée contenant les listes chainées des différentes informations
    */
    //destroyAllInfo(ListeTests2);    erreur car frequency.c ligne 466 currentInfoList->next n'existe pas
    //destroyAllInfo(ListePaterns2);  erreur car frequency.c ligne 466 currentInfoList->next n'existe pas
    //destroyAllInfo(ListeVide2);     erreur car frequency.c ligne 466 currentInfoList->next n'existe pas



    //Supression liste de mots
    list_destroy(listeMots);

    return 0;
}