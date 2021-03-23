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
        if self.verbose:
            print(message, file=file)
    
    def warning(self, message, file=stderr):
        print(f'WARNING: {message}',file=file)

    def error(self, message, file=stderr):
        print(f'ERROR: {message}', file=file)

logger = Logger()
translator = google_translator()

def translateControl(sentence: str, spanish=False,english=False,deutch=False,french=False,chinese=False,japanese=False):
    if spanish:
        translate_spanish(sentence,spanish)
    elif english:
        translate_english(sentence,english)
    elif deutch:
        translate_deutch(sentence,deutch)
    elif french:
        translate_french(sentence,french)
    elif chinese:
        translate_chinese(sentence,chinese)
    elif japanese:
        translate_japanese(sentence,japanese)
    else:
        logger.error(f'Use any command for translate {sentence}')

def translate_spanish(sentence: str, spanish):
    if translator.detect(sentence)[0] == 'es':
        message = translator.translate('is already in Spanish',lang_tgt='es')
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate to Spanish -> {sentence}')
        print(translator.translate(sentence,lang_tgt='es'))

def translate_english(sentence: str, english):
    if translator.detect(sentence)[0] == 'en':
        message = 'is already in English'
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate to English -> {sentence}')
        print(translator.translate(sentence,lang_tgt='en'))

def translate_deutch(sentence: str, deutch):
    if translator.detect(sentence)[0] == 'de':
        message = translator.translate('is already in Deutch',lang_tgt='de')
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate to Deutch -> {sentence}')
        print(translator.translate(sentence,lang_tgt='de'))

def translate_french(sentence: str, french):
    if translator.detect(sentence)[0] == 'fr':
        message = translator.translate('is already in French',lang_tgt='fr')
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate to French -> {sentence}')
        print(translator.translate(sentence,lang_tgt='fr'))

def translate_chinese(sentence: str, chinese):
    if translator.detect(sentence)[0] == 'zh-CN':
        message = translator.translate('is already in Chinese',lang_tgt='zh-CN')
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate Chinese -> {sentence}')
        print(translator.translate(sentence,lang_tgt='zh-CN'))

def translate_japanese(sentence: str, japanese):
    if translator.detect(sentence)[0] == 'ja':
        message = translator.translate('is already in Japanese',lang_tgt='ja')
        print(f'{sentence} ' + f'{message}')
    else:
        logger.log(f'Translate to Japanese -> {sentence}')
        print(translator.translate(sentence,lang_tgt='ja'))

def mi_translate() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='translate',
        description='translate command implementation in Python'
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-s', '--spanish',
        action='store_true',
        help='Translate the sentence to Spanish'
    )

    group.add_argument(
        '-e', '--english',
        action='store_true',
        help='Translate the sentence to English'
    )

    group.add_argument(
        '-d', '--deutch',
        action='store_true',
        help='Translate the sentence to Deutch'
    )

    group.add_argument(
        '-f', '--french',
        action='store_true',
        help='Translate the sentence to French'
    )

    group.add_argument(
        '-c', '--chinese',
        action='store_true',
        help='Translate the sentence to Chinese'
    )

    group.add_argument(
        '-j', '--japanese',
        action='store_true',
        help='Translate the sentence to Japanese'
    )

    parser.add_argument(
         '-v', '--verbose',
         action='store_true',
         help='Give details about actions being performed'
    )

    parser.add_argument(
         'source',
         type=str,
         help='Source String'
    )

    return parser.parse_args()

def main():
     args = mi_translate()
     try:
         logger.set_verbosity(args.verbose)
         translateControl(args.source,args.spanish,args.english,args.deutch,args.french,args.chinese,args.japanese)
     except CpError as e:
         logger.error(e)
         exit(1)
    
if __name__ == '__main__':
    main()
