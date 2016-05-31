#Author: Willie Stevenson
# Date 05/31/2016
#
# This is a function called isPalindrome.
# It accepts a string and returns a boolean.
# True if the string is a palindrome and false otherwise.
# 
#
# @param string; string; a string maybe containing a palindrome;
# @restrictions @param must be of type string;
# @return boolean; true is the string is a palindrome and false otherwise;


import re

def isPalindrome(string):
	if not isinstance(string, str):
		return "Wrong data type."
	string = string.lower() # 
	string = re.sub(r'\W+', '', string) # (matches [^a-zA-Z0-9_] removes everything else)
	
	if len(string) == 0:
		return True # Empty string is considered palindrome
	start = 0
	end = len(string) - 1
    # compare starting from the outside and then go inwards - stop at middle.
	while start < end:
		if string[start] < string[end]:
			return False
		else:
			start = start + 1
			end = end - 1

	return True



# Test runs
print("---------------------------")
print isPalindrome("dad")
print("---------------------------")
print isPalindrome("this is a string.") # not a palindrome
print("---------------------------")
print isPalindrome("I went to japan and did nothing.") # not a palindrome
print("---------------------------")
print isPalindrome("A man, a plan, a canal, Panama!")
print("---------------------------")
print isPalindrome("Not I, no hotel, cycle to Honiton.")
print("---------------------------")
print isPalindrome("Anne, I vote more cars race Rome-to-Vienna.")
print("---------------------------")
print isPalindrome("Mother Eve's noose we soon sever, eh, Tom?")
print("---------------------------")
print isPalindrome("'Sue,' Tom smiles, 'Selim smote us.'")
print("---------------------------")
print isPalindrome("Telegram, Margelet!")
print("---------------------------")
print isPalindrome("Too hot to hoot.")
print("---------------------------")
print isPalindrome("Unglad, I tar a tidal gnu.")
print("---------------------------")
print isPalindrome("Eve damned Eden, mad Eve.")
print("---------------------------")
print isPalindrome("Snug Satraps eye Sparta's guns.")
print("---------------------------")
print isPalindrome("Nurse, save rare vases, run!")
print("---------------------------")
print isPalindrome("Draw, O Caesar, erase a coward.")
print("---------------------------")
print isPalindrome("No mists or frost, Simon.")
print("---------------------------")
print isPalindrome("Sail on, game vassal! Lacy callas save magnolias!")
print("---------------------------")
print isPalindrome("Trap a rat! Stare, piper, at Star apart.")
print("---------------------------")
print isPalindrome("Sue, dice, do, to decide us.")
print("---------------------------")
print isPalindrome("La, Mr. O'Neill, lie normal.")
print("---------------------------")
print isPalindrome("Top step -- Sara's pet spot.")
print("---------------------------")
print isPalindrome("Eel-fodder, stack-cats red do flee.")
print("---------------------------")
print isPalindrome("Reg, no lone car won, now race no longer.")
print("---------------------------")
print isPalindrome("Zeus was deified, saw Suez.")
print("---------------------------")
