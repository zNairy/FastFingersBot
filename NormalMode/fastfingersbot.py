#!/usr/bin/python3
#coding: utf-8

''' Bot feito com fins de conhecimento, não recomendo, apoio ou incentivo trapaça seja qual for a situação '''

__author__ = '__Nairy__'
__version__ = ''
__contact__ = '__Nairy__#7181 or https://www.github.com/znairy/'

import pytesseract
import pyautogui as Fastfingers
import pyscreenshot as Screenshot
from threading import Thread

class FFBot(object):
    ''' nothing '''
    def __init__(self):
        self.current_frame = None
        self.second_frame = None
        self.thread_cod = 0
    
    def Start(self):
        while True:
            if(self.thread_cod == 0):
                self.current_frame = Screenshot.grab(bbox=(240, 290, 1073, 340))
                self.current_frame = pytesseract.image_to_string(self.current_frame, lang='por') + ' '
                self.StartThread()
                self.thread_cod = 1
            else:
                self.StartThread()

            for let in self.current_frame:
                Fastfingers.write(let)

            self.current_frame = self.second_frame

    def GetSecondFrame(self):
        self.second_frame = Screenshot.grab(bbox=(240, 340, 1073, 385))
        self.second_frame = pytesseract.image_to_string(self.second_frame, lang='por') + ' '

    def StartThread(self):
        thread = Thread(target=self.GetSecondFrame)
        thread.daemon=True
        thread.start()

def main():
    FastFingerBot = FFBot()
    FastFingerBot.Start()


if __name__ == '__main__':
    main()