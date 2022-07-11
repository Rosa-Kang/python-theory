# Tuples are like lists
# Tuples are another kind of sequences that functions much like a list - they have elements which are indexed starting at 0
# *diff : there is no square brakets / just use parenthesis
        # : they are immutable **
        # higher performance, better memory
# Tuples are Comparable
# Only scans until it has a definitive answer

# t = list()
# print(dir(t))

# z= tuple()
# print(dir(z))

# # lists are mutable
# x = [9,8,7]
# x[2] = 6
# print(x) #[9,8,6]

# y = (5,4,3)
# y[2] = 6 # TypeError: 'tuple' object does not support item assignment

# z= 'ABDC'
# z[2] = 'D'#  TypeError: 'str' object does not support item assignment

# we can also put a tuple on the left-hand side of an assignment Statement
# We can even omit the the parenthesis

# d = dict()
# d['csev'] = 2
# d['chen'] = 4
# for (k,v) in d.items():
#     print(k,v)

# tups = d.items()
# print(tups)

# d = {'c':20, 'a':10, 'b':1 }
# t = sorted(d.items())
# print(t)

# c =  {'c':20, 'a':10, 'b':1 }
# tmp = list()
# for k, v in sorted(c.items()) :
#     tmp.append((v,k))
#     tmp = sorted(tmp, reverse=True)
# print(tmp)

# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) +1

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)
# for val, key in lst[:10] :
#     print(key, val)

l = {'a':10, 'b':1, 'c':22}

print(sorted( [(v,k) for k, v in l.items()] ))