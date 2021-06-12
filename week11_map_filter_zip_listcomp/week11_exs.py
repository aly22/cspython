# 1


things = [3, 5, -4, 7]

accum = []
for thing in things:
    accum.append(thing+1)
print(accum)

test=list(map(lambda x:x+1,things))

# 2


def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    lst=[]
    for i in strings:
        lst.append(len(i))
    return lst

#3
def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
     of strings in the input list. Use map!"""
    # fill in this function's definition to make the test pass.
    return list(map(lambda x:len(x),strings))

#4

def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use a list comprehension!"""
    # fill in this function's definition to make the test pass.
    return [len(word)for word in strings]


#5

things = [3, 5, -4, 7]
def positives_Acc(lst):
    lst2=[]
    for num in lst:
        if num >0:
            lst2.append(num)
    return lst2
#6

things = [3, 5, -4, 7]
def positives_Fil(lst):
    return list(filter(lambda x: x>0,lst))
#7

things = [3, 5, -4, 7]
def positives_Li_Com(lst):
    return [num for num in lst if num>0]
#8

def longwords(strings):
    """Return a shorter
    list of strings containing only the strings with more than four characters. Use manual accumulation."""
    # write your code here
    shorter_lst=[]
    for i in strings:
        if len(i)>4:
            shorter_lst.append(i)

    return shorter_lst
#9

def longwords_Fil(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use the filter function."""
    # write your code here
    return list(filter(lambda x:len(x)>4,strings))

#10

def longwords_Li_Comp(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use a list comprehension."""
    # write your code here
    return [string for string in strings if len(string)>4]


#11

def longlengths(strings):
    return [i for i in strings if len(i)>=4]
#12

def longlengths(strings):
    return list(filter(lambda x:x>=4,strings))
#13


def sumSquares(L):
    ss=0
    for i in L:
        ss+=i**2
    return ss

nums = [3, 2, 2, -1, 1]


#14

def sumSquares(L):
    return sum(list(map(lambda x:(x*x),L)))

nums = [3, 2, 2, -1, 1]


#15

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

tups = zip(L1,L2,L3)


#16

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

maxs = [max(col) for col in zip(L1,L2,L3)]

#17

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri_sample=[d['name'] for d in tester['info'] if d['class standing']=='Junior']

#18


def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]
result2=[ word for lst in L for word in lst]
print(onelist(L))
#19
tester = {'info': [
    {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
    {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
    {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
    {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
    {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
    {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}


class_sched=[imp for d in tester['info'] for imp in d['important classes']]

#20

nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]
threes=[num for lst in nums for num in lst if num%3==0]
