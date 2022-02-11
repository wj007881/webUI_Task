安装说明: 
你需要安装谷歌浏览器和对应的浏览器驱动，驱动可以从'http://npm.taobao.org/mirrors/chromedriver/'下载
然后修改default.txt文件内容为新下载的浏览器驱动路径，也可直接替换文件夹内的驱动文件
(如果你的浏览器版本是'97.0.4692.71', 那么需要下载的浏览器驱动版本是'97.0.4692.*' *号代表任意数字)
安装Python3.7或者更新版本的Python到电脑上，然后输入以下指令到命令行执行:
'pip install selenium pytest pytest-bdd pyautogui opencv-python Pillow numpy pytest-html '
如果是Windows系统,可以双击目录下inatall_package.bat脚本安装对应的Python库.

使用说明:
输入以下指令到命令行执行
'pytest ./run_test.py --html=report.html --self-contained-html'
新开一个命令行窗口输入 python +空格 
然后将screen_recording.py文件拖到窗口按回车
如果是Windows系统,可以双击目录下run_test.bat脚本运行默认测试脚本.
双击脚本运行开始后会出现两个命令行窗口，一个负责运行测试，另一个负责录制运行视频，
测试失败或者完成都会自动关闭录制视频的命令行窗口，并在video文件夹生成以output加时间戳命名的avi视频文件
测试失败或者完成都会生成report.html文件，失败时有截图

注：
由于部分网络访问https://crypto.com/exchange/markets较慢，容易导致测试失败或无法完整运行测试，出现此类问题请使用科学上网工具




How to install: 
You should install Google Chrome in your pc and download the related driver from 'http://npm.taobao.org/mirrors/chromedriver/' (e.g. if your Chrome version is '97.0.4692.71', then you should download the driver version is '97.0.4692.*' )
And modify default.txt 
chromedriver='your driver path'


Install Python3.7 or latest in your pc then type the characters to command line(CMD) and execute it:

'pip install selenium pytest pytest-bdd pyautogui opencv-python Pillow numpy pytest-html '
for Windows system, you can double click inatall_package.bat to install python package.

How to use:
Type the characters to command line(CMD) and execute it
'pytest ./run_test.py --html=report.html --self-contained-html'
Open a new CMD window then type the script as below :
'python ' and press Space  
then drag the screen_recording.py to this window and execute it

for Windows system, you can double click run_test.bat to run default test.
Double click script to run will show two command line windows, one for test and one for record video.
The video window will close automatically when test finish or test fail, and make an avi file(e.g. 'output2022-02-10-12-20-29.avi') to the video folder.
It will make a report.html file when test finish or test fail, and take a screenshot into report.html when test fail


文件目录说明/File description：
├─bdd_test                     #测试文件夹/Test folder
│      run_test.py
│      UI_test.py
│      webui2.feature
│      
├─image                        #截图存放文件夹/Screenshot folder
│      english.png
│      language_list.png
│      
├─python安装包             #python安装包文件夹/Python install package folder
│      python-3.7.2-amd64.exe
│      python-3.7.2-macosx10.6.pkg
│      
├─video                          #视频存放文件夹/Video folder
│      output.avi               #视频输出文件/Video output file
│  chromedriver.exe        #浏览器驱动文件/Browse driver
│  conftest.py                 #pytest配置文件/Pytest configuration
│  default.txt                  #测试配置文件/Test configuration
│  install_package.bat     #安装脚本/Install script
│  readme.md                #说明文档/Desc file
│  report.html                #报告网页/report webpage
│  run_test.bat               #运行脚本/Run script
│  run_test.py                #执行脚本/Execute script
│  screen_recording.py  #视频录制脚本/Video record script
│  test.py                      #测试脚本/test script
│  UI_test.py                 #测试用例执行脚本/UI test script
│  webui.feature           #BDD说明文件/BDD desc file