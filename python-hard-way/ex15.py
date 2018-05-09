# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-09 13:56:24
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 14:19:40

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()