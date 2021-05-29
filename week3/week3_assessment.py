#1
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months=0
rainfall_mi_lst=rainfall_mi.split(',')
for rain in rainfall_mi_lst:
    if float(rain)>3.0:
        num_rainy_months+=1
#2
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
lst=sentence.split()
same_letter_count=0
for word in lst:
    if word[0]==word[-1]:
        same_letter_count+=1
    elif len(word)==1:
        same_letter_count+=1

#3
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for item in items:
    if 'w' in item:
        acc_num+=1

#4
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
lst=sentence.split()
num_a_or_e=0
for word in lst:
    if "e" in word or 'a' in word:
        num_a_or_e+=1

#5
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
# Write your code here.
for c in s:
    if c in vowels:
        num_vowels+=1

