https://www.hko.gov.hk/wxinfo/currwx/climatjs/9day0127_0204.js 
//后缀日期为起始日期到结束日期


需求：
1：9天的天气预报
2：后天的湿度数据
9天天气预报
https://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json
Note:过了中午十二点后会变第二天开始

抓包方法：
1.模拟器装软件抓包--失败--fiddler
2.手机装软件抓包--失败--fiddler
3.Root手机通过tcpdump 抓包，Wireshark解包，只有ip但没有对应的host信息和请求头信息
4.根据3获得的ip直接访问网站，通过浏览器抓包成功

抓包时间：
抓包花费近两小时
解析花费近一小时
投机取巧花费五分钟
