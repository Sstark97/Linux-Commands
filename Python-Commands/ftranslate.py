#!/usr/bin/env python3
from google_trans_new import google_translator  

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
        print(message, file=file)
    
    def warning(self, message, file=stderr):
        print(f'WARNING: {message}',file=file)

    def error(self, message, file=stderr):
        print(f'ERROR: {message}', file=file)

logger = Logger()
translator = google_translator()

def translateControl(src: Path, spanish=False,english=False,deutch=False,french=False):
    if src.is_file():
        if spanish:
            ftranslate_spanish(src,spanish)
        elif english:
            ftranslate_english(src,english)
        elif deutch:
            ftranslate_deutch(src,deutch)
        elif french:
            ftranslate_french(src,french)
        else:
            logger.error(f'Use any command for translate {src}')
    else:
        logger.error(f'{src} is not a File')

def ftranslate_spanish(src: Path, spanish):
    logger.log(f'Traslating {src.name} to Spanish...')
    file = open(src,'r+')
    text = file.readlines()

    for i in range(0,len(text)):
        if len(text[i]) == 1:
            continue
        else:
            new = translator.translate(text[i],lang_tgt='es') + "\n"
            text[i] = new

    file.seek(0)
    file.writelines(text)
    file.close()

def ftranslate_english(src: Path, english):
    logger.log(f'Traslating {src.name} to English...')
    file = open(src,'r+')
    text = file.readlines()

    for i in range(0,len(text)):
        if len(text[i]) == 1:
            continue
        else:
            new = translator.translate(text[i],lang_tgt='en') + "\n"
            text[i] = new

    file.seek(0)
    file.writelines(text)
    file.close()

def ftranslate_deutch(src: Path, deutch):
    logger.log(f'Traslating {src.name} to Deutch...')
    file = open(src,'r+')
    text = file.readlines()

    for i in range(0,len(text)):
        if len(text[i]) == 1:
            continue
        else:
            new = translator.translate(text[i],lang_tgt='de') + "\n"
            text[i] = new

    file.seek(0)
    file.writelines(text)
    file.close()

def ftranslate_french(src: Path, french):
    logger.log(f'Traslating {src.name} to French...')
    file = open(src,'r+')
    text = file.readlines()

    for i in range(0,len(text)):
        if len(text[i]) == 1:
            continue
        else:
            new = translator.translate(text[i],lang_tgt='fr') + "\n"
            text[i] = new

    file.seek(0)
    file.writelines(text)
    file.close()

def mi_translate() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='translate',
        description='translate command implementation in Python'
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-s', '--spanish',
        action='store_true',
        help='Translate the file to Spanish'
    )

    group.add_argument(
        '-e', '--english',
        action='store_true',
        help='Translate the file to English'
    )

    group.add_argument(
        '-d', '--deutch',
        action='store_true',
        help='Translate the file to Deutch'
    )

    group.add_argument(
        '-f', '--french',
        action='store_true',
        help='Translate the file to French'
    )

    parser.add_argument(
         '-v', '--verbose',
         action='store_true',
         help='Give details about actions being performed'
    )

    parser.add_argument(
         'source',
         type=Path,
         help='Source File'
    )

    return parser.parse_args()

def main():
     args = mi_translate()
     try:
         logger.set_verbosity(args.verbose)
         translateControl(args.source,args.spanish,args.english,args.deutch,args.french)
     except CpError as e:
         logger.error(e)
         exit(1)
    
if __name__ == '__main__':
    main()
