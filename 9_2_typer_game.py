'''
利用tkinter的标准库完成一个打字游戏的项目，游戏开始，从窗口顶部下落多个不同的字符（背景自选一幅图片），当用户录入到某个字符时，其背景图片消失，改为红色并向上运动，直到出了窗口；而没能打到的字符会落入窗口底部停留。在窗口的右上角有一个计分板，每录入正确一个字符，计10分。当用户完成一个级别（1000个字符的80%）后，游戏自动升级到第二个级别，下落速度提高，每次出现字母增多。
'''
from tkinter import *
import random
import time
class fallChar(object):
    '''
        把下落的字符设计成类，相关属性和操作都放在这里
    '''
    #构造方法初始化位置属性，包含字符图片，初始位置
    def __init__(self,alphabet,speed,width,height):
        self.alphabet = alphabet
        self.bg_path = 'type_game_bg/%s.gif' % alphabet
        self.speed = speed
        self.bg = PhotoImage(file=self.bg_path)
        self.max_x = width
        self.max_y = height
        self.x = random.randint(0,self.max_x-50)
    #这个方法控制字符运动状态
    def motion(self,cv):
        cv.bind("<Key>",self.type_event)
        for startY in range(0,self.max_y+self.speed,self.speed) :
            cv.create_image(self.x,startY,image=self.bg,tag='pic')
            cv.update()
            time.sleep(0.05)
            if startY+self.speed >= self.max_y:
                self.speed = -2
                print (startY,self.speed)
                break
            cv.delete("pic")
        for startY in range(self.max_y,0,self.speed):
            cv.create_image(self.x,startY,image=self.bg,tag='pic')
            cv.update()
            time.sleep(0.05)
            cv.delete("pic") 
    #监听按键
    def type_event(event):
        print (event.char)
    #定义这个方法通知计分板类
    def notify(self):
        pass
class scoreboard(object):
    #这个方法用于改变分数以及升级
    def score(self):
        pass
if __name__ == '__main__':
    root = Tk()
    wd = 800
    hg = 600
    canvas = Canvas(root,width = wd,height=hg,bg='white')
    canvas.pack()
    alphabet = 'a'
    typeA = fallChar(alphabet,2,wd,hg)
    typeA.motion(canvas)
    root.mainloop()


