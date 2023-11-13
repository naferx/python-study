print('\nSlice in strings')
lang = 'golang'
#  g   o   l   a   n   g 
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

print( lang[:] ) # golang
print( lang[2] ) # l
print( lang[1:] ) # olang
print( lang[2:5] ) # lan
print( lang[:4] ) # gola

print( lang[-3] ) # a
print( lang[-3:] ) # ang
print( lang[-3:-1] ) # an

print( lang[:-1] ) # golan
print( lang[1:-1] ) # olan
print( lang[-5:4] ) # ola

print( lang[::2] ) # gln
print( lang[1::2] ) # oag