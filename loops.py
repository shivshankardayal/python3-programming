#!/usr/bin/env python

for i in range(0, 10):
    flag = False
    for j in range(0, 10):
        if i == 5 and j == 5:
            flag = True
            break
        print(i, j)

    if flag:
        break
