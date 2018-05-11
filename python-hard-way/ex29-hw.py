# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-11 09:23:12
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-11 09:30:46

people = 100
cats = 30
dogs = 50
tree = 1000

if people + dogs < tree:
    print "So cool! The world is saved!"

if people + dogs > tree:
    print "The tree is in danger! We should grow more tree!"

if people < dogs + cats:
    print "The human is doomed!"

if people > dogs + cats:
    print "Saved the animal!"

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."