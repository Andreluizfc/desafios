# Solving Chalenge 2: Crawlers

# Desafio 2: Crawlers

Find and list the Reddit *threads* that are booming at that moment! We consider bombing *threads* 5000 points or more.

## Input

 - Name of subreddit Ex: cats
 Or
 - List with names of subreddits separated by commas (`,`). Ex: "askreddit,worldnews,cats"

### Part 1

Generate and print a list containing number of upvotes, subreddit, thread title, link to thread comments, thread link.

### Part 2

Build a robot that sends this list to a user via Telegram whenever it receives the command `/Trending [+ List of subrredits]` (ex: `/Trending programming,dogs,brazil`).

## Solving the Challenge

### Part 1

Using **requests** the source code of the first page about a thread was obtained. Using the **BeautifulSoup** we could create a *soup* variable to search the contents of that page. The threads were inside *class_='sitetable linklisting'*. To get all threads the **find_all** operation was used to get the *divs* containing the expression *thing_t3*. For each div, that contained information of one thread, the relevant content were obtained using **find_text** and  **get** operation of **BeautifulSoup**. 

### Part 2 

To create a bot, the user should use the [@BotFather](https://telegram.me/botfather) in the Telegram API and follow the steps to get the unique *bot_id*. The [Telegram Bot API](https://core.telegram.org/bots/api) was used to interact with the bot. To start the bot, the code constantly checks if there's a new message sent to the bot. Depending on the message, the code should interpret the text and send the response to the user. 