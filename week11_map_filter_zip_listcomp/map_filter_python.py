def triple(value):
    print("post-it note for:", value)
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)
# map:just like the key optional parameter in sorted the iterable gets passed in
# automitacally and the „post-it note” thing happpens then behind the scenes
# each item of the iterable gets associated with the functions return value
# some_list=list(map(<transformer function>,<sequence>))
# filter: So, unlike with map where the function was a transformer that was
# taking the input and transforming it into something else, here we're not
# transforming the input. We're just making a binary decision about it. Is it
# true? Meaning keep it in, or is it false? Meaning filter it out.