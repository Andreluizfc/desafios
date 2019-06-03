"""@package scrapper
Scrapper reddit page routines

##
# Created by Andre Castro on 28/05/19
##


"""

from bs4 import BeautifulSoup as bs
import os, sys 
import requests
import re

def search_topic(search_topic):


	"""
    	Search a specific topic in the reddit page

	Parameters
	----------
	search_topic : string
		topic to search

	Returns
	-------
	content : string
		relevant content about the search topic
	"""
	
	# Sets the urls to scrape
	default_url = 'https://old.reddit.com'
	search_url = default_url+'/r/'+search_topic

	# Variables
	upvotes = 0
	subreddit = ''
	title = ''
	link = ''
	coments_link = ''
	content = ''

	# Get reddit page content through a request using a custom User Agent
	page = requests.get(search_url, headers={'User-agent': 'reddit_bot'})
	# Use BeautifulSoup to parse page content to html
	soup = bs(page.text, 'html.parser')

	# Get body of the page, where is defined by class named 'sitetable linklisting'
	body = soup.find(class_='sitetable linklisting')
	
	# Inside the body there are the posts
	# Topics are inside html divs  
	# Get each post inside the div that containt the text 'thing_t3'
	posts = body.find_all('div', id=re.compile('thing_t3'))

	# For each post retrieved
	for post in posts:	
		# Get hot posts. Score should be above 5000 likes!
		if int(post.get('data-score')) < 5000:
			continue
		else:
			# Inside the post div search for information
			title = post.find_next('a', class_='title may-blank ')
			upvotes = post.get('data-score')
			subreddit = post.get('data-subreddit-prefixed')
			link = post.get('data-url')
			coments_link = default_url+post.get('data-permalink')

			# Feed content
			content += 'Title     : '+title.text+'\n'
			content += 'Upvotes   : '+upvotes+'\n'
			content += 'Subrredit : '+subreddit+'\n'
			content += 'Link      : '+link+'\n'
			content += "Comments  : "+coments_link+'\n'
			content += '________________\n\n'

	# If not hot topics, content is empty
	if content == '':
		content = '\n\nNo hot contents right now about {} =(\n\n'.format(search_topic)

	# Return text with all the hot topics details
	return content
