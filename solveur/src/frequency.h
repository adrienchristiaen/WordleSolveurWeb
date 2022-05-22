#ifndef __FREQUENCY_H__
#define __FREQUENCY_H__

#include "solveur.h"

typedef struct info_t info_t;

struct info_t
{
    char* result;
    info_t *suivant;
};

typedef struct listinfo_t listinfo_t;

struct listinfo_t
{
    info_t *premier;
};

void freqScore(list_t *oneList, char *freqList, char *alphabet);

listinfo_t* createListInfo();

void info_print(info_t *one_info);

void listInfo_print(listinfo_t *one_list);

void listInfo_append(listinfo_t *one_list, char *one_result);

void listInfo_destroy(listinfo_t *one_list);

void initListInfo(listinfo_t *oneList, int size);

void allResults(listinfo_t *oneList, char* table, int i, int size);

#endif /*__FREQUENCY_H__*/
