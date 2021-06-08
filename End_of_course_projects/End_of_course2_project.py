punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(s):
    stri = ''
    for c in s:
        if c in punctuation_chars:
            stri += c.replace(c, '')
        else:
            stri += c

    return stri


def get_neg(s):
    s = strip_punctuation(s).lower()
    cnt = 0
    for word in s.split():
        if word in negative_words:
            cnt += 1
    return cnt


def get_pos(s):
    s = strip_punctuation(s).lower()
    cnt = 0
    for word in s.split():
        if word in positive_words:
            cnt += 1
    return cnt


def open_file(path):
    twitter_data = []
    with open(path) as file:
        for lin in file.readlines()[1:]:
            twitter_data.append(lin.strip().split(','))
    return twitter_data


def calculate(lst):
    pos = []
    neg = []
    net = []
    number_rts = []
    number_reps = []
    for tweet in lst:
        pos.append(get_pos(tweet[0]))
        neg.append(get_neg(tweet[0]))
        net.append(int(get_pos(tweet[0]) - int(get_neg(tweet[0]))))
        number_rts.append(int(tweet[1]))
        number_reps.append(int(tweet[2]))

    return (number_rts, number_reps, pos, neg, net)
    # prod=pos+neg
    # for num in range(len(prod)):
    #     if num==len(prod)/2:
    #         break
    #     net.append(prod[num]-prod[(len(prod)//2)+num])


def write_file(tup, path, header_names):
    with open(path, "w") as file:

        file.write(", ".join(header_names))
        file.write('\n')
        # cols=[]
        for col in zip(*tup):
            rows="{}, {}, {}, {}, {}".format(*col)
            file.write(rows+'\n')
        return file

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
path = "project_twitter_data.csv"

twitter_data = open_file(path)

twitter_data_calc = calculate(twitter_data)
print(twitter_data_calc)
header_names=["Number of Retweets", "Number of Replies", "Positive Score","Negative Score","Net Score"]
write_file(twitter_data_calc,"resulting_data.csv",header_names)