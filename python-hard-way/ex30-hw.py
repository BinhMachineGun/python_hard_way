# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-11 09:52:14
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-11 10:30:23

people = 100
cars = 50
buses = 30

if cars > buses and cars > people:
	print "We should take the cars, not the buses"
elif cars > buses and cars < people:
	print "We should take the buses, not the cars"
else:
	print "We should stay home."

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."