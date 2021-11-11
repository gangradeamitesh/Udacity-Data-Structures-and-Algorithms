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

outgoing_calls = set([call[0] for call in calls])
incoming_calls = set([call[1] for call in calls])

outgoing_texts = set([text[0] for text in texts])
incoming_texts = set([text[1] for text in texts])

possible_telemarkets = []

for phone in outgoing_calls:
    if (phone not in outgoing_texts) and (phone not in incoming_texts) and (phone not in incoming_calls):
        possible_telemarkets.append(phone)
print("These numbers could be telemarketers:")
for possible_telemarket in sorted(possible_telemarkets):
    print(possible_telemarket)