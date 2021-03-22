#!/usr/bin/env python3
import argparse

from pathlib import Path

from sys import stderr, stdout

class CpError(Exception):
    pass

class Logger:
    def __init__(self, verbosity=False):
        self.verbose = verbosity

    def set_verbosity(self,verbosity):
        self.verbose = verbosity

    def log(self,message, file=stdout):
        if self.verbose:
            print(message, file=file)
    
    def warning(self, message, file=stderr):
        print(f'WARNING: {message}',file=file)

    def error(self, message, file=stderr):
        print(f'ERROR: {message}', file=file)

logger = Logger()

def pcaseControl(src: Path, sentenceCase=False,lowwercase=False,uppercase=False,capitalizeEachWord=False,toggleCase=False):
    if src.is_file():
        if sentenceCase:
            toSentenceCase(src,sentenceCase)
        elif lowwercase:
            toLowerCase(src,lowwercase)
        elif uppercase:
            toUpperCase(src,uppercase)
        elif capitalizeEachWord:
            toCapitalizeEachWord(src,capitalizeEachWord)
        else:
            toToggleCase(src,toggleCase)
    else:
        logger.error(f'{src} is not a File')

def toSentenceCase(src: Path,sentenceCase):
    logger.log(f'Apply sentence case to {src.name}')
    file = open(src,'r+')
    text = file.readlines()
    
    for i in range(0,len(text)):
        sentence = text[i]
        new = ""
        p = 0
        for j in range(0,len(sentence)):
            if sentence[j] == '.':
                p = 0
                new += sentence[j]
            elif p == 0:
                new += sentence[j].upper()
                p += 1
            else:
                new += sentence[j]
                p += 1
        text[i] = new
    
    file.seek(0)
    file.writelines(text)
    file.close()    

def toLowerCase(src: Path,lowwercase):
    logger.log(f'Apply lower case to {src.name}')
    file = open(src,'r+')
    text = file.readlines()
    
    for i in range(0,len(text)):
        text[i] = text[i].lower()

    file.seek(0)
    file.writelines(text)
    file.close()

def toUpperCase(src: Path,uppercase):
    logger.log(f'Apply upper case to {src.name}')
    file = open(src,'r+')
    text = file.readlines()
    
    for i in range(0,len(text)):
        text[i] = text[i].upper()
    
    file.seek(0)
    file.writelines(text)
    file.close()

def toCapitalizeEachWord(src: Path,capitalizeEachWord):
    logger.log(f'Apply capitalize each word to {src.name}')
    file = open(src,'r+')
    text = file.readlines()
    
    for i in range(0,len(text)):
        text[i] = text[i].title()
    
    file.seek(0)
    file.writelines(text)
    file.close()

def toToggleCase(src: Path,toggleCase):
    logger.log(f'Apply toggle case to {src.name}')
    file = open(src,'r+')
    text = file.readlines()
    
    for i in range(0,len(text)):
        sentence = text[i]
        new = ""
        p = 0
        for j in range(0,len(sentence)):
            if not sentence[j].isalpha():
                p = 0
                new += sentence[j]
            elif p == 0:
                new += sentence[j].lower()
                p += 1
            else:
                new += sentence[j].upper()
                p += 1
        text[i] = new
    
    file.seek(0)
    file.writelines(text)
    file.close()
    

def pcase() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='pcase',
        description='pcase command implementation in Python, this command is only apply in the same directory of the terminal is running'
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-s', '--sentenceCase',
        action='store_true',
        help='Change all the sentences contained in the file by capitalizing the first letter of the initial word of each sentence'
    )

    group.add_argument(
        '-l', '--lowwercase',
        action='store_true',
        help='It will put all the text contained in the file in lowercase'
    )

    group.add_argument(
        '-U', '--uppercase',
        action='store_true',
        help='It will put all the text contained in the file in capital letters'
    )

    group.add_argument(
        '-C', '--capitalizeEachWord',
        action='store_true',
        help='It will put the first letter of each word contained in the file in capital letter'
    )

    group.add_argument(
        '-t', '--toggleCase',
        action='store_true',
        help='It will put the first letter of each word contained in the file in lowercase and the rest in capital letter'
    )

    parser.add_argument(
         '-v', '--verbose',
         action='store_true',
         help='Give details about actions being performed'
    )

    parser.add_argument(
         'source',
         type=Path,
         help='Source file'
    )

    return parser.parse_args()


def main():
     args = pcase()
     try:
         logger.set_verbosity(args.verbose)
         pcaseControl(args.source,args.sentenceCase,args.lowwercase,args.uppercase,args.capitalizeEachWord,args.toggleCase)
         print(Path('ULPGC/Plan Nuevo/frase ').is_absolute())
         print(Path('ULPGC/Plan Nuevo/frase ').is_file())
     except CpError as e:
         logger.error(e)
         exit(1)
     except KeyboardInterrupt:
         logger.warning('\nInterrupted')
    

if __name__ == '__main__':
    main()