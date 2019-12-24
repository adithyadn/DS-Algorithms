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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_fixed_line(number):
    return number.startswith('(')

def is_mobile(number):
    return number.startswith('7') or number.startswith('8') or number.startswith('9')

def get_prefix(number, startIndex, endIndex):
    return number[startIndex:endIndex]

assert is_fixed_line('(080)12345678')
assert is_mobile('7890123456')
assert get_prefix('(080)12345678', 1, 4) == '080'
assert get_prefix('08012345678', 0, 4) == '0801'
assert get_prefix('14012345678', 0, 3) == '140'

total_banglore_outgoing = 0
banglore_only_calls = 0
outcall_area_codes = set()

for call in calls:
    if is_fixed_line(call[0]) and get_prefix(call[0], 1, 4) == '080':
        total_banglore_outgoing += 1
        if is_fixed_line(call[1]):
            prefix = get_prefix(call[1], 1, 4)
            outcall_area_codes.add(prefix)
            if prefix == '080':
                banglore_only_calls += 1
        elif is_mobile(call[1]):
            outcall_area_codes.add(get_prefix(call[1], 0, 4))
        else:
            outcall_area_codes.add('140')

outcall_area_codes = sorted(outcall_area_codes)
print('The numbers called by people in Bangalore have codes:')
for code in outcall_area_codes:
    print(code)


print('%2.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' %(banglore_only_calls * 100 / total_banglore_outgoing))


