# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-09 11:25:48
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 11:37:54

from sys import argv

script, first, second, third = argv
fourth = raw_input("What is your fourth variable? ")
fifth = raw_input("What is your fifth variable? ")
sixth = raw_input("What is your sixth variable? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is: ", fourth
print "Your fifth variable is: ", fifth
print "Your sixth variable is: ", sixth

print "For your script %r, these are the variables: %r, %r, %r, %r, %r, and %r."\
	% (script, first, second, third, fourth, fifth, sixth)
