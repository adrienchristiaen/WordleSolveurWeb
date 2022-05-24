#include "solveur.h"
#include "updateList.h"
#include "getResult.c"
#include <stdio.h>
#include <stdlib.h>

void updateList(char *mot_prop,list_t *oneList){
    char text[10];
    int inutile = getResult(&text);
    int i;
    for(i=0 ; i<10 ; i++) {
	    if (text[i]==2){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (actuel->mot[i]!=mot_prop[i]){
                    supr(actuel->mot,oneList)
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==0){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (strchr(actuel->mot,mot_prop[i] != NULL)){
                    supr(actuel->mot,oneList)
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==1){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (strchr(actuel->mot,mot_prop[i] == NULL)){
                    supr(actuel->mot,oneList)
                }
                actuel = actuel->suivant;
            }  
        }
    }
}

int main() {
    char mot[10];
    list_t oneList;
    updateList(&mot,&oneList);
    return 0;
}