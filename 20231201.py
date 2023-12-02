# Each line of input contains letters and numbers
# The first digit and last digit make up a two-digit number
# We can have 1 number and also more than 2 numbers

# PART 1
# Sum up the two-digit numbers from each line

import numpy as np

f = open("input/20231201.txt", "r")
in_data = f.read()
f.close()

lines = [i for i in in_data.split("\n")]

running_sum = 0

# Strip all alphabetic characters and the first and last characters must be numeric
for l in lines:
    l = l.strip("abcdefghijklmnopqrstuvwxyz")
    running_sum+=int(l[0]+l[-1])

#print(running_sum)

# PART 2
# Some of the digits are spelled out, so look for "one", "two", ..., "nine"
# Probably need to split this into two passes: one for the first digit, one for the last

first = []
last = []

running_sum = 0

# First digit
for l in lines:
    lstart = l
    #print(l)

    l = l.replace("four","4")
    l = l.replace("six","6")

    l = l.replace("oneight","1ight")
    l = l.replace("twone","2ne")
    l = l.replace("fiveight","5ight")
    l = l.replace("sevenine","7ine")
    l = l.replace("eightwo","8wo")
    l = l.replace("nineight","9ight")

    l = l.replace("one","1")
    l = l.replace("two","2")
    l = l.replace("three","3")
    l = l.replace("five", "5")
    l = l.replace("seven", "7")
    l = l.replace("eight", "8")
    l = l.replace("nine", "9")

    l = l.strip("abcdefghijklmnopqrstuvwxyz")
    first.append(l[0])

# Last digit
for l in lines:
    lstart = l

    l = l.replace("four", "4")
    l = l.replace("six", "6")

    l = l.replace("oneight", "on8")
    l = l.replace("twone", "tw1")
    l = l.replace("fiveight", "fiv8")
    l = l.replace("sevenine", "seve9")
    l = l.replace("eightwo", "eigh2")
    l = l.replace("nineight", "nin8")

    l = l.replace("one", "1")
    l = l.replace("two", "2")
    l = l.replace("three", "3")
    l = l.replace("five", "5")
    l = l.replace("seven", "7")
    l = l.replace("eight", "8")
    l = l.replace("nine", "9")

    l = l.strip("abcdefghijklmnopqrstuvwxyz")
    last.append(l[-1])

for l in range(0, len(first)):
    running_sum+=int(first[l] + last[l])

print(running_sum)