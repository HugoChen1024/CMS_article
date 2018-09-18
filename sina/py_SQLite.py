import sqlite3
import info
import traceback
import sys

conn = sqlite3.connect('.\\sina\\testPY.db')
cursor = conn.cursor()

# TODO: 链接数据库成功, 
# TODO: 1. 爬取数据,存放到dict 中,生成默认数字, 开始拼接url  爬取页面内容
# TODO: 2. 将默认dict 数据更改 执行写入操作, 循环



table = 'ay_con'
my_dict = info.setSmallDict(7)

sql4 = info.dict2SQL(table,my_dict)


try:

    cursor.execute(sql4)
    conn.commit() #提交到数据库执行，一定要记提交哦  
except:
    conn.rollback() #发生错误时回滚
    traceback.print_exc()  




cursor.close()

conn.close()




