import warnings
import pymysql

db=pymysql.connect('localhost','root','123456',charset='utf8')
cursor=db.cursor()
#忽略警告
warnings.filterwarnings('ignore')

cdb='create database if not exists maoyandb'

db.commit()
cursor.close()
db.close()