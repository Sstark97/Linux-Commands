#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

#include "additional_modules.h"

int tamano(char* file){
    int fd = open(file,O_RDONLY);
    struct stat estado;
    fstat(fd,&estado);
    close(fd);
    return estado.st_size;
}

int validate(int argc, char* file){
    if(argc != 3){
        fprintf(stderr,"Invocación incorrecta: pcase [-s | l | U | C | t] fichero1 ");
        return -1;
    }

    if(tamano(file) == 0){
        fprintf(stderr,"El fichero está vacío");
        return -1;
    }

    int fileComprobe = open(file,O_RDONLY);

    if(fileComprobe == -1){
        fprintf(stderr,"Error %d: %s\n",errno,strerror(errno));
        return -1;
    }

    close(fileComprobe);
    return 0;

}