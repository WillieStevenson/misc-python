#
# Author: Willie Stevenson
# Date 01/24/2016

# This is a function called deepListReverse.
# It reverses all lists in the input list.
#
# @param list1; list; a list with elemenets;
# @restrictions @param must be of type list;
# @return list; the input list reversed;
#
# To Do:
#
# Write better cases for recursive use

def deepListReverse(list1):
	if isinstance(list1, list):
	    if len(list1) == 0:
	    	return list1;
	    else:
	    	if isinstance(list1[0], list):
	    		temp = deepListReverse(list1[0])
	    	else:
	    		temp = list1[0]
	    	return deepListReverse(list1[1:]) + [temp]
	else:
		return "wrong data type encountered"


# Test runs
print("---------------------------")
print deepListReverse((1,2))
print("---------------------------")
print deepListReverse([1,[2,[4,5]],3])
print("---------------------------")
print deepListReverse([1,2,3])
print("---------------------------")
print deepListReverse([2,[3,2],1,[3,[9,0,1]]])
print("---------------------------")
