# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-09 13:43:28
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 13:50:16

from sys import argv

script, user_name, time = argv
prompt = '==> '

print "Hi %s, I'm the %s script. This is %s o' clock" % (user_name, script, time)
print "I'd like to ask you a few questions."

print "How old are you %s?" % user_name
old = raw_input(prompt)

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, you're %r year old.
You also said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (old, likes, lives, computer)