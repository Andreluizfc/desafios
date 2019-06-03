"""@package bot
Main routine to start telegram bot.

##
# Created by Andre Castro on 30/05/19
##


"""

# Imports

from src import bot
import sys
import argparse
import time


def main():

	# Arguments parser to handle arguments

	parser = argparse.ArgumentParser()
	parser.add_argument('-token', default='empty', help='Token of the bot to start')
	
	# Try to parse args and checks if arguments are empty
	try:
		args = parser.parse_args()
		if args.bot == 'empty':
			parser.print_help()
			sys.exit(0)
	except:
		print('\n\n Argument parser error! Check arguments.\n\n')
		parser.print_help()
		sys.exit(0)

	# Continue if all arguments are ok
	# Get bot token as input argument
	bot_token = str(args.bot)

	# Get last message sent to bot
	last_update = bot.get_last_update(bot_token)

	# Run in lopp to get responses
	while True:
		# Get last update
		user_id, message = bot.get_last_update(bot_token)

		# If new message not equal 
		if (user_id, message) != last_update:

			reply = bot.handle_user_message(message)
			bot.send_message(user_id, reply, bot_token)			
			last_update = (user_id, message)
			time.sleep(2)
	

if __name__ == '__main__':
	main()
