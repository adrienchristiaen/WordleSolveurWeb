#include "solveur.h"


void suppr(struct list_t *oneList, struct element_t *elem)
{
    struct element_t *cur;
    struct element_t *prev;
 
    // Si la liste est vide il n'y a rien à effacer
    if (oneList->premier == NULL) return;
 
    // Positionnement des deux éléments "prev" et "cur" sur l'élément juste avant et sur l'élément à effacer
    for (cur=oneList->premier, prev=NULL; cur != elem; prev=cur, cur=cur->suivant);
 
    // Si l'élément précédent existe
    if (prev)
        // L'élément précédent prend l'adresse du suivant
        prev->suivant=cur->suivant;
    else
        // L'élément à supprimer était le premier => celui-ci change
        oneList->premier=cur->suivant;
 
    // Si l'élément à effacer était le dernier
    if (cur->suivant == NULL)
        // Le dernier élément de la liste change
        oneList->dernier=cur;
 
    // L'élément à effacer est supprimé
   free(elem);
}


// Fonction qui efface un mot de la liste
void deleteWord(char *word, struct list_t *oneList)
{
    struct element_t *cur;
 
    // Recherche du mot dans la liste
    for (cur=oneList->premier; cur != NULL; cur=cur->suivant)
    {
          if (strcmp(cur->mot, word) == 0)
             break;
    }
 
    // Si l'élément contenant le mot a été trouvé
    if (cur)
        // Il est supprimé de la liste
       suppr(oneList, cur);
}