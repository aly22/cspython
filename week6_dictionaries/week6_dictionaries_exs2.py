# 1

d = {'apples': 15, 'grapes': 12, 'bananas': 35}
#print(d['banana']) #runtime error
d['oranges'] = 20  #add an oranges key-value pair to the dict the value is 20
print(len(d)) #print the ength: 4
print('grapes' in d) #true
#print(d['pears']) #runtime error
print(d.get('pears', 0))# print 0
fruits = d.keys()#an object
print(fruits) #print a list of the keys
del d['apples'] #delete apples
print('apples' in d) # flase

#2

path="eng2pirate.txt"
lines=[]
eng2pirate={}
with open(path,"r",encoding="utf-8") as file:

    for row in file.readlines():
        lines.append(row.strip())
    lines=tuple(lines)

    for idx in range(0,len(lines)-1,2):
        eng2pirate[lines[idx]]=lines[idx+1]
print("eng2pirate =",eng2pirate)
stri=input("Enter a sentence and I will try to translate it into pirate: ")

inpt_lst=stri.split()
pirate=''
for word in inpt_lst:
    if word in eng2pirate:
        pirate+=eng2pirate[word]+' '
    else:
        pirate+=word + " "

pirate=pirate[:-1]
newpirate=pirate+'.'
print(newpirate)
