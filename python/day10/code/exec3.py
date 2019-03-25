

s = '''
y = 20000
z = x + y
x = 10000
print(x, "+", y, "=", z)
'''

global_dict = {'x':30}
exec(s, global_dict)
# print("global_dict=", global_dict)
for key in global_dict:
    print(key)


# exec(s)
# print(x, y, z)
