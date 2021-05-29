words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[-1] == "e":
        d = word + "d"
        past_tense.append(d)
    else:

        past_tense.append(word + "ed")
print(past_tense)
