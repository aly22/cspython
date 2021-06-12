import json

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior',
                    'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's",
                    'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior',
                    'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior',
                    'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore',
                    'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance',
                    'class standing': 'Senior'}]}

print(json.dumps(tester, indent=2))
compri = [name['name'] for name in tester['info']]
print(compri)

# -----------------------------------------------
# it's always the iterator variable that I shall look at ina list comprehension!!!!
compri = [name['name'] for name in tester['info'] if
          name['major'] == "Information Science"]
print(compri)

compri = [name['name'] for name in tester['info'] if
          name['class standing'] == "Senior"]
print(compri)
