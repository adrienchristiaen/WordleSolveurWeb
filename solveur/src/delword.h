#include "solveur.h"

struct t_elem
{
    int valeur;
    struct t_elem *suivant;
}

typedef t_elem;