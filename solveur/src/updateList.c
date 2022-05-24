#include "solveur.h"
#include "updateList.h"
#include "getResult.c"
#include <stdio.h>
#include <stdlib.h>

void updateList(char *mot_prop,list_t *oneList){
    char text[12];
    int inutile = getResult(&text);
    int i, j;
    for(i=0 ; i<12 ; i++) {
	    if (text[i]==2){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (actuel->mot[i]!=mot_prop[i]){
                    
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==0){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (strchr(actuel->mot,mot_prop[i] != NULL)){
                    
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==1){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (strchr(actuel->mot,mot_prop[i] == NULL)){
                    
                }
                actuel = actuel->suivant;
            }  
        }
    }   
    int doublons[12];
    for (i = 0 ; i < 12 ; i++) {
        doublons[i] = 0;
    }
    for (i = 0; i < 12; i++) {
        for (j = i + 1; j < 12;) {
            if (mot_prop[j] == mot_prop[i] && text[j]!=0 && text[i]!=0) {
                doublons[i]++;
            }
        }
    }
    for (i = 0 ; i < 12 ; i++) {
        if (doublons[i]>=2) {
            element_t *actuel = oneList->premier;
            while (actuel != NULL) {   
                if (presentXfois(actuel->mot, doublons[i], mot_prop[i])==0){
                    
                }
                actuel = actuel->suivant;
            }
        }
    }
}

int presentXfois(char *tab, int x, char lettre) {
    int i;
    int y = 0;
    for (i = 0 ; i < 12 ; i++) {
        if (tab[i]==lettre) {
            y++;
        }
    }
    if (x==y) {
        return(1);
    }
    else {
        return(0);
    }
}

int main() {
    char mot[12];
    list_t oneList;
    updateList(&mot,&oneList);
    return 0;
}