# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/27
import numpy as np
import cv2,time,threading
from PIL import ImageGrab
import pyautogui as pyag

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开始线程：" + self.name)
        start_recording()
        print ("退出线程：" + self.name)


record_state=True
def start_recording():
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv2.VideoWriter('output.avi', fourcc, 30, pyag.size())  # 参数分别为 输出文件名，解码方式，帧数，录像范围--当前为全屏模式
    while(True):
        global record_state
        img=ImageGrab.grab()
        img_np=np.array(img)
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) # ImageGrab获取的颜色为BGR排序，需转换为RGB
        out.write(frame)
        # cv2.imshow('screen',frame)
        if record_state==False:
            break
    out.release()
    cv2.destroyAllWindows()

def stop_recording():
    global record_state
    record_state=False

if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    # 开启新线程
    thread1.start()
    # thread1.join()
    time.sleep(10)
    stop_recording()
    print("退出主线程")