Feature: 测试网站的UI及功能

  Scenario: ui test
    Given 打开浏览器并进入网站，网站是:https://www.baidu.com
    Given 开始录屏
#    And 打开浏览器，进入网站
    When 点击带文字:CRO的元素，检测是否点击成功
    And 点击带文字XTZ/CRO的元素后面的Trade按钮
    Then 页面中应存在名称为Login or Sign Up的按钮
#    And 页面中应默认选取名称为Limit的元素
#    And 页面中应存在名称为Price的输入框,单位为CRO
#    And 页面中应存在名称为Amount的输入框,单位为GRT
#    And 页面中应存在名称为Total的输入框,单位为CRO
    And 结束录屏

#  Scenario: fun test
#    Given 网站是:https://crypto.com/exchange/markets
#    Given 开始录屏
#    And 打开浏览器，进入网站
#    And 点击带文字CRO的元素，检测是否点击成功
#    And 点击带文字XTZ/CRO的元素后面的Trade按钮
#    Then 页面中应存在名称为Login or Sign Up的按钮
#    And 页面中应默认选取名称为Limit的元素
#    And 页面中应存在名称为Price的输入框,单位为CRO
#    And 页面中应存在名称为Amount的输入框,单位为GRT
#    And 页面中应存在名称为Total的输入框,单位为CRO
#    And 结束录屏