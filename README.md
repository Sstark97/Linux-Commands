# Linux-Commands 

------------

## Description
In this project you will find my customs Linux-commands

------------

## pcase command
This command works with files and apply differents effects deppends of the flag. At the moment, this command can only be applied to a local file in the directory where you are located

### Installation
Use git to clone my repository
> git clone https://github.com/Sstark97/Linux-Commands.git

If you want to run this command in the terminal, first you have to give it execution permissions.
> chmod u+x pcase.py

After you move the file to /usr/bin. At this moment you can run this command if you write pcase.py.
If you want to run the command only writting pcase, you must create an alias in the file ~/.bashrc

### Flags Description
-h, --help: show the help message and exit

-s, --sentenceCase: Change all the sentences contained in the file by capitalizing the first letter of the initial word of each sentence

-l, --lowwercase: It will put all the text contained in the file in lowercase

-U, --uppercase: It will put all the text contained in the file in capital letters

-C, --capitalizeEachWord: It will put the first letter of each word contained in the file in capital letter

-t, --toggleCase: It will put the first letter of each word contained in the file in lowercase and the rest in capital letter

-v, --verbose: Give details about actions being performed

## translate command
This command works with strings and translate it to some languages.

### Installation
Use git to clone my repository
> git clone https://github.com/Sstark97/Linux-Commands.git

If you want to run this command in the terminal, first you have to give it execution permissions.
> chmod u+x translate.py

After you move the file to /usr/bin. At this moment you can run this command if you write translate.py.
If you want to run the command only writting translate, you must create an alias in the file ~/.bashrc

### Flags Description
-h, --help: show the help message and exit

-s, --spanish: Translate the sentence to Spanish

-e, --english: Translate the sentence to English

-d, --deutch: Translate the sentence to Deutch

-f, --french: Translate the sentence to French

-c, --chinese: Translate the sentence to Chinese

-j, --japanese: Translate the sentence to Japanese

-v, --verbose: Give details about actions being performed