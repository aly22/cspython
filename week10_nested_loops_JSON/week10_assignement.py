# 1
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]


# 2
def test(s, lst, n):
    if s in lst[n]:
        return True
    return False


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = test('yellow', lst, 2)

# Test to see if 4 is in the second list of lst. Save to variable ``four``
four = test(4, lst, 1)

# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = test('orange', lst, 0)


# 3
def test(s, lst):
    if s in lst:
        return True
    return False


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = test('hola', L)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = test([5, 8, 7], L)
# Test if 6.6 is in the third element of list L. Save to variable name test3
if 6.6 in L[2]:
    test3 = True
else:
    test3 = False


# 4
def test(s, lst):
    if s in lst:
        return True
    return False


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum',
                                                                            ['math', 'calculus', 'algebra', 'geometry',
                                                                             'statistics',
                                                                             ['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = test('data', list(nested.keys()))
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = test(24, list(nested.values()))
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = test('whole', list(nested.values()))
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = test("physics", list(nested.keys()))
# 5
import json

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22, 'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29, 'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20, 'Germany': 13}}
print(json.dumps(nested_d, indent=2))
london_gold = nested_d['London']['Great Britain']
# 6
import json

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
          'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'],
          'gymnastics': {'women': ['vault', 'floor', 'uneven bars', 'balance beam'],
                         'men': ['vault', 'parallel bars', 'floor', 'rings']}}
print(json.dumps(sports, indent=2))
# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = [sports["gymnastics"]["men"][0], sports["gymnastics"]["men"][2], sports["gymnastics"]["women"][-2],
      sports["gymnastics"]["women"][-1]]
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][-1]

# 7


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for olympics in nested_d:
    US_count.append(nested_d[olympics]['USA'])

# 8

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third=[]
for i in l_of_l:
    third.append(i[2])
# 9
t=[]
other=[]

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

for lst in athletes:
    for athlete in lst:
        if 't' in athlete:
            t.append(athlete)
        if 't' not in athlete:
            other.append(athlete)
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
lst=str1.split()
#for i in lst:
if "true" in lst:
    output="True! you are you!"
elif "False".lower() in lst:
    output="False. You aren't you?"
else:
    output="Neither true nor false!"