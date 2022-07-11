# Regular Expressions
from cgitb import handler
import re

# re.search() like find()

# hanad = open('a.txt')
# for line in hand:
#     line  = line.rstrip()
#     if line.startswith('From: '):
#         print(line)

# for line in hand:
#     line = rstrip()
#     if re.search('^From:', line):
#         print(line)

# y = re.findall('[0,9]+', x)

# Whithout Whitespace : '\S'

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)