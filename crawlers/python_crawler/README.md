# Reddit Crawler + Telegram Bot

Routines for scrapping a Reddit page with one interest topic or a list of topics. Returns posts of the first page with 5000+ likes about a specific topic. Also includes a Telegram bot server to interact with user and send the list of hot posts at that moment.

## Install package

Open terminal and type:

```python

sudo python3 setup.py install

```

## start_scrapper.py

Inputs:
1. -topics or list of topics
    String: topic or list of topics to search divided by comma 

Returns:
	Saves a file with the hot topics at that moment

### How to use


Call: python3 run_scrapper.py -t [topics to search]

Open terminal and type:

```python

python3 run_scrapper.py -t cats

python3 run_scrapper.py -t askreddit,worldnews,cats

```

## run_bot.py

Inputs:
1. -bot token 
    String: token of the bot to start

### How to use

Call: python3 run_bot.py -t [bot token]

Go to **src** directory. Open terminal and type:

```python

python3 run_scrapper.py -t your_telegram_bot_unique_token_here

```

## Running tests

Go to **tests** folder. Open terminal and type:

```python

pytest tests.py

```

