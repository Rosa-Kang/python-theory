# The get method for dictionaries
# if name in counts:
#     x = counts[name]
# else :
#     x = 0

counts = {'quincy' : 1, 'mrugesh': 42, 'beau':100, '0':10}
print(counts.get('kris',0))

counts = {'chuck' : 1, 'annie':42, 'jan':100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])