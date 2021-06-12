# 1
def add(s):
    s2 = s.replace(s, "Fruit: " + s)
    return s2


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries',
             'peaches', 'apples', 'mangos', 'papaya']
map_testing = list(map(add, lst_check))
# 2

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana',
             'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh',
             'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama',
             'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda x: x[0] == 'B', countries))
# 3

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'),
          ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'),
          ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'),
          ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'),
          ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [fname[1] for fname in people]

# 4

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [lst3 * 2 for lst3 in lst]

# 5

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100),
            ('Raymond', 50), ('Sue', 75)]

passed = [student[0] for student in students if student[1] >= 70]
# 6

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']


def filtery(k):
    print(k)
    return len(k[0]) > 3 and len(k[1]) > 3


# opposites=[(k,v) for k,v in zip(l1,l2) if len(k)>3 and len(v)>3]
opposites = list(filter(filtery, zip(l1, l2)))
print(opposites)
# 7

species = ['golden retriever', 'white tailed deer', 'black rhino',
           'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant',
           'rainbow trout', 'black bear', 'blue whale', 'water moccasin',
           'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300,
              7500, 100, 1800, 9500, 125000]

pop_info = zip(species, population)
endangered = [spec for spec, pop in pop_info if pop < 2500]
