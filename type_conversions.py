print('from other types to string: ')
print('  int to string', str(1)) # '1'
print('  float to string', str(1.12)) # '1.12'
print('  bool(True) to string', str(True)) # 'True'
print('  bool(False) to string', str(False)) # 'False'
print('  empty string', str()) # ''


print('\nfrom other types to int: ')
print('  float to int:', int(1.82)) # 1
print('  float to int:', int(.45)) # 0
print('  string to int:', int('8')) # 8
print('  string with spaces to int', int(' 5 ')) # 5 removes the spaces

try:
    print('  string with letter to int')
    int('5a')
except ValueError:
    print('    fails with: ValueError: invalid literal for int() with base 10: 5a')

try:
    print('  string(float) to int')
    int('5.9') # doesnt accept decimal points
except ValueError:
    print('    fails with: ValueError: invalid literal for int() with base 10: 5.9')

print('  bool(True) to int', int(True)) # 1
print('  bool(False) to int', int(False)) # 0


print('\nfrom other types to float: ')
print('  int to float:', float(1298)) # 1298.0
print('  string to float:', float('8.91')) # 8.91
print('  string (int) to float:', float('176')) # 176.0
print('  string to float:', float('.1')) # 0.1
print('  string with spaces to float', float(' 5.21 ')) # 5.21 removes the spaces

try:
    print('  string with letter to float')
    float('5a')
except ValueError:
    print('    fails with: ValueError: could not convert string to float: 5a')

print('  bool(True) to float', float(True)) # 1.0
print('  bool(False) to float', float(False)) # 0.0


print('\nfrom other types to bool: ')
print('  int(positive) to bool:', bool(1)) # True
print('  int(negative) to bool:', bool(-1)) # True
print('  int(zero) to bool:', bool(0)) # False
print('  string to bool:', bool('abc')) # True
print('  string(int) to bool:', bool('1')) # True
print('  string empty to bool:', bool('')) # False
print('  float(positive) to bool:', bool(5.1)) # True
print('  float(zero) to bool:', bool(0.0)) # False
print('  float(negative) to bool:', bool(-1.0)) # True