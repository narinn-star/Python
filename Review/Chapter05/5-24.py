def case(s):
    if s[0] >= 'A' and s[0] <='Z':
        print('capitalized')
    elif s[0] >= 'a' and s[0] <= 'z':
        print('not capitalized')
    else:
        print('unknown')

case('Android')
case('apple')
case('3M')