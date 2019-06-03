import os, sys


from src import scrapper
from src import bot

import pytest


def test_run_scrapper():
	"""
	Test if can run the scrapper
	"""

	# Read file
	
	topic = 'cats'
	result = scrapper.search_topic(topic)

	assert (result) != ''

def test_bot_get_updates():
	"""
	Test if can get the bot updates

	WARNING: This test fails unless you add your bot token below
	"""

	bot_token = ''
	content = bot.get_updates(bot_token)
	assert (content) != ''

def test_bot_get_last_update():
	"""
	Test if can get the bot last update

	WARNING: This test fails unless you add your bot token below
	"""

	bot_token = ''
	user_id, message = bot.get_last_update(bot_token)
	assert (user_id, message) != [None,None]

def test_bot_send_message():
	"""
	Test if the bot can send a message

	WARNING: This test fails unless you add your bot token below
	"""
	bot_token = ''
	text = 'Hello, this is a test message! Regards, Skynet!'	
	user_id, message = bot.get_last_update(bot_token)

	result = bot.send_message(user_id, text, bot_token)
	assert (result) == True

def test_bot_handle_user_message():
	"""
	Test if the bot handles a message sent by the user

	WARNING: This test fails unless you add your bot token below
	"""

	message = 'Any message sent to bot.'
	reply = bot.handle_user_message(message)
	assert (reply) != ''
