
largest = None
for thing in [9, 41, 12, 3, 74, 15] :
    if largest is None :
        largest = thing
    elif thing > largest:
        largest = thing
print('The largest number is ', largest)

smallest = None
for thing in [-1, 334, 54,26,2,6,8]:
    if smallest is None :
        smallest = thing
    elif thing < smallest :
        smallest = thing
print('The smallest number in this array is ', smallest)

# Summing in a loop
count = 0
sum = 0
for i in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + i
print('The Average of this array is ', sum / count)
