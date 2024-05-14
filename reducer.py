#!/usr/bin/env python
import sys

# Initialize a dictionary to store word counts
word2count = {}

# Read input from stdin
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Parse the input received from the mapper
    word, count = line.split('\t', 1)
    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue  # Skip this line if count is not a valid integer
    # Update the word count in the dictionary
    if word in word2count:
        word2count[word] += count
    else:
        word2count[word] = count

# Output word counts to stdout
# Note: they are unsorted
for word, count in word2count.items():
    print('%s\t%s' % (word, count))
