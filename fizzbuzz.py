
for i in range(10):
    s = ''
    if i%3 == 0:
        s = s + 'fizz'
    if i%5 == 0:
        s = s + 'buzz'
    print str(i) + s

## this isn't really fizzbuzz