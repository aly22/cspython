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
print(r_phrase)
