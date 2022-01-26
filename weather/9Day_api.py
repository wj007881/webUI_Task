# -*- coding: utf-8 -*-
# author: Ryan
# time: 2022/1/26
import requests


def get_9_day_weather():
    json_data = requests.get('https://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json').json()
    print(json_data)


def get_day_after_tomorrow():
    json_data = requests.get('https://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json').json()
    print('后天的最小湿度是:' + json_data['DYN_DAT_MINDS_FND']['Day3MinRH']['Value_Chi'])
    print('后天的最大湿度是:' + json_data['DYN_DAT_MINDS_FND']['Day3MaxRH']['Value_Chi'])
    print('The min humidity for the day after tomorrow is :' + json_data['DYN_DAT_MINDS_FND']['Day3MinRH']['Value_Chi'])
    print('The max humidity for the day after tomorrow is :' + json_data['DYN_DAT_MINDS_FND']['Day3MaxRH']['Value_Chi'])
    print('The humidity for the day after tomorrow is :' + json_data['DYN_DAT_MINDS_FND']['Day3MinRH']['Value_Chi'] + '~' +
          json_data['DYN_DAT_MINDS_FND']['Day3MaxRH']['Value_Chi']+'%')


if __name__ == '__main__':
    # get_9_day_weather()
    get_day_after_tomorrow()
