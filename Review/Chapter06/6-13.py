agencies = {'CCC':'Civilian Conservation Corps','FCC':'Federal Communications Commission',
            'FDIC':'Federal Deposit Insurance Corporation', 'SSB':'Social Security Board',
            'WPA':'Works Progress Administration'}

#6-13(a)
plus = {'SEC':'Securities and Exchange Commission'}
agencies.update(plus)
print(agencies)

#6-13(b)
agencies['SSB'] = 'Social Security Administration'
print(agencies)

#6-13(c)
del agencies['CCC']
del agencies['WPA']
print(agencies)