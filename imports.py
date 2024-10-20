# 1) importing the module
import mymodule_test

# 2) import specific functions from module
from math import floor

# 3) import everything from module
from datetime import *

# 4) import with alias
from string import digits as _ds

# prefix the function or variable with the module name
print('prefixing with the module name: ', mymodule_test.NAME)

print('using specific function from module: ', floor(5.3))

print('importing everything: ', datetime.now()) # datetime is a class from the datetime module

print('using alias: ', _ds)

print(__name__)