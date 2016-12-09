#!/usr/bin/python

##
#
# Logical to physical address translator for page tables
#
# Author: Willie Stevenson
#
##

import sys, math

# pads given binary int string s up to integer bit_count
def zero_padder(s, bit_count):
	char_count = len(s)

	for i in range(bit_count - char_count):
		s = str(0) + s

	return s

# converts decimal number n to binary int string
def decimal_to_binary(n):
	s = ''

	while n > 0:
		s = str(n % 2) + s
		n = n / 2

	return s

# converts binary int string s to a base 10 integer
def binary_to_decimal(s):
	s = s[::-1] # put string backwards for simple manipulation
	summ = 0

	for i in range(len(s)):
		if s[i] == '1':
			summ += int(math.pow(2, i))

	return summ

# import function for loading program files
def import_lists(filename):
	l = []

	with open(filename) as f:
		while True:
			i = f.readline()

			if not i:
				break
			else:
				l.append(int(i))

	return l

# used to display conversions/program steps
def conversion_to_string(a, b, s = ""):
	return (str(a) + " -> " + str(b) + "\t# " + s).expandtabs(34)

# runner
# takes two cli arguments number of pages and page size
# takes two files that define the page table and the logical addresses to translate
def main():
	num_pages = int(sys.argv[1])
	page_size = int(sys.argv[2])
	np = int(math.log(num_pages, 2))
	ps = int(math.log(page_size, 2))

	page_table = import_lists("page_table.txt")
	logical_addresses = import_lists("logical_addresses.txt")

	for i in range(len(logical_addresses)):
		print "---------------------------------------------------------------------------------"
		binary_n = decimal_to_binary(int(logical_addresses[i]))
		binary_n = zero_padder(binary_n, np + ps)
		print conversion_to_string(int(logical_addresses[i]), binary_n, "Convert int to binary int and pad with zeros")
		page_frame_number = binary_n[:np]
		decimal_page_number = binary_to_decimal(page_frame_number)
		print conversion_to_string(page_frame_number, decimal_page_number, "Convert binary int to decimal")
		page_offset = binary_n[np:]

		if decimal_page_number <= len(page_table):
			corr_page_table_entry = page_table[decimal_page_number]
			print conversion_to_string(decimal_page_number, corr_page_table_entry, "Map page table index to physical memory location")
			page_frame_number = zero_padder(decimal_to_binary(corr_page_table_entry), np)
			print conversion_to_string(corr_page_table_entry, page_frame_number, "Convert int to binary int and pad up to page frame number of bits")
			full_binary_physical_address = zero_padder(page_frame_number + page_offset, np + ps)
			print conversion_to_string(full_binary_physical_address, binary_to_decimal(full_binary_physical_address), "Concatenate with offset and convert to decimal")
		else:
			print "Illegal address trap"

	print "---------------------------------------------------------------------------------"

if __name__ == "__main__":
	main()