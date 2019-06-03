import os, sys


from src import file_manager as fm
from src import formatter

import pytest


def test_open_file():
	"""
	Test if can open file
	"""

	# Read file
	file = '../files/input_default.txt'
	text = fm.read_file_to_str(file)
	assert (text) != ''

def test_read_file_null():
	"""
	Test if file is none
	"""

	file = ''
	text = fm.read_file_to_str(file)
	assert (text) == ''

def test_save_file():
	"""
	Test save file
	"""

	text = 'test sample text'
	assert fm.save_str_to_file(text) == True

def test_run_formatter_default_text():
	"""
	Test run formatter on the default text file
	"""

	default_inputfile = '../files/input_default.txt'
	default_limit = 40
	default_justify = False

	# Read file and load to string
	text = fm.read_file_to_str(default_inputfile)
	assert text != ''

	# Run text formatter
	formatted_text = formatter.format_str(text,default_limit,default_justify)
	assert formatted_text is not text

	# Save formatted text to file
	assert fm.save_str_to_file(formatted_text) == True

def test_run_formatter_default_text_and_justify():
	"""
	Test run formatter on the default text file and justify
	"""

	default_inputfile = '../files/input_default.txt'
	default_limit = 40
	default_justify = True

	# Read file and load to string
	text = fm.read_file_to_str(default_inputfile)
	assert text != ''

	# Run text formatter
	formatted_text = formatter.format_str(text,default_limit,default_justify)
	assert formatted_text is not text

	# Save formatted text to file
	assert fm.save_str_to_file(formatted_text) == True
