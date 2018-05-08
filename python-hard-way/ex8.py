# -*- coding: utf-8 -*-
# @Author: PythonHardWay
# @Date:   2018-05-08 15:28:07
# @Last Modified by:   BinhPhan
# @Last Modified time: 2018-05-08 15:28:28

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)