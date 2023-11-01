from random import random, seed, randrange, randint

##seed(1)

for _ in range(5):
    print(random())

# randrange(start, stop, step) -> int. stop not inclusive
print( randrange(3) ) # 0 - 2
print( randrange(3) ) # 0 - 2
print( randrange(3) ) # 0 - 2
print( randrange(1, 10) ) # 1 - 10
print( randrange(1, 10, 1) ) #

# randint(a, b) -> int. b inclusive
print( randint(1, 5) )
