# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-09 10:49:20
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 10:50:39
# Notice that we put a , (comma) at the end of each print line. This is so that
# print doesn’t end the line with a new line character and go to the next line.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)