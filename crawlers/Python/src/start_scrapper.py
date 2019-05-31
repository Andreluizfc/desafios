"""@package crawlers
Main routine for the scrapper scripts.

##
# Created by Andre Castro on 28/05/19
##


"""

# Imports

import 	os, sys 
import	argparse
import  scrapper
import 	file_manager as fm

def main():

	# Arguments parser to handle arguments

	parser = argparse.ArgumentParser()
	parser.add_argument('-topics', default='empty', help='Topics to search divided by collon. Example: cats,dogs,brazil')
	
	# Try to parse args and checks if arguments are empty
	try:
		args = parser.parse_args()
		if args.topics == 'empty':
			parser.print_help()
			sys.exit(0)
	except:
		print('\n\n Argument parser error! Check arguments.\n\n')
		parser.print_help()
		sys.exit(0)

	# Continue if all arguments are ok
	# Get topics in arguments
	topics = str(args.topics).split(',')
	
	# For each topic, scrap reddit page and get results
	for topic in topics:
		result = scrapper.search_topic(topic)
		# save results to file
		fm.append_str_to_file(str(result))
	
	
if __name__ == "__main__":
	main()