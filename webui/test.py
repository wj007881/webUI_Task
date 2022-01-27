# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/27
import time,threading
from screen_recording import *
def show_state(str):
    print(str)

if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    # 开启新线程
    thread1.start()
    # thread1.join()
    time.sleep(10)
    stop_recording()
    print("退出主线程")