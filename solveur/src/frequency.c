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
    printf("%s: %d: %lf", one_info->result, one_info->match, one_info->bits);
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

    printf(")\n\n");
}


void listInfo_append(listinfo_t *one_list, char *one_result)
{
    info_t *info = one_list->premier;
    
    info_t *newInfo = malloc(sizeof(*newInfo));
    newInfo->suivant = NULL;
    newInfo->match = 0;
    newInfo->bits = 0;
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

double getBits(int nbMatches, int nbWords)
{
    double probability;
    //Calcul de la probabilité qu'un mot soit "accepté" par un pattern donné
    probability = (double) nbMatches/nbWords;
    //printf("%f probability\n", probability);

    double bits = 0.0;
    //Calcul de l'information obtenue (autre écriture de la proba)
    if (probability != 0)
    {
        bits = log2(1/probability);
    }

    return bits;
}

allinfo_t *getAllInfoForAllWords(list_t *wordList)
{
    //Création de la liste chaînée contenant les informations de tous les mots
    allinfo_t *allInfo = createAllInfoList();
    //Initialisation au premier mot
    element_t *currentElem = wordList->premier;

    while (currentElem != NULL)
    {
        //Initialisation liste info associée au mot
        listinfo_t *newListInfo = createListInfo();
        newListInfo->next = NULL;
        newListInfo->meanBits = 0.0;

        if (newListInfo == NULL)
        {
            perror("No memory enough.");
        }

        strcpy(newListInfo->word,currentElem->mot);
        //Remplissage de la liste info
        getAllInfoForOneWord(newListInfo, wordList, currentElem->mot);
        //Ajout à la liste allinfo
        if (allInfo->first == NULL)
        {
            allInfo->first = newListInfo;
        }
        else
        {
            listinfo_t *currentListInfo = allInfo->first;
            while (currentListInfo->next != NULL)
            {
                currentListInfo = currentListInfo->next;
            }
            currentListInfo->next = newListInfo;
        }
        //Itération élément suivant
        currentElem = currentElem->suivant;
    }
    return allInfo;
}

allinfo_t *createAllInfoList()
{
    allinfo_t *newAllInfoList = malloc(sizeof(*newAllInfoList));

    if (newAllInfoList == NULL)
    {
        perror("no memory enough for allinfo");
    }

    newAllInfoList->first = NULL;

    return newAllInfoList;
}

void getAllInfoForOneWord(listinfo_t *oneListInfo, list_t *oneWorldList, char* word)
{
    //Calcul des patterns
    initListInfo(oneListInfo);
    //Calcul des matchs
    getMatches(oneListInfo, oneWorldList, word);
    //Calcul des bits
    info_t *currentInfo = oneListInfo->premier;
    while (currentInfo != NULL)
    {
        currentInfo->bits = getBits(currentInfo->match, NBMOTS);
        currentInfo = currentInfo->suivant;
    }
    //Calcul de la moyenne des bits
    double meanBits = getMeanBits(oneListInfo);
    //Affichage
    printf("Mot: %s. Bits: %lf\n", oneListInfo->word, meanBits);
    //listInfo_print(oneListInfo);
}

double getMeanBits(listinfo_t *oneListInfo)
{
    info_t *currentInfo = oneListInfo->premier;
    double meanBits = 0;
    int nbBits = 0;
    //int nbPatterns = 0;

    while (currentInfo != NULL)
    {
        if (currentInfo->bits != 0)
        {
            nbBits += currentInfo->bits;
            //nbPatterns++;
        }
        currentInfo = currentInfo->suivant;
    }
    meanBits = (double) nbBits/243;

    return meanBits;
}

void destroyAllInfo(allinfo_t *oneAllInfo)
{
    listinfo_t *currentInfoList = oneAllInfo->first;
    listinfo_t *nextInfoList;

    while (currentInfoList->next != NULL)
    {
        nextInfoList = currentInfoList->next;
        listInfo_destroy(currentInfoList);
        currentInfoList = nextInfoList;
    }
    listInfo_destroy(currentInfoList);
    free(oneAllInfo);
}
