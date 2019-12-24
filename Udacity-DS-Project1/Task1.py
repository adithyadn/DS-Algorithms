"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from functools import reduce
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    flatten_texts_list = reduce(lambda z, y: z + y, list(map(lambda lst: lst[:2], texts)))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    flatten_calls_list = reduce(lambda z, y: z + y, list(map(lambda lst: lst[:2], calls)))

    teleList = set(flatten_calls_list + flatten_texts_list)

    print('There are ' + str(len(teleList)) + ' different telephone numbers in the records.')


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
