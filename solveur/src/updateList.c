#include "solveur.h"
#include "updateList.h"
#include "getResult.c"
#include <stdio.h>
#include <stdlib.h>

void updateList(char *mot,list_t *oneList){
    char text[10];
    getResult(&text);
    int i;
    int k;
    size_t n = sizeof(oneList);
    for(i=0 ; i<10 ; i++) {
	    if (text[i]==2){
            for(k=0 ; k<n ; k++){
                if (oneList[k][i] != mot[i]) {
                    supr(oneList,oneList[k])
                }
            }
        }
        else if (text[i]==0){
            for(k=0 ; k<n ; k++){
                if (Array.Exists(oneList[k], x => x == mot[i])) {
                    supr(oneList,oneList[k])
                }
            }
        }
        else if (text[i]==1){
            for(k=0 ; k<n ; k++){
                if (!(Array.Exists(oneList[k], x => x == mot[i]))) {
                    supr(oneList,oneList[k])
        }
    }
}

int main() {
    char mot[10];
    list_t oneList;
    updateList(&mot,&oneList);
    return 0;
}