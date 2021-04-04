/*
Interfaz con las funciones que modificaran el fichero dependiendo del flag 
Autor: Aitor Santana Cabrera
Fecha: 23/03/21
*/

/*
Cambiará todas las frases contenidas en los ficheros
poniendo la primera letra de la palabra inicial de cada frase en
mayúscula.
*/
int sentence(char** file,int argc);

/*
Pondrá todo el texto contenido en los ficheros en
minúscula.
*/
int lowerCase(char** file,int argc);

/*
Pondrá todo el texto contenido en los ficheros
en MAYÚSCULA.
*/
int upperCase(char** file,int argc);

/*
Pondrá la primera letra de cada
palabra contenida en los ficheros en Mayúscula.
*/
int capitalize(char** file,int argc);

/*
Pondrá la primera letra de cada palabra
contenida en los ficheros en mINÚSCULA y el resto en mAYÚSCULA.
*/
int toggle(char** file,int argc);