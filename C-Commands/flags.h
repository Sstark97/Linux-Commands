/*
Interfaz con las funciones que modificaran el fichero dependiendo del flag 
Autor: Aitor Santana Cabrera
Fecha: 23/03/21
*/

/*
Cambiará todas las frases contenidas en
fichero1 poniendo la primera letra de la palabra inicial de cada frase en
mayúscula.
*/
int sentence(char* file);

/*
Pondrá todo el texto contenido en fichero1 en
minúscula.
*/
int lowerCase(char* file);

/*
Pondrá todo el texto contenido en fichero1
en MAYÚSCULA.
*/
int upperCase(char* file);

/*
Pondrá la primera letra de cada
palabra contenida en fichero1 en Mayúscula.
*/
int capitalize(char* file);

/*
Pondrá la primera letra de cada palabra
contenida en fichero1 en mINÚSCULA y el resto en mAYÚSCULA.
*/
int toggle(char* file);
