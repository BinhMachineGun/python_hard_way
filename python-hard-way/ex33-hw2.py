# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-12 21:11:52
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-12 21:14:48

numbers = []

def for_loop(top_value, incre_value=0):
	i = 0
	for i in range(0, top_value, incre_value):
	    print "At the top i is %d" % i
	    numbers.append(i)

	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i

for_loop(6, 1)

print "The numbers: "
for num in numbers:
    print num