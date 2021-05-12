def safeopen(filename, mode):
    try:
        infile = open(filename, mode)
        return infile
    except:
        return None