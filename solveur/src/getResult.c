#include "solveur.h"
#include "getResult.h"
#include <stdio.h>
#include <stdlib.h>

void getResult(char *text) {
    int nombreEntre = 0;

    printf("Entrez la réponse : ");
    scanf("%d", &nombreEntre);

    if (nombreEntre == -1) {
        printf ("La partie s'arrete\n");
    }
    else {
        printf("La partie continue\n");
        sprintf(text, "%d", nombreEntre);
        printf("La réponse entrée est %s\n", text);
    }
}


