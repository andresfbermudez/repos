def sqrt(n):
    if type(n) is str:
        raise TypeError
    if n < 0:
        raise ValueError("You can't use negative numbers")
    
    x = n
    y = 1

    e = .00001
    while(x-y > e):
        x =  (x + y)/2
        y = n / x
    return x
