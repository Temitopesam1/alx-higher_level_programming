#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
	ld = number % 10
if number < 0:
	ld = number % -10
if ld > 5:
	print(F"Last digit of {number} is {ld} and is greater than 5")
if ld == 0:
	print(F"Last digit of {number} is {ld} and is 0")
if ld < 6 and ld != 0:
	print(F"Last digit of {number} is {ld} and is less than 6 and not 0")
