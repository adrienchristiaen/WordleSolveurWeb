#include "frequency.h"

void freqScore(list_t *oneList, char *freqList, char *alphabet) //Possibilité de créer alphabet dans la fonction directement
{
    element_t *myElem = oneList->premier; //Initialisation au premier élément de la liste

    while (myElem->suivant != NULL) //Le dernier élément pointe vers NULL
    {
        char* myWord = myElem->mot;
        int length = 5; //A changer par une variable globale

        for (int i=0; i<length; i++) //Parcours toutes les lettres du mot
        {
            for (int j=0; j<26; j++) //Parcours les lettres de l'alphabet
            {
                if (myWord[i] == alphabet[j]) //Même lettres
                {
                    myElem->freqScore += freqList[j]; //Ajout de la fréquence au score de l'élément
                }
            }
        }
    }
}


listinfo_t* createListInfo()
{
    listinfo_t *myList = malloc(sizeof(*myList));
    myList->premier = NULL;

    if (myList == NULL)
    {
        perror("no memory enough for listinfo");
    }

    return myList;
}


void info_print(info_t *one_info)
{
    printf("%s: %d", one_info->result, one_info->match);
}


void listInfo_print(listinfo_t *one_list)
{
    info_t *info = one_list->premier;
    info_t *infoSuivant;
    printf("(");
    info_print(info);

    if (info == NULL)
    {
        printf(")\n");
        return;
    }

    while (info->suivant != NULL)
    {
        infoSuivant = info->suivant;
        info = infoSuivant;
        printf(" -> ");
        info_print(info);
    }

    printf(")\n");
}


void listInfo_append(listinfo_t *one_list, char *one_result)
{
    info_t *info = one_list->premier;
    
    info_t *newInfo = malloc(sizeof(*newInfo));
    newInfo->suivant = NULL;
    newInfo->match = 0;
    strcpy(newInfo->result,one_result);

    if (info == NULL)
    {
        one_list->premier = newInfo;
        return;
    }

    if (info->suivant == NULL)
    {
        if (strcmp(info->result, one_result) == 0 || strcmp(one_list->premier->result, one_result) == 0)
        {
            //printf("EXIT\n");
            free(newInfo);
            return;
        }
    }

    while (info->suivant != NULL)
    {
        //printf("%s : %s\n", info->result, one_result);
        if (strcmp(info->result, one_result) == 0 || strcmp(one_list->premier->result, one_result) == 0)
        {
            //printf("EXIT\n");
            free(newInfo);
            return;
        }
        info = info->suivant;
    }

    info->suivant = newInfo;
}


void listInfo_destroy(listinfo_t *one_list)
{
    info_t *info = one_list->premier;
    info_t *infoSuivant;

    if(info == NULL)
    {
        free(one_list);
        return;
    }

    while (info->suivant != NULL)
    {
        infoSuivant = info->suivant;
        free(info);
        info = infoSuivant;
    }

    free(info);
    free(one_list);
}


void initListInfo(listinfo_t *oneList)
{
    char tab[SIZE+1];

    for (int i=0; i<SIZE; i++)
    {
        tab[i] = '0';
    }
    tab[SIZE] = '\0';

    //printf("\nMY TEST: %s\n", tab);

    allResults(oneList, tab, 0, SIZE);
}


void allResults(listinfo_t *oneList, char* table, int i, int size)
{
    listInfo_append(oneList, table);
    //printf("%d",i);
    if (i<size)
    {
        table[i] = '0';
        allResults(oneList, table, i+1, size);
        table[i] = '1';
        allResults(oneList, table, i+1, size);
        table[i] = '2';
        allResults(oneList, table, i+1, size);
    }
}


int lengthListInfo(listinfo_t *oneList)
{
    info_t *info = oneList->premier;
    int length = 1;

    if (info == NULL)
    {
        return 0;
    }

    while (info->suivant != NULL)
    {
        length++;
        info = info->suivant;
    }

    return length;
}


void getMatches(listinfo_t *infoList, list_t *wordList, char oneWord[20])
{
    //Sauvegarde du mot
    strcpy(infoList->word, oneWord);

    //Pour chaque possibilité de pattern
    info_t *currentInfo = infoList->premier;

    while (currentInfo != NULL)
    {
        //On initialise le nombre de match pour ce pattern
        int nbMatches = 0;
        
        //Pour chaque mot
        element_t *currentElement = wordList->premier;

        while (currentElement != NULL)
        {
            int i = 0;
            int wrong = 0;
            char possibleMatch[20];
            strcpy(possibleMatch, currentElement->mot);
            while (i<SIZE && wrong == 0)
            {
                //printf("%d: ", i);
                //printf("%c - %c: ", oneWord[i], possibleMatch[i]);
                //Si les caractères sont identiques
                if (oneWord[i] == possibleMatch[i])
                {
                    //printf("SAME\n");
                    //Si le pattern montre que les caractères ne sont pas identiques
                    if (currentInfo->result[i] == '0')
                    {
                        //printf("\tPATTERN NOT CORRESPOND\n");
                        //On peut passer au mot suivant
                        wrong = 1;
                    }
                    //Si le pattern montre que le caractère est mal placé
                    else if (currentInfo->result[i] == '1')
                    {
                        //printf("\tPATTERN NOT CORRESPOND\n");
                        //On peut passer au mot suivant
                        wrong = 1;
                    }
                    else
                    {
                        //printf("\tPATTERN CORRESPOND\n");
                    }
                }
                //Si les caractères sont différents
                if (oneWord[i] != possibleMatch[i])
                {
                    //printf("DIFFERENT\n");
                    //Si le pattern montre que les caractères sont identiques
                    if (currentInfo->result[i] == '2')
                    {
                        //On peut passer au mot suivant
                        wrong = 1;
                    }
                    //Si le pattern montre que les caractères sont mal placés
                    if (currentInfo->result[i] == '1')
                    {
                        //Si le caractère n'appartient pas au mot
                        if (strchr(possibleMatch, oneWord[i]) == NULL)
                        {
                            //On peut passer au mot suivant
                            wrong = 1;
                        }
                        //Sinon
                        else
                        { 
                            //On regarde à quel endroit apparait la lettre dans le mot possible
                            int indOcc = indiceOccurence(possibleMatch, oneWord[i]);
                            //On le remplace par un chiffre
                            possibleMatch[indOcc] = '8';
                            //On passe aux lettres suivantes
                        }
                    }
                }
                i++;
            }
            if (wrong == 0)
            {
                nbMatches++;
                //printf("%s: %s - %s\n\n", currentInfo->result, oneWord, currentElement->mot);
            }
            
            //On passe au mot suivant
            currentElement = currentElement->suivant;
        }
        //On ajoute à la liste chaînée le nombre de matchs pour le pattern
        currentInfo->match = nbMatches;
        //On passe au pattern suivant
        currentInfo = currentInfo->suivant;
    }
}

int indiceOccurence(char *word, char caractere)
{
    int i = 0;
    while (word[i] != caractere)
    {
        i++;
    }
    return i;
}
