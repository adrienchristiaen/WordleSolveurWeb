#include "solveur.h"



void supprimeMot(list_t *oneList, char* one_mot)
{
    element_t* actuel = oneList -> premier;
    element_t* precedent = NULL;
    printf("%s\n",one_mot);
    while (actuel->mot != one_mot && actuel->suivant!= NULL)
    {
        printf("%s\n",actuel->suivant->mot);
        precedent=actuel;
        actuel = actuel -> suivant;
    }
    printf("%s\n",actuel->mot);
    printf("%s\n",oneList->premier->mot);
    printf("test5");
    if (actuel->suivant == NULL)
    {
        printf("test3");
        if(actuel->mot == one_mot)
        {
            precedent->suivant=actuel->suivant;
            free(actuel);
        }
    }
    else
    {
        printf("test4");
        if (strcmp(actuel->mot,oneList->premier->mot)==0)
        {
            printf("test1");
            oneList->premier=actuel -> suivant;
            free(actuel);
            printf("test1");
        }
        else
        {   
            printf("test2");
            printf("%s\n",actuel->suivant->mot);
            precedent->suivant=actuel->suivant;
            free(actuel);
        } 
    }
}

