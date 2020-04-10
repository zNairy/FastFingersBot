#!/usr/bin/python3
#coding: utf-8

''' Bot feito com fins de conhecimento, não recomendo, apoio ou incentivo trapaça seja qual for a situação '''

__author__ = '__Nairy__'
__version__ = ''
__contact__ = '__Nairy__#7181 or https://www.github.com/znairy/'

import pytesseract
import pyautogui as fastfingers
import pyscreenshot as screenshot
from threading import Thread
from time import sleep

class FFBot(object):
    ''' nothing '''
    def __init__(self):
        self.current_frame = None
        self.second_frame = None
        self.thread_cod = 0
    
    def start(self):
        while True:
            if(self.thread_cod == 0):
                self.current_frame = screenshot.grab(bbox=(240, 290, 1073, 340))
                self.current_frame = pytesseract.image_to_string(self.current_frame, lang='por') + ' '
                self.start_thread()
                self.thread_cod = 1
            else:
                self.start_thread()
            fastfingers.write(self.current_frame)
            sleep(1.3)
            self.current_frame = self.second_frame

    def get_second_frame(self):
        self.second_frame = screenshot.grab(bbox=(240, 340, 1073, 385))
        self.second_frame = pytesseract.image_to_string(self.second_frame, lang='por') + ' '

    def start_thread(self):
        thread = Thread(target=self.get_second_frame)
        thread.daemon=True
        thread.start()

def main():
    FastFingerBot = FFBot()
    FastFingerBot.start()


if __name__ == '__main__':
    main()