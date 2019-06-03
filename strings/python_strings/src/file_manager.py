"""
File manager utils.

##
# Created by Andre Castro on 27/05/19
##

"""

import sys

def read_file_to_str(file):
    """
    Read file and load content to string

    Parameters
    ----------
    file : string
        filename
    
    Returns
    -------
    data : string
        string containing file content
    """

    try:
    	with open(file, 'r') as file:
    		data = file.read()
    		return data
    except IOError:
        print("\nERROR: Could not read file - Check file name\n")
        return ''
        sys.exit(0)

def save_str_to_file(text):
    """
    Save formatted text to file

    Parameters
    ----------
    text_formatted : string
        text

    Returns
    -------
    boolean
        True if saved file. False if not saved file.
    """

    try:
        with open('output.txt', 'w') as file:
            file.write(text)
            file.close()
            return True
    except IOError:
        print("\nERROR: Could not save file.\n")
        return False
        sys.exit(0)