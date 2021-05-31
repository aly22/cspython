
prefixes = "JKLMNOPQ"
suffix = "ack"
prefixes=list(prefixes)
prefixes[prefixes.index("O")]+='u'
prefixes[prefixes.index("Q")]+='u'
for p in prefixes:


    print(p + suffix)
print(prefixes)