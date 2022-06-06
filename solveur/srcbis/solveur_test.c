#include "solveur.h"

int main()
{
    /* //SOLVEUR FREQUENCE
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
    updateList(liste_mots,mot,combinaison);          //Penser également à commenter la fonction dans la boucle
    //updateListV2(liste_mots,mot,combinaison);   
    while (strcmp(combinaison,"-1")!=0 && strcmp(liste_mots->premier->mot,"")!=0)
    {
        while (strcmp(combinaison,"0")==0)
        {
            combinaison = getResult(taille_mot);
        }
<<<<<<< HEAD
=======
        //updateList(liste_mots,mot,combinaison);
        updateListV2(liste_mots,mot,combinaison);
>>>>>>> origin/solveur-test
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
            updateList(liste_mots,mot,combinaison);
            //updateListV2(liste_mots,mot,combinaison);
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
<<<<<<< HEAD
    } */
=======
    }
    //Suppression des listes
    list_destroy(liste_mots);
    */
>>>>>>> origin/solveur-test

    //SOLVEUR BITS 
    list_t* liste_mots = list_create();
    //printf("AJOUT MOT\n");
    ajout_mots(liste_mots);
    unsigned int taille_mot=strlen(liste_mots->premier->mot);
    //printf("%d taille mot \n",taille_mot);
    //printf("LIST PRINT\n");
    list_print(liste_mots);

    //allinfo_t *myAllInfo = getAllInfoForAllWords(liste_mots);
    //char *mot = getBestWord(myAllInfo);

    //Pour éviter la première boucle dont on connait le résultat, mettre en commentaire les deux lignes d'au-dessus et enlver les commentaires des deux lignes d'en dessous
    allinfo_t *myAllInfo;
    char mot[6] = {'P','O','R','E','S'};

    char win[taille_mot+2];
    for (unsigned int i = 0;i<taille_mot;i++)
    {
        win[i]='2'; 
        //printf("%s\n",win);
    } 
    int nb_coups=1;
    printf("%s\n",mot);
    char* combinaison = getResult(taille_mot);
<<<<<<< HEAD
    //updateList(liste_mots,mot,combinaison);
    updateListV2(liste_mots,mot,combinaison);
    while (strcmp(combinaison,"-1")!=0 && strcmp(liste_mots->premier->mot,"")!=0)
=======
    int end = 0;
    while (strcmp(combinaison,"-1")!=0 && strcmp(liste_mots->premier->mot,"")!=0 && end==0 && liste_mots->premier->suivant != NULL)
>>>>>>> origin/solveur-test
    {
        printf("Liste->premier->suivant->mot: %s", liste_mots->premier->suivant->mot);
        while (strcmp(combinaison,"0")==0)
        {
            combinaison = getResult(taille_mot);
        }
<<<<<<< HEAD
=======
        updateList(liste_mots,mot,combinaison);
        //updateListV2(liste_mots,mot,combinaison);
>>>>>>> origin/solveur-test
        if (strcmp(liste_mots->premier->mot,"")!=0)
        {
            list_print(liste_mots);
            myAllInfo = getAllInfoForAllWords(liste_mots);
            strcpy(mot,getBestWord(myAllInfo));
            nb_coups+=1;
            printf("%s\n",mot);
            //printf("Score premier mot %lf\n",liste_mots->premier->freqScore);
            combinaison = getResult(taille_mot);
<<<<<<< HEAD
            //printf("%s,%s,%d\n",combinaison,win,strcmp(combinaison,win));
            //updateList(liste_mots,mot,combinaison);
            updateListV2(liste_mots,mot,combinaison);
            supprimeMot(liste_mots,mot);
            if (strcmp(combinaison,win)==-1) 
=======
            printf("%s,%s,%d\n",combinaison,win,strcmp(combinaison,win));
            if (strcmp(combinaison,win)==0) 
>>>>>>> origin/solveur-test
            {
                //printf("Victoire du solveur en %d coups ! \n",nb_coups);
                end = 1;
            }
        } 
        else
        {
            printf("Aucun mot n'est possible : ");
            list_print(liste_mots);
            printf("\n");
        }
<<<<<<< HEAD
    } 

    //Suppression des listes
    destroyAllInfo(myAllInfo);
    //list_destroy(liste_mots);
=======
    }
    printf("Victoire du solveur en %d coups ! \n",nb_coups);
    //Suppression des listes
    destroyAllInfo(myAllInfo);

>>>>>>> origin/solveur-test
    return 0;
}

