# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-12 21:03:46
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-12 21:03:59

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num