
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
def pokemon1(dic):
    p_names=[]
    p_number=[]
    for k,v in dic.items():
        p_names.append(k)
        p_number.append(v)
    return [p_names,p_number]

p_names, p_number=pokemon1(pokemon)
print(pokemon1(pokemon))
print(p_names)
print(p_number)


track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
def track_medals(dic):
    track_events=[]
    for e,v in dic.items():
        track_events.append(e)
    return track_events

track_events=track_medals(track_medal_counts)

#2

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

people = [julia, claude, alan]
# def persons(lst):
#     lname,yob,cty=[],[],[]
#     for itm in lst:
#         lname.append(itm[1])
#         yob.append(itm[2])
#         cty.append(itm[-1])
#     return lname,yob,cty
# lname,yob,cty=persons(people)
# for i in (persons(people)):
#     pass

for person in people:
    print(f"The Person's last name is: {person[1]} the year of birth is: {person[2]} and their city: is {person[-1]}")