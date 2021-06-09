states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}


def cityname(state):
    print("states dic", states)
    print("state:", state)
    print("First city", states[state][0])
    print("first cities length (charcters):", len(states[state][0]))
    print("first two cities", states[state][0:2])
    return len(states[state][0])


print(sorted(states, key=cityname))
## its the same as saying

print(sorted(states, key=lambda x: len(states[x][0])))


# I can do this because  states gets passed in int the anonymous fuunction then it returns  each states, first cities length
def a_second_letter(cities_lst):
    cnt = 0
    for city in cities_lst:
        if city[1] == 'a':
            cnt += 1
    return cnt


LST = sorted(states, key=lambda x: a_second_letter(states[x]))

print(LST)
# for k in LST:
    # print(f"state {k}, occurrence of 'a's as the second letter of the city name {states[k]}")
# in conclusion you should fill in a NEW tuple, dictionary or a list first with the
# "answers to the sorting algorithm" before
# writing any sorting code, because it will be much easier to think through
# the process and print (get) the answers
# todo : write an example of this
