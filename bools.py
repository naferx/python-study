# https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# By default, an object is considered true unless its class defines
# either a __bool__() method that returns False or a __len__() 
# method that returns zero, when called with the object. 1 
# Here are most of the built-in objects considered false:

# constants defined to be false: None and False

# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

# empty sequences and collections: '', (), [], {}, set(), range(0)

b1 = True
b2 = False
b3 = bool(set())
b4 = bool(set([1]))
b5 = bool('abc')
b6 = bool(1)
b7 = bool(0)
b8 = bool(None) # None is similar to null

print(b1) # True
print(b2) # False
print(b3) # False
print(b4) # True
print(b5) # True
print(b6) # True
print(b7) # False
print(b8) # False
print(type(None)) # <class 'NoneType'>
print(bool(0.0)) # False

if not b3: # True
  print('hello')

if b3 or b4 or b5: # True
  print('any of these')

if not '': # not False -> True
  print('is empty')

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # False


x = None

if not x: # not False
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")


def cun() -> bool:
  return True

print(cun()) # True
