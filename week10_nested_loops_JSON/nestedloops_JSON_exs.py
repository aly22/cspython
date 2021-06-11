# 1
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
m_list=[]
for lst in d:
    if type(lst) is not list:
        if 'm' in lst:
            m_list.append(lst)
    else:
        for lst2 in lst:
            if type(lst2) is not list:
                if 'm' in lst2:
                    m_list.append(lst2)
            else:
                for lst3 in lst2:
                    if type(lst3) is not list:
                        if 'm' in lst3:
                            m_list.append(lst3)


print(m_list)
# 2
import json
pokemon = {'Trainer1':
               {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
           'Trainer2':
               {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
           'Trainer3':
               {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
           'Trainer4':
               {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}
pokemon2=json.dumps(pokemon, indent=2)
print(pokemon2)
r, d, p=0,0,0
for trainer in pokemon:
    print(pokemon[trainer].keys())
    for element in pokemon[trainer]:

        if 'rattatas' in pokemon[trainer][element]:
            r+=pokemon[trainer][element]['rattatas']
        if 'ditto' in pokemon[trainer][element]:
            d+=pokemon[trainer][element]['ditto']
        if 'pidgey' in pokemon[trainer][element]:
            p+=pokemon[trainer][element]['pidgey']


# 3
big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]
word_counts={}
for outer_lst in big_list:
    # print(outer_lst)
    for inner_lst in outer_lst:
        for word in inner_lst:
            # print(word)
            if word in word_counts:
                word_counts[word]+=1
            else:
                word_counts[word]=1

min_freq=list(word_counts.keys())[0]
for k,v in word_counts.items():
    if v==min(list(word_counts.values())):
        min_freq=k
        break


# 4
import json
pokemon_go_data = {'bentspoon':
                       {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                   'Laurne':
                       {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                   'picklejarlid':
                       {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                   'professoroak':
                       {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}

print(json.dumps(pokemon_go_data,indent=2))

# d={}
#
# for trainer,value in pokemon_go_data.items():
#     d.update(value)
# most_common_pokemon=list(d.keys())[0]
# for k in d:
#     if d[k]>d[most_common_pokemon]:
#         most_common_pokemon=k
most_common_pokemon=''
for trainer in pokemon_go_data:
    for pokemon,val in pokemon_go_data[trainer].items():
        if val==max(list(pokemon_go_data[trainer].values())):
            most_common_pokemon=pokemon