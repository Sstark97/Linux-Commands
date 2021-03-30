#include "additional_modules.h"
#include "flags.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

int main(int argc, char *argv[]){
    if(validate(argc,argv[2]) == 0){
        int c;
        int sflag = 0, Uflag = 0, lflag = 0, Cflag = 0, tflag = 0;
        while((c = getopt(argc, argv, "sUlCt")) != -1){
            switch(c){
                case 's':
                    sflag = 1;
                    sentence(argv[2]);
                    break;
                case 'U':
                    Uflag = 1;
                    upperCase(argv[2]);
                    break;
                case 'l':
                    lflag = 1;
                    lowerCase(argv[2]);
                    break;

                case 'C':
                    Cflag = 1;
                    capitalize(argv[2]);
                    break;

                case 't':
                    tflag = 1;
                    toggle(argv[2]);
                    break;

                default:
                    fprintf(stderr,"Invocación incorrecta: pcase -[s | l | U | C | t] fichero1");
                    exit(-1);
            }
        }

    } else {
        exit(-1);
    }
}