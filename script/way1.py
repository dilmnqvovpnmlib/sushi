import subprocess
import time
import csv
from string import digits

import pyautogui
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
        s.save('./pictures/sushi.png')

        im = Image.open('./pictures/sushi.png')

        # im_crop_amount = im.crop((835, 375, 905, 400))
        # im_crop_amount.save('amount.png', dpi=(70, 70))

        # im_crop_course = im.crop((835, 410, 905, 430))
        # im_crop_course.save('course.png', quality=95)

        # im_crop_profit = im.crop((820, 455, 900, 482))
        # im_crop_profit.save('profit.png', quality=95)

        # im_crop_correct = im.crop((785, 528, 850, 555))
        # im_crop_correct.save('correct.png', quality=95)

        # im_crop_average = im.crop((925, 528, 975, 555))
        # im_crop_average.save('average.png', quality=95)

        # im_crop_mis = im.crop((1080, 528, 1120, 555))
        # im_crop_mis.save('mis.png', quality=95)

        im_crop_new = im.crop((785, 375, 1120, 555))
        im_crop_new.save('./pictures/new.png', quality=95)

        #subprocess.run(['rm', 'sushi.png'])
    
    def make_text(self):
        print('HEllo')
        subprocess.run(['tesseract', './pictures/new.png', 'out', '-l', 'eng'])
        # for name in self.names:
        #     subprocess.run(['tesseract', '{}.png'.format(name), name, '-l', 'eng'])
        #     break
        
    
    def get_text(self):
        output = open("out.txt", "r")
        lines = output.readlines()
        # print(lines)
        for i in range(len(lines)):
            splited = lines[i].replace('\n', '').split(' ')
            print(splited)
            if i == 1:
                self.amount = splited[1].replace(',', '')
            elif i == 2:
                self.course = splited[0].replace(',', '')
            elif i == 3:
                self.profit = splited[0].replace(',', '')
            elif i == 7:
                self.correct = splited[0]
                self.average = splited[2].replace('a', '').replace('/', '').replace('#', '')
                self.mis = splited[-2].replace('a', '').replace('/', '').replace('#', '')  if splited[-2].replace('a', '').replace('/', '').replace('#', '').isdigit() else splited[-1].replace('@', '').replace('\n', '').replace('©', '')
            else:
                continue
        output.close()

        print(self.amount, self.course, self.profit, self.correct, self.average, self.mis)
        
        self.result = [self.amount, self.course, self.profit, self.correct, self.average, self.mis]

        return [self.amount, self.course, self.profit, self.correct, self.average, self.mis]
    
    def make_csv(self):
        with open('results.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(self.result)
    
    def del_files(self):
        subprocess.run(['rm', 'new.png', 'out.txt', 'sushi.png'])

if __name__ == '__main__':
    print('Mana')
    sushilog = SushiLog()
    sushilog.make_picture()
    sushilog.make_text()
    sushilog.get_text()
    # sushilog.make_csv()
    # sushilog.del_files()
