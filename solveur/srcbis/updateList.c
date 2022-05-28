#include "solveur.h"


void updateList(list_t *oneList,char *mot_prop,char* combinaison)
{
    unsigned int taille_mot = strlen(mot_prop);
    //printf("%d",taille_mot);
    char text[taille_mot+1];
    strcpy(text,combinaison);
    for(unsigned int i=0 ; i<taille_mot ; i++) 
    {
        if (strcmp(oneList->premier->mot, "")!=0)
        {
            printf("Etude de l'élément: %d du pattern: %s.\n", i, text);
            //printf("%c\n",text[i]);
            if (text[i]=='2')
            {
                element_t *actuel = oneList->premier;
                while (actuel != NULL) 
                {   
                    //printf("%c,%c\n",actuel->mot[i],mot_prop[i]);
                    if (actuel->mot[i]!=mot_prop[i])
                    {
                        //printf("ca passe\n");
                        element_t* temp=actuel;
                        actuel = actuel->suivant;
                        supprimeMot(oneList, temp->mot);
                    }
                    else
                    {
                        actuel = actuel->suivant;
                    }
                }
            }
            else if (text[i]=='0')
            {
                //printf("Elem of pattern is 0.\n");
                element_t *actuel = oneList->premier;
                while (actuel != NULL) 
                {   
                    //printf("Current word: %s.\n", actuel->mot);
                    //printf("Lettre indice %d du mot actuel %s comparé: %c.\n", i, actuel->mot, actuel->mot[i]);
                    // printf("Lettre indice: %d.\n", i);
                    // printf("Mot proposé: %s.\n", mot_prop);
                    // printf("Indice mot proposé: %c.\n", mot_prop[i]);
                    //printf("Lettre indice %d du mot proposé %s comparé: %c.\n\n", i, mot_prop, mot_prop[i]);
                    if (actuel->mot[i] == mot_prop[i])
                    {
                        //printf("ca passe\n");
                        element_t* temp=actuel;
                        actuel = actuel->suivant;
                        supprimeMot(oneList, temp->mot);
                    }
                    else
                    {
                        actuel = actuel->suivant;
                    }
                }
            }
            //Cas où l'élément du pattern vaut 1
            else
            {
                element_t *actuel = oneList->premier;
                while (actuel != NULL) 
                {   
                    //Si le pattern montre que les caractères sont identiques
                    if (strchr(actuel->mot,mot_prop[i]) == NULL)
                    {
                        //Suppression du mot de la liste
                        element_t* temp=actuel;
                        actuel = actuel->suivant;
                        supprimeMot(oneList, temp->mot);
                    }
                    else if (actuel->mot[i]==mot_prop[i])
                    {
                        //Suppression du mot de la liste
                        element_t* temp=actuel;
                        actuel = actuel->suivant;
                        supprimeMot(oneList, temp->mot);
                    }
                    //Si le pattern montre que les mots sont différents
                    else
                    {
                        actuel = actuel->suivant; 
                    }
                }
            }
        }
    }
    /* int doublons[taille_mot+1];
    for (unsigned int i = 0 ; i < taille_mot+1 ; i++) 
    {
        doublons[i] = 0;
    }
    for (unsigned int i = 0; i < taille_mot+1; i++) 
    {
        for (unsigned int j = i + 1; j < taille_mot+1;j++) 
        {
            if (mot_prop[j] == mot_prop[i] && text[j]!=0 && text[i]!=0) 
            {
                doublons[i]++;
            }
        }
    }
    for (unsigned int i = 0 ; i < taille_mot+1 ; i++) 
    {
        if (doublons[i]>=2) 
        {
            element_t *actuel = oneList->premier;
            while (actuel != NULL) 
            {   
                //printf("%s\n",actuel->mot);
                if (presentXfois(actuel->mot, doublons[i], mot_prop[i])==0)
                {
                    element_t* temp=actuel;
                    actuel = actuel->suivant;
                    supprimeMot(oneList, temp->mot);
                }
                else
                {
                    actuel = actuel->suivant; 
                }
            }
        }
    } */
} 



int presentXfois(char *tab, int x, char lettre) 
{
    int y = 0;
    for (unsigned int i = 0 ; i < 20 ; i++) 
    {
        if (tab[i]==lettre) 
        {
            y++;
        }
    }
    if (x==y) 
    {
        return(1);
    }
    else 
    {
        return(0);
    }
}


