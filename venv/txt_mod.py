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
    contest_process_step3 = contest_process_step2[0:5]  ##保留前6项
    contest_process_step3.insert(0,today)  ##在列表第一个元素中插入今天的日期
    print (contest_process_step3)
    content = file.readline()
    # 读文本的全文并打印出来
    #i = file.read().splitlines()
    #for a =
    #print (i)
    # 这个时候再读的话，返回EOF
#stock_price = re.compile(r'')

#regMatch = stock_price.split(line)
        #print (stock_price)