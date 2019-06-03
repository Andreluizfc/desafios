# Solving Chalenge 1: Strings

## Challenge Description

### Requirements 

Implement a solution that receives:
1. a generic text
2. a size limit

and generates the outputs of the challenges below:

### Input Example

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`

The text must be parameterizable.

#### Part 1 (Basic) - limit 40 characters

The output file should be like [this file](https://github.com/idwall/desafios/blob/master/strings/output_parte1.txt), where the text has a maximum of 40 characters per line. Words can not be broken in the middle.

#### Part 2 (Intermediary) - limit 40 characters

The output file should be like [this file](https://github.com/idwall/desafios/blob/master/strings/output-parte2.txt), where, in addition to having a maximum of 40 characters per line, the text must be **justified**.

## Solving the Challenge

### Part 1 (Basic)

To deal with texts, first we need to understant the composition of a text. Texts in general can be divided in words, lines and paragraphs. To create a ***uncooked*** solution the input text was loaded to a string and iterated one character by time. Each character was analysed as being a letter, a pontctuation sign or a special character. Words were formed by letters and ponctuation, lines formed by letters, and paragraphs formed by lines. While iterating through the text the size of the current line was constantly checked, if a word to be added in the line would not break the limit of the characters, that word as added to the line. Otherwise, a new line was created. Paragraphs were created by checking the special character of Break Line *\n*.

### Part 2 (Intermediary)

To justify the text, the lines were treated separately. It was created a function to deal with the line justification. This function splits the line into words using the ***str.split*** operation and checks the number o characters of that line by adding the number of characters in all the words. The limit of the blank spaces to add was determined by subtracting the limit and the number of characters in the line. After that a loop was created to add a blank space to each word in the line util the limit was reached. All words were joined again to form a justified line with the ***str.join*** operation.