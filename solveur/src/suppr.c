#include "suppr.h"
#include <stdio.h>
#include <stdlib.h>

void suppr_tout_critere(t_elem**prem,int val)
{
t_elem*n,*sup,*prec;
    // supprimer au début
    while(*prem!=NULL && (*prem)->val==val){
        sup=*prem;
        *prem=(*prem)->suiv;
        free(sup);
    }
    // les suivants
    if (*prem!=NULL){
        prec=*prem;
        n=prec->suiv;
        while (n!=NULL){
            while(n!=NULL && n->val==val){
                sup=n;
                n=n->suiv;
                prec->suiv=n;
                free(sup);
            }
            if (n!=NULL){
                prec=n;
                n=n->suiv;
            }
        }
    }
}