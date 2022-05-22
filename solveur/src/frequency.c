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
    printf("%s", one_info->result);
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

    while (currentInfo->suivant != NULL)
    {
        //Pour chaque mot
        element_t *currentElement = wordList->premier;

        while (currentElement->suivant != NULL)
        {
            for (int i=0; i<SIZE; i++)
            {
                if (strcmp(oneWord[i], currentElement->mot[i]) == 0)
                {
                    
                }
            }
            
            //Incrémentation
            currentElement = currentElement->suivant;
        }
        
        //Incrémentation
        currentInfo = currentInfo->suivant;
    }
}
