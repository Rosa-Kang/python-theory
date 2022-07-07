from msilib.schema import File


xfile =open('mbox.txt')
for cheese in xfile:
print(cheese)

# Counting Lines in a File
fhand = open('afile.txt')
count = 0
for line in fhand:
    count = count +1
print('Line Count:', count)

# Reading Whole File
fhand = open('bfile.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Searching Through a File
fhand = open('cfile.txt')
for line in fhand:
    line = line.rstrip() #rstrip removes whitespace
    if not line.startwith('something'):
        continue
    print(line)

fhand = open('cfile.txt')
for line in fhand:
    line = line.rstrip() #rstrip removes whitespace
    if line.startwith('something'):
        print(line)

fname = input('Enter the file name you want to search: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startwith('Subjext:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)