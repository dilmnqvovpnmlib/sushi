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
        self.names = ['amount', 'course', 'profit', 'correct', 'average', 'mis']
        self.result = []
    
    def make_picture(self):
        time.sleep(1)
        s = pyautogui.screenshot()
        s.save('sushi.png')

        im = Image.open('sushi.png')

        im_crop_amount = im.crop((835, 375, 905, 400))
        im_crop_amount.save('amount.png', dpi=(70, 70))

        im_crop_course = im.crop((835, 410, 905, 430))
        im_crop_course.save('course.png', quality=95)

        im_crop_profit = im.crop((820, 455, 900, 482))
        im_crop_profit.save('profit.png', quality=95)

        im_crop_correct = im.crop((785, 528, 850, 555))
        im_crop_correct.save('correct.png', quality=95)

        im_crop_average = im.crop((920, 525, 975, 565))
        im_crop_average.save('average.png', quality=95)

        im_crop_mis = im.crop((1075, 525, 1125, 555))
        im_crop_mis.save('mis.png', quality=95)

        im_crop_new = im.crop((785, 375, 1120, 555))
        im_crop_new.save('new.png', quality=95)

    def make_text(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)

        tool = tools[0]

        for name in self.names:
            value = tool.image_to_string(
                Image.open('{}.png'.format(name)),
                lang='eng',
                builder=pyocr.builders.DigitBuilder(),
            )
            # もとの値のデバッグ
            print(value)
            if name == 'amount' or name == 'profit':
                value = int(value.replace(',', '').replace(' ', ''))
            elif name == 'course':
                value = int(value.replace('.', ''))
            elif name == 'mis':
                value = int(value.replace('.', ''))
            # キレイに値が抽出出来ているかのデバッグ
            print(value)
            self.result.append(value)

    def make_csv(self):
        with open('./outputs/results.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(self.result)
    
    def del_files(self):
        for name in self.names + ['sushi', 'new']:
            subprocess.run(['rm', '{}.png'.format(name)])

if __name__ == '__main__':
    sushilog = SushiLog()
    sushilog.make_picture()
    sushilog.make_text()
    sushilog.make_csv()
    sushilog.del_files()
