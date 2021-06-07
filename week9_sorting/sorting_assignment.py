# 1

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters=sorted(letters,reverse=True)

# 2

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted=sorted(animals)

# 3

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical=sorted(medals)

# 4

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three=sorted(medals,key=lambda x:-medals[x])[0:3]

# 5

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed=sorted(groceries, key=lambda x:groceries[x],reverse=True)

# 6

def last_four(x):
    return str(x)[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids=sorted(ids,key=last_four)

# 7

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id=sorted(ids,key=lambda x: str(x)[-4:])

# 8

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort=sorted(ex_lst,key=lambda x:x[1])    