#!/usr/bin/python

##
#
# Quick and naive way to compare two text files containing 
# unique sets of strings and calculate what percent 
# of the contents of file1 exists in file2
#
#
# Ex.
#
#		$ python percentdiff.py file1.txt file2.txt
#
# Author: Willie Stevenson
#
##


from sys import argv

def readFileToList(filename):
	tmp = open(filename, "r")

	return tmp.readlines()

def statusDisplayFormat(string):
	print "\n[-] " + string + "\n"


file1 = argv[1]
file2 = argv[2]

statusDisplayFormat("Lines per file")

f1 = readFileToList(file1)
f2 = readFileToList(file2)

# Should already be a set anyway! This program takes unique passwords!

set1 = set(f1)
set2 = set(f2)

set1Len = len(set1)
set2Len = len(set2)

print file1 + ": " + str(set1Len)
print file2 + ": " + str(set2Len)

statusDisplayFormat("Starting comparison. This may take a while...")

commonElements = set1.intersection(set2)
numberCommonElements = len(commonElements) 

statusDisplayFormat("String comparison completed.")

print "Number of common strings found: " + str(numberCommonElements)
print "Percent similar: " + str(((numberCommonElements * 1.0)/(set1Len)) * 100) + "%"
print "\n"