#include "additional_modules_m.h"
#include "flags_m.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

int main(int argc, char *argv[]){
    if(validate(argc,argv) == 0){
        int c;
        int sflag = 0, Uflag = 0, lflag = 0, Cflag = 0, tflag = 0;
        while((c = getopt(argc, argv, "sUlCt")) != -1){
            switch(c){
                case 's':
                    sflag = 1;
                    sentence(argv,argc);
                    break;
                case 'U':
                    Uflag = 1;
                    upperCase(argv,argc);
                    break;
                case 'l':
                    lflag = 1;
                    lowerCase(argv,argc);
                    break;

                case 'C':
                    Cflag = 1;
                    capitalize(argv,argc);
                    break;

                case 't':
                    tflag = 1;
                    toggle(argv,argc);
                    break;

                default:
                    fprintf(stderr,"Invocación incorrecta: pcase -[s | l | U | C | t] fichero1 [fichero2...]");
                    exit(-1);
            }
        }

    } else {
        exit(-1);
    }
}