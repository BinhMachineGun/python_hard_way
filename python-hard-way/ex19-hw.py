# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-10 10:14:44
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-10 10:57:37

def dogs_and_chickens(dog_count, chicken_count):
	print "You have %d dogs!" % dog_count
	print "You have %d chickens!" % chicken_count
	print "Wow! That's a lot!"
	print "Let's show me!.\n"

# give the function numbers directly
print "We can just give the function numbers directly:"
dogs_and_chickens(20, 30)

# give the function variable
print "OR, we can use variables from our script:"
amount_of_dog = 30
amount_of_chicken = 50
dog_legs = 4
chicken_leg = 2

dogs_and_chickens(amount_of_dog, amount_of_chicken)

print "A total leg of %d dogs is %d." % (amount_of_dog, amount_of_dog * dog_legs)
print "A total leg of %d chickens is %d." % (amount_of_chicken, amount_of_chicken * chicken_leg)

# give the function math with bare number
print "We can do math addition inside:"
dogs_and_chickens(10 + 20, 5 + 6)

print "We can do math minus inside:"
dogs_and_chickens(100 - 10, 50 - 6)

print "We can do math multiply inside:"
dogs_and_chickens(10 * 2, 5 * 6)

print "We can do math division inside:"
dogs_and_chickens(100 / 10, 50 / 5)

# give the function math and variable
print "And we can combine the two, bare number, variables and math:"
dogs_and_chickens(100 + amount_of_dog, 1000 + amount_of_chicken)

print "We can combine variables and math and do math minus inside:"
dogs_and_chickens(100 - amount_of_dog, 1000 - amount_of_chicken)

print "We can combine variables and math and do math multiply inside:"
dogs_and_chickens(100 * amount_of_dog, 1000 * amount_of_chicken)

print "We can combine variables and math and do math division inside:"
dogs_and_chickens(100 / amount_of_dog, 1000 / amount_of_chicken)

# give the function variable and math
print "And we can combine the two, variables, bare number and math:"
dogs_and_chickens(amount_of_dog + 100, amount_of_chicken + 1000)

print "We can combine variables and math and do math minus inside:"
dogs_and_chickens(amount_of_dog - 10, amount_of_chicken - 10)

print "We can combine variables and math and do math multiply inside:"
dogs_and_chickens(amount_of_dog * 10, amount_of_chicken * 10)

print "We can combine variables and math and do math division inside:"
dogs_and_chickens(amount_of_dog / 10, amount_of_chicken / 10)
