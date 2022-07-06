#Comparison Operators


# < . Question Less Than
# <= . Question less than equal
# == . Question:equal to?

#Indent to print "yes" if x=0a and y=10?
# if 0 == x:
#     if y == 10:
#         print('Yes')

x = 5
if x >2 :
    print('Bigger than 2')
    print('Stile bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i>2:
        print('Bigger than 2')
    print('Done with i', i)
print('All done')

# Two Way Decitions
x = 4
if x >2 :
    print('Bigger')
else :
    print('Smaller')

print('All done')

# except block only triggered only when something goes wrong
astr = 'Bob'
try:
    istr = int(astr) #blows up
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

#sample try/ except
rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice work')
else:
    print('Not a number')