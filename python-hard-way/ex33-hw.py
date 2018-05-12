# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-12 21:07:34
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-12 21:11:03

numbers = []

def while_loop(top_value, incre_value):
	i = 0
	while i < top_value:
	    print "At the top i is %d" % i
	    numbers.append(i)

	    i += incre_value
	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i

while_loop(6, 2)

print "The numbers: "
for num in numbers:
    print num