#ifndef __SOLVEUR_H__
#define __SOLVEUR_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>


typedef struct element_t element_t;

struct element_t
{
    double freqScore;
    char* mot;
    element_t *suivant;
};



typedef struct list_t list_t;

struct list_t
{
    element_t *premier;
};


/*_______________A_COMPLETER__________________*/
list_t *list_create();

void ajout_mots(list_t* list_vide);

double freq_letters(list_t *liste_mots, char lettre);

void list_destroy(list_t *liste_mots);

void list_print(list_t *liste_mots);

void list_append(list_t *one_list, char *one_key, double one_value);

#endif /*__SOLVEUR_H__*/
