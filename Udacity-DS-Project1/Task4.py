"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def is_tele_marketer(number):
    return number.startswith('140')

assert is_tele_marketer('140111222')

tele_market_outcallers = set()
tele_market_txt_incoming = set()

for call in calls:
    if is_tele_marketer(call[0]):
        tele_market_outcallers.add(call[0])
    if(is_tele_marketer(call[1])):
        tele_market_txt_incoming.add(call[1])

for text in texts:
    if(is_tele_marketer(call[0])):
        tele_market_txt_incoming.add(call[0])
    if(is_tele_marketer(call[1])):
        tele_market_txt_incoming.add(call[1])

tele_market_outcallers_only = tele_market_outcallers.difference(tele_market_txt_incoming)
tele_market_outcallers_only = sorted(tele_market_outcallers_only)

print('These numbers could be telemarketers: ')
for number in tele_market_outcallers_only:
    print(number)