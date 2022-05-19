#include "frequency.h"

void freqScore(list_t *oneList, char *freqList, char *alphabet) //Possibilité de créer alphabet dans la fonction directement
{
    element_t *myElem = oneList->premier; //Initialisation au premier élément de la liste

    while (myElem->suivant != NULL) //Le dernier élément pointe vers NULL
    {
        char* myWord = myElem->mot;
        int length = 5; //A changer par une variable globale

        for (int i=0; i++; i<length) //Parcours toutes les lettres du mot
        {
            for (int j=0; j++; j<26) //Parcours les lettres de l'alphabet
            {
                if (myWord[i] == alphabet[j]) //Même lettres
                {
                    myElem->freqScore += freqList[j]; //Ajout de la fréquence au score de l'élément
                }
            }
        }
    }
}
