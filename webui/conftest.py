# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/27
from selenium import webdriver
import pytest,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from screen_recording import *

driver = None
@pytest.fixture(scope='session', autouse=True)
def start_fun():
    print("start")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen = _capture_screenshot()
            extra.append(pytest_html.extras.png(screen))
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra



def _capture_screenshot():
    return driver.get_screenshot_as_base64()

# @pytest.fixture(scope='session', autouse=True)
# def setup(request):
#     print('准备录屏，开始操作')
#     start_recording()
#     def fin():
#         stop_recording()
#     request.addfinalizer(fin)

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.record_state=True
        global driver
        try:
            with open('default.txt', 'r') as f:
                driver_path = f.read()
                driver_path = os.path.join(driver_path)
        finally:
            if f:
                f.close()
        if driver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            __browser_url = driver_path
            desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
            desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
            driver = webdriver.Chrome(options=chrome_options, desired_capabilities=desired_capabilities)
            driver.wait = WebDriverWait(driver, 10)
            driver.set_page_load_timeout(15)
            driver.maximize_window()
    def run(self):
        # print ("开始线程：" + self.name)
        self.start_recording()
        return driver
        # print ("退出线程：" + self.name)

    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        time_st=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(int(round(time.time()*1000))/1000))
        # print(time_st)
        video_name='./video/output'+time_st+'.avi'
        # print(video_name)
        out = cv2.VideoWriter(video_name, fourcc, 30, pyag.size())  # 参数分别为 输出文件名，解码方式，帧数，录像范围--当前为全屏模式
        while(True):
            img=ImageGrab.grab()
            img_np=np.array(img)
            frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) # ImageGrab获取的颜色为BGR排序，需转换为RGB
            out.write(frame)
            # cv2.imshow('screen',frame)
            if self.record_state==False:
                break
        out.release()
        cv2.destroyAllWindows()
    def stop_recording(self):
        self.record_state=False


@pytest.fixture(scope='session', autouse=True)
def browser():

    global driver

    try:
        with open('default.txt', 'r') as f:
            driver_path=f.readline().split('=')[1]
            driver_path=os.path.join(driver_path)
    finally:
        if f:
            f.close()
    if driver is None:
        # option = webdriver.ChromeOptions()  # 加载浏览器配置
        #
        # option.add_argument('disable-infobars')  # 浏览器不显示受自动测试软件控制
        #
        # option.add_argument('-kiosk')  # 启动时自动全屏(相当于在浏览器界面按F11按键)

        # __browser_url = driver_path
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        __browser_url = driver_path
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        driver = webdriver.Chrome(options=chrome_options)
        driver.wait = WebDriverWait(driver, 10)
        # driver.set_page_load_timeout(15)
        driver.maximize_window()
        # driver.recording=myThread(1, "Thread1", 1)
    return driver



