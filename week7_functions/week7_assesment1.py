# 1

def int_return(n):
    return n


# 2

def add(n):
    n += 2
    return n


# 3

def change(s):
    s += "Nice to meet you!"
    return s


# 4

def accum(lst):
    accum = 0
    for num in lst:
        accum += num

    return accum


# 5
def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"


# 6
def divide(n):
    n /= 2
    return n


def sum(n):
    num = divide(n) + 6
    return num
