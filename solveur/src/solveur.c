#include "solveur.h"

list_t *list_create()
{
    list_t* liste = malloc(sizeof(*liste));

    if (liste == NULL)
    {
        perror("can't allocate a new list");
    }

    liste->premier = NULL;

    return liste;
}

void ajout_mots(list_t* list_vide)
{
    assert(list_vide != NULL);
    
    char word[6];
    
    FILE *in_file = fopen("../data/wsolf.txt", "r");
    if (!in_file)
    {
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    //list_print(list_vide);
    while(!feof(in_file))
    {
        fscanf(in_file, "%s", word);
        //printf("%s\n",word);
        list_append(list_vide, word, 0);
        //list_print(list_vide);
    }

    fclose(in_file);
}




double freq_letters(list_t *liste_mots, char lettre)
{
    assert(liste_mots != NULL);
    
    element_t* actuel = liste_mots -> premier;
    int total_lettres=0;
    int total_lettre=0;
    double result;
    while (actuel -> mot != NULL)
    {
        char* mot = actuel->mot;
        for (unsigned long i=0;i<strlen(mot);i++)
        {
            if(mot[i]==lettre)
            {
                total_lettre+=1;
            }
            total_lettres+=1;
        }
        actuel = actuel -> suivant;
    }
    result=total_lettre/total_lettres;
    return result;
}



void list_destroy(list_t *liste_mots)
{
    assert(liste_mots != NULL);
    
    element_t *aSupprimer = liste_mots->premier;
	element_t *precedent = NULL;
    while (aSupprimer != NULL)
    {
		precedent=aSupprimer;
        aSupprimer = aSupprimer -> suivant;
		free(precedent);
    }
	free(liste_mots);
}


void list_print(list_t *liste_mots)
{
    assert(liste_mots != NULL);
    
    element_t *actuel = liste_mots->premier;
    printf("[");
    printf("%s",actuel->mot);
    while (actuel->suivant != NULL)
    {
		actuel = actuel->suivant;
        printf(", %s",actuel->mot);
        //char* key = actuel -> mot;
        //double value = actuel -> freqScore;
        //printf("%s : %lf, ", key, value);  
    }
    printf("] \n");
}


void list_append(list_t *one_list, char *one_key, double one_value)
{
    assert(one_list != NULL);
    
    //printf("LIST APPEND: %s\n",one_key);

    element_t* nouveau_element = malloc(sizeof(*nouveau_element));

    if (nouveau_element == NULL)
    {
        perror("can't allocate a new element");
    }

    strcpy(nouveau_element->mot, one_key);
    //printf("LIST APPEND CHECK: %s\n",nouveau_element -> mot);
    nouveau_element -> freqScore = one_value;
    nouveau_element -> suivant = NULL; 

    element_t* actuel = one_list -> premier;

    if (actuel == NULL)
    {
        one_list->premier = nouveau_element;
        return;
    }

    while (actuel -> suivant != NULL)
    {
        //printf("%s\n",actuel->mot);
        actuel = actuel -> suivant;
    }
    actuel -> suivant = nouveau_element;
}


