# Strings formatting

Routine for text formatting. The code receives a file containing a text, a number N, and a Boolean option to justify the text or not. It formats the present text into the file with lines containing a maximum number N of characters and justifies the text if is set to True.

## Install package

Open terminal and type:

```python

sudo python3 setup.py install

```

## run_formatter.py


Inputs:
1. -path to file
    String: Path to the file to open
2. -max_char 
    Int: Maximum characters per line 
3. -format
    Bool: justify the text if set to **True**

### How to use

```python

python3 run_formatter.py -f [path to file] -l [maximum characters] -f [True or False]

```

Go to **exec** directory. Open terminal and type:


```python

python3 run_formatter.py -f ../files/input_default.txt -l 40 -f True

```

## Running tests

Go to **tests** folder. Open terminal and type:

```python

pytest tests.py

```
