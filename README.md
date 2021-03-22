# Linux-Commands 
![Alt text](https://es.wikipedia.org/wiki/Tux#/media/Archivo:Tux.svg"Optional title")

------------

## Description
In this project you will find my customs Linux-commands

------------

## pcase command
This command works with files and apply differents effects deppends of the flag. If you install the command in your PC and you write in the terminal pcase -h, you can see the differentes flags and a simple description of all of them. At the moment, this command can only be applied to a local file in the directory where you are located

### Installation
Use git to clone my repository
> git clone https://github.com/Sstark97/Linux-Commands.git

If you want to run this command in the terminal, first you have to give it execution permissions.
> chmod u+x pcase.py

After you move the file to /usr/bin. At this moment you can run this command if you write pcase.py.
If you want to run the command only writting pcase, you must create an alias in the file ~/.bashrc

### Flags Description
-s, - -sentenceCase: Change all the sentences contained in the file by capitalizing the first letter of the initial word of each sentence

-l, - -lowwercase: It will put all the text contained in the file in lowercase

-U, - -uppercase: It will put all the text contained in the file in capital letters

-C, - -capitalizeEachWord: It will put the first letter of each word contained in the file in capital letter

-t, - -toggleCase: It will put the first letter of each word contained in the file in lowercase and the rest in capital letter

-v, - -verbose: Give details about actions being performed
