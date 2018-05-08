# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-08 14:14:03
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-08 14:23:56

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# no.1 string in side a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# no.2 string in side a string
print "I said: %r." % x
# no.3 string in side a string
print "I also said: '%s'." % y

hilarious = False
# no.4 string in side a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Python uses + to concatenate strings because that's how core developers of Python defined that operator.
print w + e