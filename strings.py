'''
    Immutable sequences
'''

print('\none line strings')
name = 'david'
print( len(name) ) # 5
print( name[-1] ) # d

# multiline strings with triple quotes
print('\nmultiline strings')
multi = '''starts here
, end here'''
print( len(multi) ) # 22
print( multi[-1] ) # e


'''
Operations on strings
    - concatenated
    - replicated
'''
print('\noperations on strings')
str1 = 'a'
str2 = 'b'
print(str1 + str2) # ab
print(str2 + str1) # ba
print(3 * str1) # aaa
print(str2 * 2) # bb

print('\ncharacter to code point. ord(str)')
print(ord('a')) # 97
print(ord(' ')) # 32
# print(ord('ab')) # TypeError: ord() expected a character, but string of length 2 found

print('\ncharacter from code point. chr(int)')
print(chr(97)) # a
print(chr(32)) # <space>
print(chr(945)) # α


print('\nIterating over a string')
txt = 'Nos bebemos e falamos'
for c in txt:
    print(c, end = '-') #N-o-s- -b-e-b-e-m-o-s- -e- -f-a-l-a-m-o-s-
print()

# max() - searchs the string from the beginning to find the first element specified
print('\nindex(sub)')
item = 'table'
print(item.index('b')) # 2
print(item.index('le')) # 3
# print(item.index('x')) ValueError: substring not found


# count() - counts the number of ocurrences
print('\ncount(sub)')
food = 'pizza'
print(food.count('z')) # 2
print(food.count('i')) # 1
print(food.count('t')) # 0
