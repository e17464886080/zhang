#!/usr/bin/python3
import time
a=100
for i in range(a):
    c=0
    for j in range(1,i//2+1):
        if i%j==0:
            c+=j
    if c==i:
        print(c)
