def sortstr(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    lst = sorted(d, key=lambda x: (-d[x], x))

    return lst[0:5]


sorted_string = sortstr("asdfghjklasdfgasdas")
print(sorted_string)
