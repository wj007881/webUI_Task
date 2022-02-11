# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/27
import numpy as np
import cv2,time,threading,sys
from PIL import ImageGrab
import pyautogui as pyag

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.record_state=True
    def run(self):
        print ("开始录制视频")
        self.start_recording()
        print ("结束录制")


    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        time_st=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(int(round(time.time()*1000))/1000))
        # print(time_st)
        video_name='./video/output'+time_st+'.avi'
        # print(video_name)
        out = cv2.VideoWriter(video_name, fourcc, 30, pyag.size())# 参数分别为 输出文件名，解码方式，帧数，录像范围--当前为全屏模式
        time.sleep(3)
        while (True):
            img=ImageGrab.grab()
            img_np=np.array(img)
            frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) # ImageGrab获取的颜色为BGR排序，需转换为RGB
            out.write(frame)
            self.check_state()
            if self.record_state != True:
                break
            # cv2.imshow('screen',frame)
        out.release()
        cv2.destroyAllWindows()
    def check_state(self):
        try:
            with open('default.txt', 'r+') as f:
                f.readline().split('=')
                state=f.readline().split('=')[1]
                # print(state)
                if state!='True':
                    self.record_state=False
        finally:
            if f:
                f.close()
    def stop_recording(self):
        self.record_state=False

if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread1", 1)
    # 开启新线程
    thread1.start()
    thread1.join()

    # print("退出主线程")