def hexASCII():
    for i in range(ord('a'), ord('z')+1):
        print("{} : {:x} ".format(chr(i),i), end='')
        if chr(i) == 'm' :
            print()

hexASCII()