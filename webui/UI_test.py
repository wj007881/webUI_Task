# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/26
import time
from time import sleep

import pytest
from pytest_bdd import when, then, parsers
from pytest_bdd import scenario, given
from selenium import webdriver
from screen_recording import *
driver=None
@given(parsers.parse('打开浏览器并进入网站，网站是:{url}'))
def open_browser_then_go_to_url(browser,url):
    # global driver
    # if driver is None:
    #     driver = webdriver.Chrome('./chromedriver.exe')
    # return driver
    browser.get(url)




@given('开始录屏')
def start_record():
    print('准备录屏，30s后开始操作')
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    # 开启新线程
    thread1.start()
    time.sleep(20)

@when(parsers.parse('点击带文字:{CRO}的元素，检测是否点击成功'))
def click_method(browser,CRO):
    time.sleep(10)
    browser.find_element_by_xpath("//div[contains(text(),'CRO') and @class='e-tabs__nav-item']").click()
    time.sleep(0.5)
    browser.find_element_by_xpath("//div[contains(text(),'CRO') and @class='e-tabs__nav-item active']")

@when(parsers.parse('点击带文字{text1}/{text2}的元素后面的{Trade}按钮'))
def click_trade(browser,text1,text2,Trade):
    browser.find_element_by_xpath(" //tr/td/div/div/div/span[@class='base' and contains(text(),'"+text1+'/'+text2+"')]/following-sibling::span[@class='quote' and contains(text(),'CRO')]/../../../../following-sibling::td/div/button[contains(text(),'"+Trade+"')]").click()
    time.sleep(1)
    assert browser.current_url=='https://crypto.com/exchange/trade/spot/'+text1.upper()+'_'+text2.upper()


@then(parsers.parse('页面中应存在名称为{LoginButton}的按钮'))
def check_login_button(browser,LoginButton):
    browser.find_element_by_xpath("//div[@style!='display: none']//button[contains(text(),"+LoginButton+")]")



@then('结束录屏')
def stop_record():
    print('结束录屏')
    stop_recording()

@then('关闭浏览器')
def close_browser(browser):
    print('关闭浏览器')
    browser.quit()
# Given 网站是:<https://crypto.com/exchange/markets>
#     Given 开始录屏
#     And 打开浏览器，进入网站
#     And 点击带文字<CRO>的元素，检测是否点击成功
#     And 点击带文字<XTZ/CRO>的元素后面的<Trade>按钮
#     Then 页面中应存在名称为<Login or Sign Up>的按钮
#     And 页面中应默认选取名称为<Limit>的元素
#     And 页面中应存在名称为<Price>的输入框,单位为<CRO>
#     And 页面中应存在名称为<Amount>的输入框,单位为<GRT>
#     And 页面中应存在名称为<Total>的输入框,单位为<CRO>
#     And 结束录屏