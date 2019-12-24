"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    maxTime = 0
    teleNum = None
    for call in calls:
        if int(maxTime) < int(call[-1]):
            maxTime = call[-1]
            teleNum = call[0]

    print(str(teleNum) + ' spent the longest time, ' + str(maxTime) + ' seconds, on the phone during September 2016.')


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

