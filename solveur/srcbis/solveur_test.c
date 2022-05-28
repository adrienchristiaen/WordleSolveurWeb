#include "solveur.h"

int main()
{
    /* TEST CREATION LISTE */
    /* UPDATELIST
    list_t* liste_mots = list_create();
    //printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    unsigned int taille_mot=strlen(liste_mots->premier->mot);
    //printf("%d taille mot \n",taille_mot);
    //printf("LIST PRINT\n");
    list_print(liste_mots);
    freqScore(liste_mots);
    char* mot = giveProposition(liste_mots);
    char win[taille_mot+2];
    for (unsigned int i = 0;i<taille_mot;i++)
    {
        win[i]='2'; 
        //printf("%s\n",win);
    } 
    int nb_coups=1;
    printf("%s\n",mot);
    char* combinaison = getResult(taille_mot);
    while (strcmp(combinaison,"-1")!=0 && strcmp(liste_mots->premier->mot,"")!=0)
    {
        while (strcmp(combinaison,"0")==0)
        {
            combinaison = getResult(taille_mot);
        }
        updateList(liste_mots,mot,combinaison);
        if (strcmp(liste_mots->premier->mot,"")!=0)
        {
            list_print(liste_mots);
            freqScore(liste_mots);
            mot = giveProposition(liste_mots);
            nb_coups+=1;
            printf("%s\n",mot);
            //printf("Score premier mot %lf\n",liste_mots->premier->freqScore);
            combinaison = getResult(taille_mot);
            //printf("%s,%s,%d\n",combinaison,win,strcmp(combinaison,win));
            if (strcmp(combinaison,win)==-1) 
            {
                printf("Victoire du solveur en %d coups ! \n",nb_coups);
            }
        } 
        else
        {
            printf("Aucun mot n'est possible : ");
            list_print(liste_mots);
            printf("\n");
        }
    }*/
    //UPDATELISTV2
    list_t* liste_mots = list_create();
    //printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    unsigned int taille_mot=strlen(liste_mots->premier->mot);
    //printf("%d taille mot \n",taille_mot);
    //printf("LIST PRINT\n");
    list_print(liste_mots);
    freqScore(liste_mots);
    char* mot = giveProposition(liste_mots);
    printf("%s\n",mot);
    char* combinaison = getResult(taille_mot);
    while (strcmp(combinaison,"-1")!=0 && strcmp(liste_mots->premier->mot,"")!=0)
    {
        while (strcmp(combinaison,"0")==0)
        {
            combinaison = getResult(taille_mot);
        }
        updateListV2(liste_mots,mot,combinaison);
        if (strcmp(liste_mots->premier->mot,"")!=0)
        {
            list_print(liste_mots);
            freqScore(liste_mots);
            mot = giveProposition(liste_mots);
            printf("%s\n",mot);
            printf("Score premier mot %lf\n",liste_mots->premier->freqScore);
            combinaison = getResult(taille_mot);
        }
        else
        {
            printf("Aucun mot n'est possible : ");
            list_print(liste_mots);
            printf("\n");
        }
    }
    /* TEST FREQUENCE */
    listinfo_t *infoList = createListInfo();
    initListInfo(infoList);
    //listInfo_print(infoList);
    int len = lengthListInfo(infoList);
    printf("My length is: %d\n",len);

    //getMatches(infoList, liste_mots, "POULE");
    //listInfo_print(infoList);

    //Suppression des listes
    listInfo_destroy(infoList);
    list_destroy(liste_mots);
    return 0;
}

