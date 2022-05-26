#include "delword.h"
#include <stdio.h>
#include <stdlib.h>

void suppr_tout_critere(t_elem**prem,int val)
{
t_elem*n,*sup,*prec;
    // supprimer au début
    while(*prem!=NULL && (*prem)->valeur==val){
        sup=*prem;
        *prem=(*prem)->suivant;
        free(sup);
    }
    // les suivants
    if (*prem!=NULL){
        prec=*prem;
        n=prec->suivant;
        while (n!=NULL){
            while(n!=NULL && n->valeur==val){
                sup=n;
                n=n->suivant;
                prec->suivant=n;
                free(sup);
            }
            if (n!=NULL){
                prec=n;
                n=n->suivant;
            }
        }
    }
}