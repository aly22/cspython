# 1
def num_test(num):
    if num > 10:
        return "Greater than 10."
    elif num < 10:
        return "Less than 10."
    else:
        return "Equal to 10."


# 2
def numDigits(n):
    # your code here
    lst = str(n)
    return len(lst)


# 3
def reverse(astring):
    bstring = ''
    for c in astring:
        bstring = c + bstring
    return bstring
    # or an alternative
    # return astring[::-1]


reverse('loltyler1.comdisccodealpha')


# 4
def mirror(mystr):
    # your code here
    return mystr + mystr[::-1]


# 5
def remove_letter(theLetter, theString):
    newstr = theString
    for c in theString:
        if theLetter == c:
            newstr = newstr.replace(c, '')
    return newstr


remove_letter("a", 'banana')


# 6
def myindex(lst, itm):
    count = 0
    for item in lst:

        if item == itm:
            return count
        count += 1


def mycount(lst, itm):
    count = 0
    for item in lst:
        if item == itm:
            count += 1
    return count


def myin(lst, itm):
    for item in lst:
        if item == itm:
            return True
    return False


def myreverse(lst):
    return lst[::-1]


def myinsert(lst, position, itm):
    lst[position] = lst[position] + itm
    return lst


print(myinsert([1, 2, 3, 4, 5, 6, 5, 5], 1, 2))


# 7
def replace(s, old, new):
    st = s.split(old)
    st1 = new.join(st)
    return st1


print("string".split("in"))

# 8
import random


def randmax():
    lst = []
    for _ in range(100):
        lst.append(random.randint(0, 1000))
    max_val = 0
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


print(randmax())


# 9
def sum_of_squares(lst):
    ss = 0
    for num in lst:
        ss = ss + num ** 2
    return ss


# 10
def countOdd(lst):
    count = 0
    for num in lst:
        if num % 2 == 1:
            count += 1

    return count


# 11
def sumEven(lst):
    # your code here
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += num

    return count


# 12

def sumNegatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += num
    return count


# 13

def findHypot(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# 16

def is_rightangled(a, b, c):
    if c == (a ** 2 + b ** 2) ** 0.5:
        return True
    else:
        return False
