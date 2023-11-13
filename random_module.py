from random import random, seed, randrange, randint, choice, sample

##seed(1)

for _ in range(5):
    print(random())


print('\nrandrange()')
# randrange(start, stop, step) -> int. stop not inclusive
print( randrange(3) ) # 0 - 2
print( randrange(3) ) # 0 - 2
print( randrange(3) ) # 0 - 2
print( randrange(1, 10) ) # 1 - 10
print( randrange(1, 10, 1) ) #

print('\nrandint()')
# randint(a, b) -> int. b inclusive
print( randint(1, 5) )


print('\nchoice()')
ls = [5, 9, 1]
# choose a random element from a non-empty sequence
print(choice(ls))
print(choice(ls))

#my results looked like this
print('\nsample()')
# chooses k unique random elements from a population sequence
print(sample(ls, 2))
print(sample(ls, 3))

st = ('a', '9', 'l', 'p', 'x', 'h')
print(sample(st, 3))

print(sample('watch', 2))

