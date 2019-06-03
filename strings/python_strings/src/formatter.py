"""
Text formatter utils.

##
# Created by Andre Castro on 27/05/19
##

"""

import sys, textwrap



def format_str_wrapper(text,limit):
	"""
    Format text to specified parameters

    # Not used in this project
	# This could be another altenative to avoid the function format_str():
	# TODO: Improve to detect break line characters in text \n

    Parameters
    ----------
    text : string
        text to format
    limit : int
    	line limit

    Returns
    -------
    formatted_text : string
    	text formatted with parameters
    """

	formatted_text = ''

	# Creates a text wrapper to deal with the formatting
	wrapper = textwrap.TextWrapper(width = limit)
	wrap_list = wrapper.wrap(text=text)

	for i in wrap_list:
		i =  align_line(i,limit)
		formatted_text = formatted_text + i + '\n'

	return formatted_text
	 

def format_str(text,limit,justify):
	"""
    Format text to specified parameters

    Parameters
    ----------
    text : string
        text to format
    limit : int
    	line limit
    justify : bool
    	justify text if true

    Returns
    -------
    formatted_text : string
    	text formatted with parameters
    """

	word = ''
	line = ''
	formatted_text = ''

	# run through the characters in text
	for pos,char in enumerate(str(text)):
		
		# create word adding one char at time
		if char != ' ' and char != '\n': 
			word += char
		
		# has reached the end of a word
		if char == ' ' or char == '\n':						
			# if line is empty add word 
			if line == '':
				line = word
				word = ''
			# else line has content
			# add word to line if line + word <= limit
			elif len(line) + len(word) <= limit - len(char):
				line += ' ' + word
				word = ''
			
			# if line is full
			# add line to formatted text
			if len(line) + len(word) > limit - len(char):
				if justify: line = justify_line(line,limit)
				formatted_text += line + '\n'	
				line = word
				word = ''
			
			# if break line
			# add break line to the formatted text
			if char == '\n':
				if justify: line = justify_line(line,limit)
				formatted_text +=  line + '\n'
				line = ''
			
			# if end of text
			# add line to the formatted text
			if pos == len(text)-1:
				if justify: line = justify_line(line,limit)
				formatted_text += line
				line = ''
			
	return formatted_text

def justify_line(line,limit):
	"""
    Justify line text

    Parameters
    ----------
    line : string
        line containing words
    limit : int
    	line limit

    Returns
    -------
    justified_text : string
    	text justified
    """

	justified = ''

	# split line into words
	words = line.split()
	# defines counter as the number of blank spaces to add to line
	counter = limit - items_len(words)
	# while has blank space to add and line not empty
	while counter > 0 and len(words) > 1:
		# for each word in the line
		for i in range(len(words) - 1):
			# add blank space to word in list
			words[i] += ' '
			counter -= 1
			if counter < 1:  
				break

	# join all words in one string
	justified = justified.join(words)

	return justified

def items_len(list):
	"""
    Get total number of characters in a list of words	

    Parameters
    ----------
    list : list
        list containing words

    Returns
    -------
    sum : int
    	number of characters in the list of words
    """
	return sum([ len(x) for x in list] )
