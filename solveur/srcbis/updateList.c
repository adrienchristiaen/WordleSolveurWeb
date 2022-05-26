#include "solveur.h"



void updateList(list_t *oneList,char *mot_prop,int combinaison)
{
    char text[20];
    sprintf(text, "%d", combinaison);
    int i, j;
    for(i=0 ; i<20 ; i++) {
	    if (text[i]==2){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) 
            {   
                if (actuel->mot[i]!=mot_prop[i])
                {
                    supprimeMot(oneList, actuel->mot);
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==0){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) 
            {   
                if (strchr(actuel->mot,mot_prop[i]) != NULL)
                {
                    supprimeMot(oneList, actuel->mot);
                }
                actuel = actuel->suivant;
            }
        }
        else if (text[i]==1){
            element_t *actuel = oneList->premier;
            while (actuel != NULL) 
            {   
                if (strchr(actuel->mot,mot_prop[i]) == NULL)
                {
                    supprimeMot(oneList, actuel->mot);
                }
                actuel = actuel->suivant;
            }  
        }
    }   
    int doublons[20];
    for (i = 0 ; i < 20 ; i++) {
        doublons[i] = 0;
    }
    for (i = 0; i < 20; i++) {
        for (j = i + 1; j < 20;) {
            if (mot_prop[j] == mot_prop[i] && text[j]!=0 && text[i]!=0) {
                doublons[i]++;
            }
        }
    }
    for (i = 0 ; i < 20 ; i++) {
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
    for (i = 0 ; i < 20 ; i++) {
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

