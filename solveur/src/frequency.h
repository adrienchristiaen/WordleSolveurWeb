#ifndef __FREQUENCY_H__
#define __FREQUENCY_H__
#define SIZE 5
#define NBMOTS 7645

#include "solveur.h"
#include <math.h>

typedef struct info_t info_t;

struct info_t
{
    int match;
    double bits;
    char result[20];
    info_t *suivant;
};

typedef struct listinfo_t listinfo_t;

struct listinfo_t
{
    info_t *premier;
    listinfo_t *next;
    char word[20];
    double meanBits;
};

typedef struct allinfo_t allinfo_t;

struct allinfo_t
{
    listinfo_t *first;
};

void freqScore(list_t *oneList, char *freqList, char *alphabet);

listinfo_t* createListInfo();

void info_print(info_t *one_info);

void listInfo_print(listinfo_t *one_list);

void listInfo_append(listinfo_t *one_list, char *one_result);

void listInfo_destroy(listinfo_t *one_list);

void initListInfo(listinfo_t *oneList);

void allResults(listinfo_t *oneList, char* table, int i, int size);

int lengthListInfo(listinfo_t *oneList);

void getMatches(listinfo_t *infoList, list_t *wordList, char oneWord[20]);

int indiceOccurence(char *word, char caractere);

double getBits(int nbMatches, int nbWords);

allinfo_t *getAllInfoForAllWords(list_t *wordList);

allinfo_t *createAllInfoList();

void getAllInfoForOneWord(listinfo_t *oneListInfo, list_t *oneWorldList, char* word);

double getMeanBits(listinfo_t *oneListInfo);

void destroyAllInfo(allinfo_t *oneAllInfo);

char *getBestWord(allinfo_t *oneAllInfo);

#endif /*__FREQUENCY_H__*/
