# 1

def g(x, y=4, z=0):
    return 2 * x + y + z


print(g(3))  # should output 10
print(g(3, 2))  # should output 8
print(g(3, 2, 1))  # should output 9

# 2


def nums(n,mult_int=5,switch=False):
    if switch:
        return -(n*mult_int)
    return n*mult_int

# 3

def together(num,str1,str2=' '):
    str2=str(num)+str2+str1
    return str2
