##Word-Search-System
##项目说明：
1、词汇仅红宝石必考、基础部分，位于Vocabulary to Database/vocabulary.txt，将之存入数据库  
2、对数据库内所有单词通过有道进行爬取中文翻译，存入数据库  
3、创建flask服务端api，带参数请求获取符合条件单词  
4、网页端，负责向api发送请求

##使用说明：
云端地址:tamakooo.com   
服务器:项目内为localhost

###单词查询模式:
a、Easy-Search:支持如'twist','*ist','tw*t','tw*'类型模糊查询  
b、Re-Search:支持输入正则进行查询,但不支持非贪婪匹配
