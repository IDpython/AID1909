import pymysql

db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 生成游标对象 (用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 执行各种数据库操作
f = open('dict.txt')
args_list = [] # [(w,m), (w,m).....]
for line in f:
    # 获取单词解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    args_list.append(tup)
f.close()


# 关闭游标和数据库链接
cur.close()
db.close()