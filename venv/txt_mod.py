import re
import datetime, time

now = datetime.datetime.now()  # 定义时间

#with open('Original_list_file.txt', encoding='utf-8', ) as file:

file = open("Original_list_file.txt", "r")
content = file.readline()

while content != "":
    today = now.strftime('%Y-%m-%d')  # 定义时间格式
    content_initial = content
    content_process_step1 = re.compile(r'(?<=~).+?(?=~)')  ##匹配的字符是XX，但必须满足形式是AXXB这样的字符串
    contest_process_step2 = content_process_step1.findall(content_initial)  ##匹配所有条件
    contest_process_step3 = contest_process_step2[0:20]  ##保留前6项
    contest_process_step3.insert(0,today)  ##在列表第一个元素中插入今天的日期
    print (contest_process_step3)
    content = file.readline()
    # 输出部分
    stock_data = contest_process_step3 # 定义result读取的内容，GBK格式
    stock_data_file = open('stock_data_file.txt', 'a')  # 导入http模块，a表示追加
    stock_data_file.write(str(stock_data))
    stock_data_file.write('\n')
    stock_data_file.close()
    #conn.close()
     # 防止进入无限的循环