# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-10 13:22:07
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-10 13:46:30

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d -  %d" % (a, b)
	return a -  b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

def add_1(a, b):
	print "ADDING %d + %d + 1" % (a, b)
	return a + b + 1

def func_x(a, b, c, d):
	print "Function x: %.2f + %.2f / %.2f - %.2f" % (a, b, c, d)
	return round((a + b) / (c - d), 2)

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

n_value = add_1(30, 5)
print "add_1 value: %d\n" % n_value

x_value = func_x(24, 34, 100, 1023)
print "func_x value: %.2f\n" % x_value

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?\n"

print "The puzzle: (age + height - weight * (iq / 2)"
print "The step to solve it by hand:"
print "Div = %d" % (iq / 2)
print "Mul = %d" % (weight * iq / 2)
print "Sub = %d" % (height - weight * iq / 2)
print "Ans = %d" % (age + height - weight * iq / 2)
