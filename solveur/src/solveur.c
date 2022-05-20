#include "solveur.h"

list_t *list_create()
{
    list_t* liste = malloc(sizeof(*liste));
    element_t* element = malloc(sizeof(*element));
    element->mot="";
    element->freqScore=0.0;
    element->suivant=NULL;
    liste->premier=element;
    return liste;
}

void ajout_mots(list_t* list_vide)
{
    FILE *in_file = fopen("wsolf.txt", "r");
    if (!in_file)
    {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    struct stat sb; 
    char *file_contents = malloc(sb.st_size);
    int i=0;
    int j=0;
    while (fscanf(in_file, "%[^\n ] ", file_contents) != EOF) 
    {
        i+=1;
    }
    char* tableau[i];
    while (fscanf(in_file, "%[^\n ] ", file_contents) != EOF) 
    {
        tableau[j]=file_contents;
        j+=1;
    }
    for(int k=0; k<i;k++)
    {
        printf("%s",tableau[k]);
        //list_append(list_vide,tableau[k],0.0);
    }

    fclose(in_file);
}




double freq_letters(list_t *liste_mots, char lettre)
{
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
    element_t *actuel = liste_mots->premier;
    printf("%s",liste_mots->premier->suivant->mot);
    printf("[");
    while (actuel->suivant != NULL)
    {
		actuel = actuel->suivant;
        //printf("%s",actuel->mot);
        char* key = actuel -> mot;
        double value = actuel -> freqScore;
        printf("%s : %lf, ", key, value);  
    }
    printf("] \n");
}


void list_append(list_t *one_list, char *one_key, double one_value)
{
    element_t* actuel = one_list -> premier;
    while (actuel -> suivant != NULL)
    {
        actuel = actuel -> suivant;
    }
    element_t* nouveau_element = malloc(sizeof(*nouveau_element));

    actuel -> suivant = nouveau_element;

    nouveau_element -> mot = one_key;
    nouveau_element -> freqScore = one_value;
    nouveau_element -> suivant = NULL; 
}


