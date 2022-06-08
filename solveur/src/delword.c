#include "solveur.h"



void supprimeMot(list_t *oneList, char* one_mot)
{
    element_t* actuel = oneList -> premier;
    element_t* precedent = NULL;
    //printf("%s\n",one_mot);
    if (oneList->premier == NULL) 
    {
        return;
    }

    while (strcmp(actuel->mot, one_mot)!=0 && actuel->suivant!= NULL)
    {
        //printf("%s\n",actuel->suivant->mot);
        precedent=actuel;
        actuel = actuel -> suivant;
    }
    //printf("%s\n",actuel->mot);
    //printf("%s\n",oneList->premier->mot);
    
    if (actuel->suivant == NULL)
    {
        //printf("test3\n");
        if(strcmp(actuel->mot, one_mot)==0)
        {
            if (strcmp(actuel->mot,oneList->premier->mot)==0)
                {
                    //printf("%s\n",actuel->mot);
                    free(actuel);
                    element_t* fin = malloc(sizeof(*fin));
                    strcpy(fin->mot, "");
                    fin -> freqScore = 0.0;
                    fin -> suivant = NULL;

                    oneList->premier = fin;
                }
            else
            {
                //printf("test3\n");
                precedent->suivant=actuel->suivant;
                free(actuel);
            }
        }
    }
    else
    {
        //printf("test4");
        if (strcmp(actuel->mot,oneList->premier->mot)==0)
        {
            //printf("test1");
            oneList->premier=actuel -> suivant;
            free(actuel);
            //printf("test1");
        }
        else
        {   
            //printf("Suppr :%s\n", actuel->mot);
            //printf("%s\n",actuel->suivant->mot);
            precedent->suivant=actuel->suivant;
            free(actuel);
        } 
    }
}

