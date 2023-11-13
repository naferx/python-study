
# Built-in functions
# References: 
# ASCII table - https://www.ascii-code.com 


# min() - finds the minimum element in an iterable
print('\nmin(iter)')
my_str = 'pencil'
ls_int = [9, 2, 1, 5]
ls_str = ['b', 'd', 'A', 'o']

print( min(my_str) ) # c - finds the character with the minimal codepoint
print( min(ls_int) ) # 1
print( min(ls_str) ) # A, 0-9 < A-Z < a-z ??? - refer to the ASCII table


# max() - finds the maximum element in an iterable
print('\nmax(iter)')
my_str = 'computer'
ls_int = [9, 2, 1, 5]
ls_str = ['b', 'd', 'A', 'o']
tup_int = (4, 8, 2)
set_int = {3, 5, 1}
dct_int = {1: 'a', 3: 't', 6: 'r'}

print( max(ls_int) ) # 9
print( max(ls_str) ) # 0, 0-9 < A-Z < a-z ???
print( max(tup_int) ) # 8
print( max(set_int) ) # 5
print( max(dct_int) ) # 6. uses the dict keys
#print( max({}) ) # ValueError: max() arg is an empty sequence
print( max(my_str) ) # u - finds the character with the maximal codepoint


# len(collection) - returns the length of a container
