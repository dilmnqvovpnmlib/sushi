import subprocess
import time
import csv
import sys

import pyautogui
import pyocr
import pyocr.builders
from PIL import Image


class SushiLog():
    def __init__(self):
        self.amount = 0
        self.course = 0
        self.profit = 0
        self.correct = 0
        self.average = 0
        self.mis = 0
        self.names = ['amount', 'course', 'profit', 'correct', 'average', 'mis', 'names']
    
    def make_picture(self):
        time.sleep(1)
        s = pyautogui.screenshot()
        s.save('sushi.png')

        im = Image.open('sushi.png')

        im_crop_new = im.crop((785, 375, 1120, 555))
        im_crop_new.save('new.png', quality=95)

    def make_text(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)

        tool = tools[0]
        self.txt = tool.image_to_string(
            Image.open('../display.png'),
            lang='eng',
            builder=pyocr.builders.DigitBuilder(),
        )

    
    def get_text(self):
        splited = self.txt.split(' ')
        self.amount = splited[1].replace(',', '')

        index_M = splited.index('M')
        self.course = splited[index_M-1].replace('M\n', '').replace(',', '').replace('>b\n', '').replace('\n', '')
        self.profit = splited[index_M+1].replace('&oT\n\n', '').replace(',', '').replace('&oT\n', '').replace('\n', '')

        self.correct = splited[-5].replace('47\n', '')
        self.average = splited[-3] if '.' in splited[-3] else splited[-3][:-1] + '.' + splited[-3][-1]
        self.mis = splited[-1]

        # 実際に値がキレイに抽出出来ているかのデバッグ
        print(self.amount, self.course, self.profit, self.correct, self.average, self.mis)
        
        self.result = [self.amount, self.course, self.profit, self.correct, self.average, self.mis]

        return [self.amount, self.course, self.profit, self.correct, self.average, self.mis]
    
    def make_csv(self):
        with open('./outputs/results.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(self.result)
    
    def del_files(self):
        subprocess.run(['rm', 'sushi.png', 'new.png'])

if __name__ == '__main__':
    print('Mana')
    sushilog = SushiLog()
    sushilog.make_picture()
    sushilog.make_text()
    sushilog.get_text()
    sushilog.make_csv()
    sushilog.del_files()
