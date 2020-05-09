# -*- coding : utf-8 -*-
# Day ： 2019/7/3 8:39
# Author : "kate_liu"
import datetime


filename = '2020.02.%02d-研二寒假—第%d天.docx'
file = '2020.02.%02d\n我们的毕业第%d天					星期%s\n\n\n'

day = 1  # 每月的天数
term_day = 22  # 每学期的第几天
graduation_day = 574
week_list = ['日', '一', '二', '三', '四', '五', '六']
while day <= 29:  # 每月的天数, 例如2019年8月是31天
    new_filename = filename % (day, term_day)  # 组装成功的文件名

    week_day_num = datetime.datetime(2020, 2, day).strftime("%w")
    week_day = week_list[int(week_day_num)]
    new_file_demo = file % (day, graduation_day, week_day)  # 组装的文件内容模板

    with open(new_filename, 'w+', encoding='gbk') as f:
        f.write(new_file_demo)

    day += 1
    term_day += 1
    graduation_day += 1







