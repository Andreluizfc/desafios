"""@package bot
Telegram bot routines.

##
# Created by Andre Castro on 30/05/19
##


"""

# Imports

from src import scrapper
import requests
import json


def get_updates(bot_token):
    """
    Get content in bot messages API

    Parameters
    ----------
    bot_token : string
        telegram bot token

    Returns
    -------
    content : dict
    	all the content in bot messages API 
    """

	link = 'https://api.telegram.org/bot{}/getUpdates'.format(bot_token)
	
	# Get Telegram API page content through a request
	response = requests.get(link)
	# Parse content to utf8 style
	content = response.content.decode("utf8")
	content = content_to_dict_format(content)
	return content

def content_to_dict_format(content):
    """
    Parse content of the API page to dictionaty format

    Parameters
    ----------
    content : string
        content to parse to dictionary format

    Returns
    -------
    content_as_dict : dict
    	content in dictionaty format
    """

	content_as_dict = json.loads(content)
	return content_as_dict

def get_last_update(bot_token):
    """
    Get the last message sent to bot and who sent it

    Parameters
    ----------
    bot_token : string
        telegram bot token

    Returns
    -------
    user_id,message : tuple
    	user id and message sent to bot 
    """

    # Get all messages
	updates = get_updates(bot_token)
	# Get the number of messagens
	num_updates = len(updates["result"])
	
	# Variables
	user_id = ''
	message = ''
	
	# If last message sent to bot is 'message' or 'edited_message' type
	if 'message' or 'edited_message' in updates['result'][num_updates-1]:
		try:
			user_id = updates['result'][num_updates-1]['message']['chat']['id']
			message = updates['result'][num_updates-1]['message']['text']
		except:
			user_id = updates['result'][num_updates-1]['edited_message']['chat']['id']
			message = updates['result'][num_updates-1]['edited_message']['text']
	# Message is not a processable format. Is either audio, video, document or other content
	else:
		user_id = 'null'
		message = 'null'

	# Return tuple containing who sent the message and the message
	return(user_id, message)

def send_message(user_id, text, bot_token):
    """
    Bot send a message to some user

    Parameters
    ----------
    text : string
    	message to send
    user_id: string
		the user to send the message
    bot_token : string
        telegram bot token
    """

	link = 'https://api.telegram.org/bot{}/sendMessage?text={}&chat_id={}'.format(bot_token,text, user_id)
	# Try to make a request to the send message API 
	try:
		requests.get(link)
		return True
	except requests.exceptions.RequestException as e:
		print('\n\n Request Error: {}'.format(e))
		return False

def handle_user_message(message):
    """
    Handle message sent by user to bot

    Parameters
    ----------
    message : string
    	message to treat

    Returns
    -------
    reply : string
    	reply to the user
    """

	reply = ''
	
	# If user message has '/Trending'
	if '/Trending' in message:

		# Split the message into words separated by blank space
		message = message.split(' ')
		# Try to get the topics to search
		try:
			topics = message[1].split(',')
			# For each topic inside the message topics
			for topic in topics:
				# Use scrapper in the reddit page about the topic
				# Return text with all the hot topics details
				result = scrapper.search_topic(topic)
				# Increment reply
				reply += result
		# If message could not be treated
		except:
			reply = 'Sorry. Try again 😢'
	
	# Else user message is not processable
	else:
		reply = 'Hello! Want to get 🔥HOT🔥 topics on reddit? \n\n Try to type /Trending topic_to_search \n\n Example: /Trending cats \
				\n\n Or maybe you want to get a list of trending topics ?? \n\n Just type /Trending topic1,topic2,topic3 \n\n Enjoy 😄'
	
	return reply
