# 1) importing the module
import mymodule_test

# 2) import specific functions from module
from math import floor

# 3) import everything from module
from datetime import *

# 4) import with alias
from string import digits as _ds

# 5) import specific functions from module
from math import (
    ceil, pi
)

# prefix the function or variable with the module name
print('prefixing with the module name: ', mymodule_test.NAME)

print('using specific function from module: ', floor(5.3))

print('importing everything: ', datetime.now()) # datetime is a class from the datetime module

print('using alias: ', _ds)

print(__name__)

print('Importing using parentheses multi line. e.g PI: ' + str(pi))