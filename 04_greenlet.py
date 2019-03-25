from greenlet import greenlet

def f1():
    print(12)
    gr2.switch()
    print(34)

def f2():
    print(56)
    gr1.switch()
    print(78)

#创建携程
gr1=greenlet(f1)
gr2=greenlet(f2)
gr1.switch()
gr2.switch()