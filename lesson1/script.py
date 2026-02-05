def sum(a,b):
    return a+b

def devide(a,b):
    if isinstance(a,str) or isinstance(b,str):
        raise ValueError("You can not divide strings!")
    if b!=0:
        return a/b
    else:
        raise ValueError("Divisor can not be zero!")

