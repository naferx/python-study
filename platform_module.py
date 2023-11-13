from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

#returns a string identifying the underlying platform
print('\nplatform()')
print( platform(aliased=True) ) # Linux-6.2.0-36-generic-x86_64-with-glibc2.35
print( platform(aliased=False) )
print( platform(aliased=True, terse=True))

# return the generic name of the processor
print('\nmachine()')
print( machine()) # x86_64

#returns the real processor's name 
print('\nprocessor()')
print( processor()) # x86_64


#returns the system's/OS name 
print('\nsystem()')
print( system()) # Linux


#returns the system's release version 
print('\nversion()')
print( version()) # #37~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Oct  9 15:34:04 UTC 2

#returns the Python implementation
print('\npython_implementation()')
print( python_implementation() ) # CPython

print('\npython_version_tuple()')
print( python_version_tuple() ) # ('3', '11', '6') major.minor.patch