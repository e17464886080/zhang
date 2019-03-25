#  yield2.py
import time
# 此示例示意用 for语句来调用生成器函数
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成结束")

for x in myyield():
    time.sleep(1)
    print(x)  # 2 3 5 7

# gen = myyield()  # gen绑定的是生成器对象
# print(gen)  # <generator object myyield at 0x7fb42d0b6f10>
# it = iter(gen)  # 向生成器来获取迭代器
# print(next(it))  # 2 向迭代器取值时,生成器函数才开始执行
# print(next(it))  # 3
# print(next(it))  # 5
# print(next(it))  # 7
# print(next(it))  # StopIteration异常



