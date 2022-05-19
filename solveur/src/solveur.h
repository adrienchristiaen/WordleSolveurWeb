#ifndef __SOLVEUR_H__
#define __SOLVEUR_H__



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


#endif /*__SOLVEUR_H__*/
