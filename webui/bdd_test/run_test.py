# file_name: test_educa.py
from pytest_bdd import scenario
from UI_test import *  # 导入场景解释/支持步骤

@scenario("webui2.feature", "This is a test sample")
def test_add_course():  # 测试educa需求文件中名为"通过educa后台添加课程"的场景
    pass   # 可以不写内容, pass即可
