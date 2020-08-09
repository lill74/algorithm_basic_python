def toIntFromString(str):
    strArr = list(str)
    base = 0
    
    for char in strArr:
        base *= 10
        base += ord(char) - 48
    
    return base

assert toIntFromString('101010') == 101010
