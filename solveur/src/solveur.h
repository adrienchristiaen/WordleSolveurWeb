#ifndef __SOLVEUR_H__
#define __SOLVEUR_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>


typedef struct element_t element_t;

struct element_t
{
    double freqScore;
    char mot[20];
    element_t *suivant;
};



typedef struct list_t list_t;

struct list_t
{
    element_t *premier;
};



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

/*_______________Création liste mots__________________*/
list_t *list_create();

void ajout_mots(list_t* list_vide);

double freq_letters(list_t *liste_mots, char lettre);

void list_destroy(list_t *liste_mots);

void list_print(list_t *liste_mots);

void list_append(list_t *one_list, char *one_key, double one_value);

/*_______________Fréquences__________________*/
void freqScore(list_t *oneList);

listinfo_t* createListInfo();

void info_print(info_t *one_info);

void listInfo_print(listinfo_t *one_list);

void listInfo_append(listinfo_t *one_list, char *one_result);

void listInfo_destroy(listinfo_t *one_list);

void initListInfo(listinfo_t *oneList, int size);

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



/*_______________Récupère le résultat__________________*/
char* getResult(unsigned int longueur_mot);

char* giveProposition(list_t *oneList);


/*_______________Met à jour la liste__________________*/
void supprimeMot(list_t *oneList, char*mot);

void updateList(list_t *oneList,char *mot_prop,char *combinaison);

void updateListV2(list_t *oneList,char *mot_prop,char* combinaison);

int presentXfois(char *tab, int x, char lettre);

void supprimeTousMotsAvec(list_t *oneList, char* caractereAVerifier, char *combinaison);

#endif /*__SOLVEUR_H__*/
