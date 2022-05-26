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
    while(fscanf(in_file, "%s", word)!= EOF)
    {
        //printf("%s\n",word);
        list_append(list_vide, word, 0);
        //list_print(list_vide);
    }

    fclose(in_file);
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
    }
    else
    {
        while (actuel -> suivant != NULL)
        {
            //printf("%s\n",actuel->mot);
            actuel = actuel -> suivant;
        }
        actuel -> suivant = nouveau_element;
    }
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



int getResult(unsigned int longueur_mot) 
{
    char nombreEntre[longueur_mot+1];

    printf("Entrez la réponse : ");
    scanf("%s", nombreEntre);

    if (strcmp(nombreEntre,"-1")==0) 
	{
        printf ("La partie s'arrete\n");
        return(-1);
    }
    else if (strlen(nombreEntre)!=longueur_mot)
	{
		printf("Proposition non valide\n");
		return 0;
	}
	else
	{
        printf("La partie continue\n");
		int combinaison=0;
		for(unsigned int i=0;i<longueur_mot;i++)
		{
			char c = nombreEntre[longueur_mot-1-i];
			if (c == '2' || c == '1' || c == '0')
			{
				c = c - '0';
				combinaison+= (int)c*pow(10,i);
			}
			else
			{
				printf("Proposition non valide\n");
				return 0;
			}
			
		}
        printf("La réponse entrée est %d\n", combinaison);
        return combinaison;
    }
}

char* giveProposition(list_t* one_list)
{
    element_t *depart = one_list->premier;
    double best = 0;
    char* best_mot;
    while (depart!=NULL)
    {
        if (depart->freqScore>best)
        {
            best = depart->freqScore;
            best_mot = depart->mot;
        }
        depart = depart->suivant;
    }
    return best_mot;
}
