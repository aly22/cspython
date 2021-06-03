# 1

d = {'apples': 15, 'grapes': 12, 'bananas': 35}
# print(d['banana']) #runtime error
d['oranges'] = 20  # add an oranges key-value pair to the dict the value is 20
print(len(d))  # print the ength: 4
print('grapes' in d)  # true
# print(d['pears']) #runtime error
print(d.get('pears', 0))  # print 0
fruits = d.keys()  # an object
print(fruits)  # print a list of the keys
del d['apples']  # delete apples
print('apples' in d)  # flase

# 2

path = "eng2pirate.txt"
lines = []
eng2pirate = {}
with open(path, "r", encoding="utf-8") as file:
    for row in file.readlines():
        lines.append(row.strip())
    lines = tuple(lines)

    for idx in range(0, len(lines) - 1, 2):
        eng2pirate[lines[idx]] = lines[idx + 1]
print("eng2pirate =", eng2pirate)
# stri=input("Enter a sentence and I will try to translate it into pirate: ")
stri = "the "
inpt_lst = stri.split()
pirate = ''
for word in inpt_lst:
    if word in eng2pirate:
        pirate += eng2pirate[word] + ' '
    else:
        pirate += word + " "

pirate = pirate[:-1]
newpirate = pirate + '.'
print(newpirate)

# 3

with open('scarlet3.txt', 'r') as f:
    words = []
    for row in f:
        words.append(row.strip().split())
    word_dic = {}
    for lst in words:
        for word in lst:
            if len(word) == 7:
                if word not in word_dic:
                    word_dic[word] = 0
                word_dic[word] += 1
    most_used_7_letter = list(word_dic.keys())[0]
    for k in word_dic:
        if word_dic[k] > word_dic[most_used_7_letter]:
            most_used_7_letter = k
    print("The most used 7 letter word was: {} with {} usages".format(most_used_7_letter, word_dic[most_used_7_letter]))
# 4

import string

# first I need the lowercase alphabet
alphabet = list(string.ascii_lowercase)

# then I need an input
sentence = "ThE MightY HoRde EntEreD The cAstLe HunTing ThE kING'S hEAD"  # (input("Enter a random sentence: "))
sentence = sentence.lower()
word_dic = {}
for c in sentence:
    if c in alphabet:
        if c in word_dic:
            # c='w' word_dic['w']=1
            word_dic[c] += 1
        else:

            # c="w" word_dic['w']=0
            word_dic[c] = 1


for k, v in sorted(word_dic.items()):
    print(k, v)
