# 1
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
score_lst = scores.split()
a_scores = 0
for score in score_lst:
    if float(score) >= 90.0:
        a_scores += 1
# 2
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
# first I need to filter out the words in the stopwords from the string
wrd_lst = org.split()
for wrd in wrd_lst:
    if wrd in stopwords:
        wrd_lst.remove(wrd)

# then I want to iterate through each word and make it an acronym with upper
acro = ""
for word in wrd_lst:
    acro += word[0].upper()
# 3
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
# first I need to filter out the words in the stopwords from the string
wrd_lst = sent.split()
for wrd in wrd_lst:
    if wrd in stopwords:
        wrd_lst.remove(wrd)

# then I want to iterate through each word and make it an acronym with upper
acro = ""
for word in wrd_lst:
    acronym = word[0:2] + '. '
    acro = acro + acronym.upper()
acro = acro[:-2]

# 4

p_phrase = "was it a car or a cat I saw"
# I need to loop through the phrase and add each character to the place before it
r_phrase = ""
for c in p_phrase:
    r_phrase = c + r_phrase

# r_phrase=''.join()
# print(r_phrase)
# 5
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
# for elem in range(len(inventory)):
#     for i in range(3):############################################################################################################################################################################
#         inventory[i]=
# inventory[1]="The store has "+inventory[1]
inventory_str=', '.join(inventory)
inventory_lst=inventory_str.split(', ')
for i in range(0,len(inventory_lst)-1,3):
    print("The store has {} {}, each for {} USD.".format(inventory_lst[i+1],inventory_lst[i],inventory_lst[i+2]))