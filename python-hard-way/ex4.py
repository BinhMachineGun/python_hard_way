# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-08 11:50:40
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-08 11:58:42

cars = 100
# Use floating point 4.0 for variable space_in_a_car because the space in the car is flexible.
# 4 people can be fit on 3 seats if they're small.
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars -  drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."