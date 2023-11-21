s1 = '12.8' #ValueError: invalid literal for int() with base 10: '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)