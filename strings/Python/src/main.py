"""@package string
Main routine to start text formatting

##
# Created by Andre Castro on 27/05/19
##


"""


import os, sys
import file_manager as fm
import formatter


def main(argv):
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

	# Default variables
	default_inputfile = 'input_default.txt'
	default_limit = 40
	default_justify = False

	
	# Get params
	if len(argv) == 0:
		pass
	elif len(argv) == 1:
		default_inputfile = str(argv[0])
	elif len(argv) == 2:
		default_inputfile = str(argv[0])
		try:
			default_limit = int(argv[1])
		except ValueError:
			print("\nERROR: Argument 2 should be ant integer\n")
			sys.exit(0)    
	elif len(argv) == 3:
		default_inputfile = str(argv[0])
		default_limit = int(argv[1])
		if argv[2].lower() == 'true':
			default_justify = True

	# print initial data
	print("\nFile:\n\n",default_inputfile)
	print("\nLine limit: ",default_limit)
	print("\nJustify text: ",default_justify)

	# Read file and load to string
	text = fm.read_file_to_str(default_inputfile)

	# Run text formatter
	formatted_text = formatter.format_str(text,default_limit,default_justify)

	# Save formatted text to file
	fm.save_str_to_file(formatted_text)


if __name__ == "__main__":
	main(sys.argv[1:])


