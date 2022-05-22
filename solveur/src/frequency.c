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
    info_t *myInfo = malloc(sizeof(*myInfo));
    listinfo_t *myList = malloc(sizeof(*myList));

    myList->premier = myInfo;

    myInfo->result = "_FIRST_ELEM_";
    myInfo->suivant = NULL;

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
    
    while (info->suivant != NULL)
    {
        info = info->suivant;
    }

    info_t *newInfo = malloc(sizeof(*newInfo));
    newInfo->suivant = NULL;
    newInfo->result = one_result;

    info->suivant = newInfo;
}


void listInfo_destroy(listinfo_t *one_list)
{
    info_t *info = one_list->premier;
    info_t *infoSuivant;

    while (info->suivant != NULL)
    {
        infoSuivant = info->suivant;
        free(info);
        info = infoSuivant;
    }

    free(info);
    free(one_list);
}


void initListInfo(listinfo_t *oneList, int size)
{
    char tab[6] = "00000\0";

    //printf("\nMY TEST: %s\n", tab);

    allResults(oneList, tab, 0, size);
}


void allResults(listinfo_t *oneList, char* table, int i, int size)
{
    listInfo_append(oneList, table);
    printf("%d",i);
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
