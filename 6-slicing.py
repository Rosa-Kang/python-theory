# S sub 0 through 4 : print(s[0:4]) upto but not including '4'

s= 'Monty Python'
print(s[0:2])
print(s[8:])
print(s[:])

w = 'Hello world'
# print(type(w))
# print(dir(w))

d = 'From therosesomm@gmail.com Sat July 10'
at = d.find('@')
print(at)

end = d.find(' ', at)
print(end)

host = d[at+1 : end]
print(host)

# Using open
handle = open(filename, mode)
fhand = open('filename')