"""@package string
Main routine to start text formatting

##
# Created by Andre Castro on 27/05/19
##


"""


import os, sys
import argparse
from src import file_manager as fm
from src import formatter


def main():
	"""
	Parameters
    ----------
	argv: list
		list of inputs by user
    
    argv[0] filename : str
    	path of the file
    arvv[1] limit: int
    	limit to format the lines
    argv[2] justify: bool
    	justify text if true
	"""

	# Arguments parser to handle arguments

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', default='../files/input_default.txt', help='File path to open')
	parser.add_argument('-l', default=40, help='Limit of characters per line')
	parser.add_argument('-j', default=False, help='Justify lines: True or False')

	# Try to parse args and checks if arguments are empty
	try:
		args = parser.parse_args()
	except:
		print('\n\n Argument parser error! Check arguments.\n\n')
		parser.print_help()
		sys.exit(0)

	# Continue if all arguments are ok


	default_inputfile = str(args.i)
	default_limit = int(args.l)
	if str(args.j).lower() == 'true':
		default_justify = True
	else:
		default_justify = False


	# print initial data
	print("\nFile:",default_inputfile)
	print("\nLine limit: ",default_limit)
	print("\nJustify text: ",default_justify)

	# Read file and load to string
	text = fm.read_file_to_str(default_inputfile)

	# Run text formatter
	formatted_text = formatter.format_str(text,default_limit,default_justify)

	# Save formatted text to file
	fm.save_str_to_file(formatted_text)


if __name__ == "__main__":
	main()


