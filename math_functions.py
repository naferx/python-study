from math import ceil, floor, trunc

x = 1.4
y = 2.6
z = 4.0
w = 4.1

# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
print('ceil(x)')
print( ceil(x) ) # 1.4 -> 2 
print( ceil(y) ) # 2.6 -> 3
print( ceil(z) ) # 4.0 -> 4
print( ceil(w) ) # 4.1 -> 5

print('\nceil(-x)')
print( ceil(-x) ) # -1.4 -> -1 
print( ceil(-y) ) # -2.6 -> -2
print( ceil(-z) ) # -4.0 -> -4
print( ceil(-w) ) # -4.1 -> -4


# floor(x) → the floor of x (the largest integer less than or equal to x)
print('\nfloor(x)')
print( floor(x) ) # 1.4 -> 1 
print( floor(y) ) # 2.6 -> 2
print( floor(z) ) # 4.0 -> 4
print( floor(w) ) # 4.1 -> 4

print('\nfloor(-x)')
print( floor(-x) ) # -1.4 -> -2 
print( floor(-y) ) # -2.6 -> -3
print( floor(-z) ) # -4.0 -> -4
print( floor(-w) ) # -4.1 -> -5

# trunc(x) → the value of x truncated to an integer
print('\ntrunc(x)')
print( trunc(x) ) # 1.4 -> 1 
print( trunc(y) ) # 2.6 -> 2
print( trunc(z) ) # 4.0 -> 4
print( trunc(w) ) # 4.1 -> 4

print('\ntrunc(-x)')
print( trunc(-x) ) # -1.4 -> -1 
print( trunc(-y) ) # -2.6 -> -2
print( trunc(-z) ) # -4.0 -> -4
print( trunc(-w) ) # -4.1 -> -4