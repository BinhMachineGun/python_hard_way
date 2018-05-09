# -*- coding: utf-8 -*-
# @Author: BinhPhan
# @Date:   2018-05-09 16:19:17
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-09 16:27:28

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL- C to abort."
# raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
out_file.close()

"""
Find out why you had to do output.close() in the code?
==============================
Source: https://mail.python.org/pipermail/tutor/2012-January/088031.html
First, Python (the language) does not promise that it will close the 
files for you. The operating system does, when the program exits.  In 
this trivial program, that's right away.  But if your program does 
something else for a while, or repeats this sequence of steps dozens of 
times, you could run out of resources, or overwrite something.

CPython, the most common implementation, does promise that the file will 
be closed when the usage count of the file object goes away.  So if you 
did any of the following, it would close the file:

    1) del output
    2) output = None
    3) output = open(someother_file, "w")

However, that's an optimization within CPython, and not necessarily 
guaranteed for other Python implementations, like IronPython or Jython.

Second, some operating system platforms won't let the same file be 
simultaneously open for readonly and for write.  So if the two filenames 
happened to be the same file (through symlink or other mechanism, or 
even using two different ways to describe the same file), you might get 
an error trying to write without having closed the input file.

Try putting the same name for both input and output file, see what it 
does.  Or use an absolute path for the input filename and a relative 
path to the same place for the output file.

The place to close the input file is right after you're done reading the 
data, and before opening the output file.
"""