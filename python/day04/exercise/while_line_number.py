#   输入一个整数n,写程序打印如下:
#     这是第1行
#     这是第2行
#     这是第3行
#     ...
#     这是第n行

n = int(input("请输入一个整数: "))
i = 1
while i <= n:
    print("这是第%d行" % i)
    i += 1
