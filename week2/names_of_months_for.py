lst=["January","February","March","April","May","June"]
prefix="One of the months of the year is "
sentence=[]
for i in lst:
    sentence.append(prefix+i)
for i in sentence:
    print(i)