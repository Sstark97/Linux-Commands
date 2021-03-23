#include "additional_modules.h"
#include "flags.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
    if(validate(argc,argv[2]) == 0){
        if(strcmp(argv[1],"-s") == 0){
            sentence(argv[2]);
        } else if(strcmp(argv[1],"-U") == 0){
            upperCase(argv[2]);
        } else if(strcmp(argv[1],"-l") == 0){
            lowerCase(argv[2]);
        } else if(strcmp(argv[1],"-C") == 0){
            capitalize(argv[2]);
        } else if(strcmp(argv[1],"-t") == 0){
            toggle(argv[2]);
        } else {
            fprintf(stderr,"Invocación incorrecta: pcase [-s | l | U | C | t] fichero1 ");
            exit(-1);
        }
    } else {
        exit(-1);
    }
}