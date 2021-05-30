# 1
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
for i in range(len(verbs)):
    verbs[i] += "ing"
# 2
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103",
           "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
lower = []
upper = []
class_str = " ".join(classes)
class_lst = class_str.split(' ')

for i in range(0, len(class_lst) - 1, 2):
    if (class_lst[i] == "MATH" and int(class_lst[i + 1]) >= 300) or \
            (class_lst[i] == "ENG" and int(class_lst[i + 1]) >= 200) or \
            (class_lst[i] == "PSYCH" and int(class_lst[i + 1]) >= 400):
        upper.append(class_lst[i] + ' ' + class_lst[i + 1])
    else:
        lower.append(class_lst[i] + ' ' + class_lst[i + 1])

# 3
myList = [76, 92.3, 'hello', True, 4, 76]

# Your code here
myList.append('apple')
myList.append(76)
myList.insert(2,"cat")
myList.insert(0,99)
myList.index('hello')
myList.count(76)
myList.remove(76)
popped=myList.pop(4)

#4


test = ["else", "integer", "except", "elif"]
keyword_test = []

import keyword

for word in test:
    keyword_test.append(keyword.iskeyword(word))

#5


chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']

import string

nums=string.digits
is_num=[]
for c in chars:
    if c in nums:
        is_num.append((c, True))
    else:
        is_num.append((c, False))
print(is_num)