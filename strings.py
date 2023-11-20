'''
    Immutable sequences
'''

print('\none-line strings')
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

# capitalize() - 
print('\ncapitalize()')
print('coMuni cat'.capitalize()) # Comuni cat
print(' coMuni CAt'.capitalize()) #  comuni cat

# center() - 
print('\ncenter()')
print('['+'abc cat'.center(2)+']') # Comuni cat
print('line'.center(10, '*')) #  comuni cat


# endswith(sub) - 
print('\nendswith()')
print('airplane'.endswith('ne')) # True
print('line'.endswith('a')) # False

# startswith() -  
print('\nstartsWith()')
print('airplane'.startswith('ai')) # True
print('line'.startswith('lp')) # False


# find(sub) - 
print('\nfind(sub)')
print('airplane'.find('ne')) # 6
print('line'.find('a')) # -1

# isalnum() - Check if the string contains only digits or alpha chars 
print('\nisalnum()')
print('airplan1e'.isalnum()) # True
print('line$'.isalnum()) # False

# isalpha() - Check if the string only contains letters 
print('\nisalpha()')
print('airplane'.isalpha()) # True
print('line '.isalpha()) # False
print('line1'.isalpha()) # False

# isdigit() - Check if the string contains only digits
print('\nisdigit()')
print('123'.isdigit()) # True
print('241 '.isdigit()) # False
print('34a'.isdigit()) # False


# islower() - Check if the string contains only lower-case letters only
print('\nislower()')
print('123'.islower()) # False
print('abc'.islower()) # True
print('abc '.islower()) # True
print('AbG'.islower()) # False

# isupper() - Check if the string contains only upper-case letters only
print('\nisupper()')
print('123'.isupper()) # False
print('ABC'.isupper()) # True
print('ABC '.isupper()) # True
print('AbG'.isupper()) # False

# isspace() - 
print('\nisspace()')
print(' \n'.isspace()) # True
print('ABC '.isspace()) # False
print(' '.isspace()) # True
print('1 '.isspace()) # False

# join(list) - 
print('\njoin()')
print(",".join(["omicron", "pi", "rho"])) # omicron,pi,rho


# lower() - convert to lower case
print('\nlower()')
print('ABc'.lower()) # abc
print('abC 1'.lower()) # abc 1

# upper() - convert to upper case
print('\nupper()')
print('ABc'.upper()) # ABC
print('abC 1'.upper()) # ABC 1


# lstrip() - remove leading white space chars
print('\nlstrip()')
print(' ABc'.lstrip()) # ABc
print('abC 1'.lstrip('a')) # bC 1


# rstrip() - remove trailing white space chars
print('\nrstrip()')
print('ABc '.rstrip()) # ABc
print('abC 1'.lstrip('1')) # bC 1 ???
print("cisco.com".rstrip(".com")) # cis


# strip() - remove leading and trailing white space chars
print('\nstrip()')
print(' ABc '.strip()) # ABc
print('abC '.strip()) # abC 
 

# replace() - replace a subtring with other
print('\nreplace()')
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # www.pythoninstitute.org
print("This is it!".replace("is", "are")) #thare are it
print("Apple juice juice juice".replace("juice", "suco", 2)) # Apple suco suco juice
print("Apple juice".replace("juice", "")) # Apple

# rfind(sub, start, end) - find the position of a substring from right to left
print('\nrfind()')
print("tau tau tau".rfind("ta")) # 8
print("tau tau tau".rfind("ta", 9)) # -1
print("tau tau tau".rfind("ta", 3, 9)) # 4


# swapcase() - swaps lower case characters to upper and viceversa 
print('\nswapcase())')
print("HeLlo WorlD!".swapcase()) # hElL0 wORLd!


# title() - upper every initial letter in each word
print('\ntitle()')
print("dEsigniNg DAta intensive applications".title()) # Designing Data Intensive Applications