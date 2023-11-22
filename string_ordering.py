
'''
Unicode:
    0 (48), A(65), a (97)
'''

print('unicode a:', ord('a'), 'unicode A:',  ord('A'))
print('unicode 0:', ord('0'))

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2) #ascending order
print(s3) # ['Where', 'are', 'of', 'snows', 'the', 'yesteryear?']
print(s3[1]) # are