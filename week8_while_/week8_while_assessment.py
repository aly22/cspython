# 1
def sublist(lst):
    newlst = []
    counter = 0
    while counter < len(lst):
        if lst[counter] == 5:
            break
        newlst.append(lst[counter])
        counter += 1
    return newlst


# 2
def checknums(lst):
    newlst = []
    counter = 0
    while counter < len(lst):
        if lst[counter] == 7:
            break
        newlst.append(lst[counter])
        counter += 1
    return newlst


# 3
def sublist(lst):
    newlst = []
    counter = 0
    while counter < len(lst):
        if lst[counter] == "STOP":
            break
        newlst.append(lst[counter])
        counter += 1
    return newlst


# 4
def stop_at_z(lst):
    newlst = []
    counter = 0
    while counter < len(lst):
        if lst[counter] == "z":
            break

        newlst.append(lst[counter])
        counter += 1
    return newlst


# 5
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
count = 0
sum2 = 0
while count < len(lst):
    sum2 += lst[count]
    count += 1


# 6
def beginning(lst):
    counter = 0
    newlst = []
    while lst[counter] != "bye" and counter < 10:
        newlst.append(lst[counter])
        counter += 1
    return newlst
beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night'])