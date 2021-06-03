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
    newstr=theString
    for c in theString:
        if theLetter==c:
            newstr=newstr.replace(c,'')
    return newstr

remove_letter("a",'banana')

def myindex(lst,itm):
    count=0
    for item in lst:

        if item==itm:
            return count
        count+=1
def mycount(lst,itm):
    count=0
    for item in lst:
        if item==itm:
            count+=1
    return count

def myin(lst,itm):
    for item in lst:
        if item==itm:
            return True
    return False

def myreverse(lst):
    return lst[::-1]

def myinsert(lst,position,itm):
    lst[position]=lst[position]+[itm]
    return lst


print(myinsert([1,2,3,4,5,6,5,5],1,2))

def replace(s, old, new):
    