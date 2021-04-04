#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>


#include "flags.h"
#include "additional_modules.h"

int sentence(char* file){
    int length = tamano(file);
    int fd = open(file,O_RDONLY);
    int pd = open(file,O_WRONLY);

    
    char buffer[100];
    char copy[100];
    int i = 0;
    int j = 0;

    while(i < length){
        /*Leer fichero*/
        read(fd,buffer,1);
        if(j == 0 && isalpha(*buffer)){
            char c = toupper(*buffer);
            copy[i] = c;
            j++;
        } else if(!isalpha(*buffer)){
            if(strcmp(buffer,".") > 0){
                copy[i] = *buffer;
                j = 0;
                i++;
                continue;
            }
            copy[i] = *buffer;
        }else {
            copy[i] = tolower(*buffer);
            j++;
        }
        i++;
    }
    
    write(pd,copy,length);
    close(fd);
    return 0;
}

int lowerCase(char* file){
    int length = tamano(file);
    int fd = open(file,O_RDONLY);
    int pd = open(file,O_WRONLY);

    
    char buffer[100];
    char copy[100];
    int i = 0;

    while(i < length){
        /*Leer fichero*/
        read(fd,buffer,1);
        if(isalpha(*buffer)){
            char c = tolower(*buffer);
            copy[i] = c;
            
        } else{
            copy[i] = *buffer;
        }
        i++;
    }
    
    write(pd,copy,length);
    close(fd);
    return 0;

}

int upperCase(char* file){
    int length = tamano(file);
    int fd = open(file,O_RDONLY);
    int pd = open(file,O_WRONLY);

    
    char buffer[100];
    char copy[100];
    int i = 0;

    while(i < length){
        /*Leer fichero*/
        read(fd,buffer,1);
        if(isalpha(*buffer)){
            char c = toupper(*buffer);
            copy[i] = c;
            
        } else{
            copy[i] = *buffer;
        }
        i++;
    }

    write(pd,copy,length);
    close(fd);
    return 0;

}

int capitalize(char* file){
    int length = tamano(file);
    int fd = open(file,O_RDONLY);
    int pd = open(file,O_WRONLY);

    
    char buffer[100];
    char copy[100];
    int i = 0;
    int j = 0;

    while(i < length){
        /*Leer fichero*/
        read(fd,buffer,1);
        if(j == 0 && isalpha(*buffer)){
            char c = toupper(*buffer);
            copy[i] = c;
            j++;
        } else if(!isalpha(*buffer)){
            copy[i] = *buffer;
            j = 0;
        } else {
            copy[i] = tolower(*buffer);
            j++;
        }
        i++;
    }
    
    write(pd,copy,length);
    close(fd);
    return 0;

}

int toggle(char* file){
    int length = tamano(file);
    int fd = open(file,O_RDONLY);
    int pd = open(file,O_WRONLY);

    
    char buffer[100];
    char copy[100];
    int i = 0;
    int j = 0;

    while(i < length){
        /*Leer fichero*/
        read(fd,buffer,1);
        if(j == 0 && isalpha(*buffer)){
            char c = tolower(*buffer);
            copy[i] = c;
            j++;
        } else if(!isalpha(*buffer)){
            copy[i] = *buffer;
            j = 0;
        } else {
            copy[i] = toupper(*buffer);
            j++;
        }
        i++;
    }
    
    write(pd,copy,length);
    close(fd);
    return 0;

}