# 1

olympics = "Beijing", "London", "Rio", "Tokyo"

# 2

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'),
              ('Tokyo', 'Japan', 2020, 'Future')]


def countries(lst):
    countries_lst = []
    for i in lst:
        countries_lst.append(i[1])
    return countries_lst


country = countries(tuples_lst)
print(country)
# 3


olymp = ('Rio', 'Brazil', 2016)

city, country, year = olymp


# 4

def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown


# 5


gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13, 'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}


def golds(dic):
    num_medals = []
    for country, num in dic.items():
        num_medals.append(num)

    return num_medals


num_medals = golds(gold)
