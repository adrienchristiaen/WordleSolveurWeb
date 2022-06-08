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
    
    char nombre[2];
    FILE *in_file1 = fopen("../data/wsolf.txt", "r");
    if (!in_file1)
    {
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    fscanf(in_file1, "%s", nombre);
    printf("%c\n",nombre[0]);
    fclose(in_file1);

    char filename[28] = "../data/liste_taille_x.txt";
    filename[21]=(char)nombre[0];

    char word[(int)nombre[0]+1];
    FILE *in_file2 = fopen(filename, "r");
    if (!in_file2)
    {
        perror("fopen"); 
        exit(EXIT_FAILURE);
    }
    //list_print(list_vide);
    int passe=0;
    while(fscanf(in_file2, "%s", word)!= EOF)
    {
        if (passe>0)
        {
            //printf("%s\n",word);
            list_append(list_vide, word, 0);
            //list_print(list_vide);
        }
        passe+=1;
    }
    
    fclose(in_file2);
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



char* getResult(unsigned int longueur_mot) 
{
    //char nombreEntre[longueur_mot+1];
    char* nombreEntre=malloc(sizeof(char)*longueur_mot+1);
    //printf("%d",longueur_mot);

    printf("Entrez la réponse : ");
    scanf("%s", nombreEntre);
    //printf("%ld",strlen(nombreEntre));
    //printf("%s",nombreEntre);
    if (strcmp(nombreEntre,"-1")==0) 
	{
        printf ("La partie s'arrete\n");
        return nombreEntre;
    }
    else if (strlen(nombreEntre)!=longueur_mot)
	{
		printf("Proposition non valide\n");
        strcpy(nombreEntre,"0");
		return nombreEntre;
	}
	else
	{
        //printf("La partie continue\n");
		for(unsigned int i=0;i<longueur_mot;i++)
		{
			char c = nombreEntre[longueur_mot-1-i];
			if (c != '2' && c != '1' && c != '0')
			{
                //printf("%c",c);
				printf("Proposition non valide\n");
				return "0";
			}		
		}
        //printf("La réponse entrée est %s\n", nombreEntre);
        return nombreEntre;
    }
}

char* giveProposition(list_t* one_list)
{
    element_t *depart = one_list->premier;
    double best = 0;
    char* best_mot = malloc(sizeof(one_list->premier->mot)+1);
    while (depart!=NULL)
    {
        if (depart->freqScore>best)
        {
            best = depart->freqScore;
            strcpy(best_mot,depart->mot);
        }
        depart = depart->suivant;
    }
    supprimeMot(one_list,best_mot);
    return best_mot;
}
