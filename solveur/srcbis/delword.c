#include "solveur.h"



void supprimeMot(list_t *oneList, char* one_mot)
{
    element_t* actuel = oneList -> premier;
    element_t* precedent = NULL;
    printf("%s\n",one_mot);
    while (strcmp(actuel->mot, one_mot)!=0 && actuel->suivant!= NULL)
    {
        //printf("%s\n",actuel->suivant->mot);
        precedent=actuel;
        actuel = actuel -> suivant;
    }
    printf("%s\n",actuel->mot);
    //printf("%s\n",oneList->premier->mot);
    
    if (actuel->suivant == NULL)
    {
        //printf("test3\n");
        if(strcmp(actuel->mot, one_mot)==0)
        {
            //printf("test3\n");
            precedent->suivant=actuel->suivant;
            free(actuel);
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
            printf("test2");
            //printf("%s\n",actuel->suivant->mot);
            precedent->suivant=actuel->suivant;
            free(actuel);
        } 
    }
}

void suppr(struct list_t *oneList, struct element_t *elem)
{
    struct element_t *cur;
    struct element_t *prev;
 
    // Si la liste est vide il n'y a rien à effacer
    if (oneList->premier == NULL) 
    {
        return;
    }
    // Positionnement des deux éléments "prev" et "cur" sur l'élément juste avant et sur l'élément à effacer
    for (cur=oneList->premier, prev=NULL; cur != elem; prev=cur, cur=cur->suivant)
    {
        // Si l'élément précédent existe
        if (prev)
            // L'élément précédent prend l'adresse du suivant
            prev->suivant=cur->suivant;
        else
            // L'élément à supprimer était le premier => celui-ci change
            oneList->premier=cur->suivant;
    }
 
    /* // Si l'élément à effacer était le dernier
    if (cur->suivant == NULL)
    {
        // Le dernier élément de la liste change
        oneList->dernier=cur;
    } */
    // L'élément à effacer est supprimé
   free(elem);
}


// Fonction qui efface un mot de la liste
void deleteWord(char *word, list_t *oneList)
{
    element_t *cur;
    printf("%s",oneList->premier->mot);
    // Recherche du mot dans la liste
    for (cur=oneList->premier; cur->suivant != NULL; cur=cur->suivant)
    {
        printf("test");
          if (strcmp(cur->mot, word) == 0)
             break;
    }
 
    // Si l'élément contenant le mot a été trouvé
    if (cur)
        // Il est supprimé de la liste
       suppr(oneList, cur);
}


