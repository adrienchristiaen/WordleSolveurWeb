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
    int doublons[taille_mot+1];
    for (unsigned int i = 0 ; i < taille_mot+1 ; i++) 
    {
        doublons[i] = 0;
    }
    for (unsigned int i = 0; i < taille_mot+1; i++) 
    {
        for (unsigned int j = i + 1; j < taille_mot+1;j++) 
        {
            if (mot_prop[j] == mot_prop[i])
            {
                if ((text[i]!='0') && (text[j]!='0'))
                {
                    doublons[i]++;
                }
            }
        }
    }
    for (unsigned int i = 0 ; i < taille_mot+1 ; i++) 
    {
        if (doublons[i]>=1) 
        {
            element_t *actuel = oneList->premier;
            while (actuel != NULL) 
            {   
                //printf("%s\n",actuel->mot);
                if (presentXfois(actuel->mot, doublons[i], mot_prop[i])==0)
                {
                    //printf("mot : %s\n",actuel->mot);
                    //printf("nbr : %d\n",doublons[i]);
                    //printf("lettre : %c\n",mot_prop[i]);
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
    }
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

void updateListV2(list_t *oneList,char *mot_prop,char* combinaison)
{
    unsigned int taille_mot = strlen(mot_prop);
    char combi[taille_mot+1];
    strcpy(combi,combinaison);
    char caracteresVerifies[27] = {'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};

    //Pour chaque mot
    element_t *currentElement = oneList->premier;
    element_t *beforeElement = NULL;
    element_t *nextElement = NULL;

    while (currentElement != NULL)
    {
        unsigned int i = 0;
        int wrong = 0;
        char possibleMatch[20];
        //printf("TEST\n");
        //printf("Mot: %s\n", currentElement->mot);
        strcpy(possibleMatch, currentElement->mot);
        while (i<taille_mot && wrong == 0)
        {
            //printf("%d: ", i);
            //printf("%c - %c: ", oneWord[i], possibleMatch[i]);
            //Si les caractères sont identiques
            if (mot_prop[i] == possibleMatch[i])
            {
                //printf("SAME\n");
                //Si le pattern montre que les caractères ne sont pas identiques
                if (combi[i] == '0')
                {
                    //printf("\tPATTERN NOT CORRESPOND\n");
                    //On peut supprimer le mot
                    wrong = 1;
                }
                //Si le pattern montre que le caractère est mal placé
                else if (combi[i] == '1')
                {
                    //printf("\tPATTERN NOT CORRESPOND\n");
                    //On peut supprimer le mot
                    wrong = 1;
                }
                else
                {
                    //On garde le mot dans la liste
                    //printf("\tPATTERN CORRESPOND\n");
                }
            }
            //Si les caractères sont différents
            if (mot_prop[i] != possibleMatch[i])
            {
                //printf("DIFFERENT\n");
                //Si le pattern montre que les caractères sont identiques
                if (combi[i] == '2')
                {
                    //On peut supprimer le mot
                    wrong = 1;
                }
                //Si le pattern montre que les caractères sont mal placés
                else if (combi[i] == '1')
                {
                    //Si le caractère n'appartient pas au mot
                    if (strchr(possibleMatch, mot_prop[i]) == NULL)
                    {
                        //On peut supprimer le mot
                        wrong = 1;
                    }
                    //Sinon
                    else
                    { 
                        //On regarde à quel endroit apparait la lettre dans le mot possible
                        int indOcc = indiceOccurence(possibleMatch, mot_prop[i]);
                        //On le remplace par un chiffre
                        possibleMatch[indOcc] = '8';
                        //On passe aux lettres suivantes
                    }
                }
                //Si le pattern vaut 0 (caractère non présent dans le mot)
                else
                {
                    //On vérifie qu'on a pas déjà vérifié cette lettre
                    if (strchr(caracteresVerifies,mot_prop[i]) == NULL)
                    {
                        //On supprime tous les mots qui contiennent le caractère essayé
                        printf("Caractères vérifiés: %s", caracteresVerifies);
                        printf("Supprimons tous les mots qui contiennent un: %c mal placé: %s.\n", mot_prop[i], combi);
                        //On ajoute la lettre dans la liste
                        int j = 0;
                        int etat = 0;

                        while (j < 26 && etat == 0)
                        {
                            if (caracteresVerifies[j] != '0')
                            {
                                j++;
                            }
                            else
                            {
                                caracteresVerifies[j] = mot_prop[i];
                                etat = 1;
                            }
                        }
                    }
                }
                
            }
            i++;
        }
        if (wrong == 1)
        {
            //Supression du mot en question
            //printf("Supression du mot: %s\n", currentElement->mot);
            if (beforeElement == NULL)
            {
                if (strcmp(currentElement->mot,oneList->premier->mot)==0 && currentElement->suivant == NULL)
                {
                    //printf("%s\n",currentElement->mot);
                    free(currentElement);
                    element_t* fin = malloc(sizeof(*fin));
                    strcpy(fin->mot, "");
                    fin -> freqScore = 0.0;
                    fin -> suivant = NULL;
                    currentElement = NULL;
                    oneList->premier = fin;
                }
                else
                {
                    //printf("C'est le premier mot de la liste.\n");
                    oneList->premier = currentElement->suivant;
                    nextElement = currentElement->suivant;
                    free(currentElement);
                    currentElement = nextElement;
                }
            }
            else
            {
                if (currentElement->suivant == NULL)
                {
                    //printf("C'est le dernier mot de la liste.\n");
                    free(currentElement);
                    beforeElement->suivant = NULL;
                    currentElement = NULL;
                }
                else
                {
                    nextElement = currentElement->suivant;
                    free(currentElement);
                    beforeElement->suivant = nextElement;
                    currentElement = nextElement;
                }
            }
            //printf("%s: %s - %s\n\n", currentInfo->result, oneWord, currentElement->mot);

        }
        else
        {
            //On passe au mot suivant
            beforeElement = currentElement;
            currentElement = currentElement->suivant;
        }
    }
    if (oneList->premier == NULL)
    {
        element_t *newElement;
        oneList->premier = newElement;
        strcpy(newElement->mot,"");
        newElement->freqScore = 0;
        newElement->suivant = NULL;
    }
    else
    {
        supprimeTousMotsAvec(oneList, caracteresVerifies, combinaison);
    }
}

void supprimeTousMotsAvec(list_t *oneList, char* caractereAVerifier, char *combinaison)
{
    printf("Caractères à supprimer: %s\n", caractereAVerifier);
    //Taille du mot
    unsigned int taille_mot = strlen(oneList->premier->mot);

    //Pour chaque caractère à vérifier
    int j = 0;
    while (caractereAVerifier[j] != '0' && caractereAVerifier[j] != '\0')
    {
        element_t *currentElement = oneList->premier;
        element_t *beforeElement = NULL;
        element_t *nextElement = NULL;
        
        printf("Caractère à vérifier: %c\n", caractereAVerifier[j]);
        //Pour chaque mot
        while (currentElement != NULL)
        {
            printf("Mot étudié: %s\n", currentElement->mot);
            unsigned int i = 0;
            int wrong = 0;
            char possibleMatch[20];
            strcpy(possibleMatch, currentElement->mot);
            //Pour chaque caractère
            while (i<taille_mot && wrong == 0)
            {
                //Si le mot contient un caractère à supprimer
                if (possibleMatch[i] == caractereAVerifier[j])
                {
                    //Si le caractère à supprimer n'a pas été déjà été validé
                    if (combinaison[i] == '0')
                    {
                        //Supression du mot
                        wrong = 1;
                    }
                }
                i++;
            }
            if (wrong == 1 && strcmp(oneList->premier->mot, "")!=0)
            {
                //Supression du mot en question
                printf("Supression du mot: %s\n", currentElement->mot);
                if (beforeElement == NULL)
                {
                    printf("C'est le premier mot de la liste.\n");
                    oneList->premier = currentElement->suivant;
                    nextElement = currentElement->suivant;
                    free(currentElement);
                    currentElement = nextElement;
                }
                else
                {
                    if (currentElement->suivant == NULL)
                    {
                        if (strcmp(currentElement->mot,oneList->premier->mot)==0)
                        {
                            //printf("%s\n",currentElement->mot);
                            free(currentElement);
                            element_t* fin = malloc(sizeof(*fin));
                            strcpy(fin->mot, "");
                            fin -> freqScore = 0.0;
                            fin -> suivant = NULL;

                            oneList->premier = fin;
                        }
                        else
                        {
                            printf("C'est le dernier mot de la liste.\n");
                            free(currentElement);
                            beforeElement->suivant = NULL;
                            currentElement = NULL;
                        }
                    }
                    else
                    {
                        nextElement = currentElement->suivant;
                        free(currentElement);
                        beforeElement->suivant = nextElement;
                        currentElement = nextElement;
                    }
                }
                //printf("%s: %s - %s\n\n", currentInfo->result, oneWord, currentElement->mot);

            }
            else
            {
                printf("Non supression.\n");
                //On passe au mot suivant
                beforeElement = currentElement;
                currentElement = currentElement->suivant;
            }
        }
        j++;
    }
    if (oneList->premier == NULL)
    {
        element_t *newElement;
        oneList->premier = newElement;
        strcpy(newElement->mot,"");
        newElement->freqScore = 0;
        newElement->suivant = NULL;
    }
}
