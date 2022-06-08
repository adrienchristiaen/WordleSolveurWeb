#include "solveur.h"
#include "assert.h"

int list_is_empty(list_t *one_list);
double list_get_freq(list_t *one_list, int index);
char *list_get_mot(list_t *one_list, int index);

int main() {
    list_t *one_list = list_create();
    assert(list_is_empty(one_list)==1);


    list_append(one_list, "arbre", 0.2);
    assert(list_is_empty(one_list)==0);
    list_print(one_list);


    list_append(one_list, "table", 1.56);
    list_append(one_list, "loupe", 2.98);
    list_append(one_list, "tiges", 3.45);
    list_append(one_list, "tigre", 4.53);
    list_append(one_list, "hache", 5.14);


    assert(strcmp(list_get_mot(one_list, 0),"arbre") == 0);
    assert(strcmp(list_get_mot(one_list, 1),"table") == 0);
    assert(strcmp(list_get_mot(one_list, 2),"loupe") == 0);
    assert(strcmp(list_get_mot(one_list, 3),"tiges") == 0);
    assert(strcmp(list_get_mot(one_list, 4),"tigre") == 0);
    assert(strcmp(list_get_mot(one_list, 5),"hache") == 0);


    assert(list_get_freq(one_list, 0) == 0.2);
    assert(list_get_freq(one_list, 1) == 1.56);
    assert(list_get_freq(one_list, 2) == 2.98);
    assert(list_get_freq(one_list, 3) == 3.45);
    assert(list_get_freq(one_list, 4) == 4.53);
    assert(list_get_freq(one_list, 5) == 5.14);

    list_print(one_list);


    assert((indiceOccurence(list_get_mot(one_list, 0),'e'))==4);
    assert(indiceOccurence(list_get_mot(one_list, 0),'r')==1);
    assert(indiceOccurence(list_get_mot(one_list, 1),'l')==3);
    assert(indiceOccurence(list_get_mot(one_list, 2),'o')==1);
    assert(indiceOccurence(list_get_mot(one_list, 5),'h')==0);
        

    printf("getBits : %f\n",getBits(5,200));
    printf("getBits : %f\n",getBits(10,200));
    printf("getBits : %f\n",getBits(20,200));
    printf("getBits : %f\n",getBits(30,200));


    allinfo_t *oneAllInfo = getAllInfoForAllWords(one_list);
    double meanBits = getMeanBits(oneAllInfo->first);
    printf("Mean : %f\n",meanBits);
    

    char *BestWord = getBestWord(oneAllInfo);
    assert(strcmp(BestWord,"table")==0);
    free(BestWord);
    

    char* prop = giveProposition(one_list);
    assert(strcmp(prop,"hache")==0);
    assert(strcmp(prop,"tigre")!=0);
    free(prop);


    list_destroy(one_list);
    destroyAllInfo(oneAllInfo);

    return EXIT_SUCCESS;
}


int list_is_empty(list_t *one_list)
{
    assert(one_list != NULL);
    if (one_list->premier == NULL) {
        return(1);
    }
    else {
        return(0);
    }
}

char* list_get_mot(list_t *one_list, int index) {
    int pos = index;
    element_t *current = one_list->premier;
    
    while (pos > 0 && current->suivant != NULL) 
    {
        pos--;
        current = current->suivant;
    }
    assert(pos == 0);
    return current->mot;
}

double list_get_freq(list_t *one_list, int index) {

    int pos = index;
    element_t *current = one_list->premier;
    
    while (pos > 0 && current->suivant != NULL) 
    {
        pos--;
        current = current->suivant;
    }
    assert(pos == 0);
    return current->freqScore;
}
