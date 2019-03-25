import gevent
import time

def f1(m,n):
    print('执行函数1',m,n)
    # time.sleep(2)
    gevent.sleep(2)
    print('函数1执行结束')

def f2():
    print('执行函数2')
    # time.sleep(3)
    gevent.sleep(3)
    print('函数2执行结束')
#创建携程对象
g1=gevent.spawn(f1,10,20)
g2=gevent.spawn(f2)

gevent.joinall([g1,g2])
