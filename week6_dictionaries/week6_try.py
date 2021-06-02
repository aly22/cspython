#f = open('scarlet2.txt', 'r')
txt = "teletext"
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = {}
for y in x:
    if y in letter_values:
        tot[y]=0

    tot[y]+=letter_values[y] * x[y]

print(tot)


d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
best_key_so_far=list(d.keys())[0]
for k in ks:
    if d[k]>=d[best_key_so_far]:
        best_key_so_far=k
# check if the value associated with the current key is
# bigger than the value associated with the best_key_so_far
# if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for c in placement:
    if c not in d:
        d[c]=0
    d[c]+=1
min_value=list(d.keys())[0]
for k in d:
    if d[k]<d[min_value]:
        min_value=k

product = "iphone and android phones"
lett_d={}
for c in product:
    if c not in lett_d:
        lett_d[c]=0

    lett_d[c]+=1

max_value=list(lett_d.keys())[0]
for k in lett_d:
    if lett_d[k]>lett_d[max_value]:
        max_value=k