#!/usr/bin/python3
#-*- coding=UTF-8 -*-
import math

cvd = 1.6 # double const
cvil1 = 8  # int const for MI ones
cvil2 = 2  # int const for MI Doubles
cmsqr = 1.6 # double const for SQRT calc        *

print("-------舍入函数")
print("math.ceil({0}) = {1}".format(cvd, math.ceil(cvd)))
print("math.floor({0}) = {1}".format(cvd, math.floor(cvd)))

print("-------幂和对数函数")
print("math.log({0}, {1}) = {2}".format(cvil1, cvil2, math.log(cvil1, cvil2)))
print("math.pow({0}, {1}) = {2}".format(cvil1, cvil2, math.pow(cvil1, cvil2)))
print("math.log({0}) = {1}".format(cvil1, math.log(cvil1)))
print("math.sqrt({0}) = {1}".format(cmsqr, math.sqrt(cmsqr)))
