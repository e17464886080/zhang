

s = '''
v = 100

def f1():
     
    print(v)
    print(locals())

f1()
print(v)  # 100

'''
exec(s)

