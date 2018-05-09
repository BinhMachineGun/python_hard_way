# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-09 14:19:19
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 14:22:11

from sys import argv

# Parse the argument value
script, filename = argv

# Open the file
txt = open(filename)

print "Here's your file %r:" % filename
# Read all content in the file and print out
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()