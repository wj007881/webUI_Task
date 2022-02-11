Feature: 测试网站的UI及功能

  Scenario: ui_test
    Given 开始录屏
    Given 打开浏览器并进入网站，网站是:https://crypto.com/exchange/markets
    When 点击CRO元素，检测是否点击成功
    When 点击DAI/CRO元素后面的Trade按钮,检测是否跳转
    Then 页面中应存在名称为Login or Sign Up的按钮
    And 检测按钮Login or Sign Up是否可用
    And 页面中应默认选取名称为 Buy 的元素
    And 页面中应默认选取名称为Limit的元素
    And 页面中应存在名称为Price的输入框,单位为CRO
    And 对名称为Price的输入框进行验证，验证方式为中文字符验证/特殊符号验证/英文字符验证/纯数字验证
    And 页面中应存在名称为Amount的输入框,单位为DAI
    And 对名称为Amount的输入框进行验证，验证方式为中文字符验证/特殊符号验证/英文字符验证/纯数字验证
    And 页面中应存在名称为Total的输入框,单位为CRO
    And 对名称为Total的输入框进行验证，验证方式为中文字符验证/特殊符号验证/英文字符验证/纯数字验证
    And 移动到'english.png'中心位置
    And 验证截图'language_list.png'是否存在
    And 结束录屏
#    Examples:

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