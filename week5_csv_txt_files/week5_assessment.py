# 1
path = "travel_plans.txt"
with open(path, "r") as  file:
    num = len(file.read())

# 2
path = "emotion_words.txt"
with open(path, "r") as file:
    num_words = 0
    emotion_lst = file.read().split()
    for word in emotion_lst:
        num_words += 1
# 3
path = "school_prompt.txt"
with open(path, "r") as file:
    prompt_lns = file.readlines()
    num_lines = 0
    for line in prompt_lns:
        num_lines += 1
# 4


path = "school_prompt.txt"
with open(path, "r") as file:
    beginning_chars = file.read(30)

# 5

path="school_prompt.txt"
with open(path,"r") as file:
    three=[]
    for row in file:
        lines=row.strip().split()
        three.append(lines[2])

# 6

path="emotion_words.txt"
with open(path,"r") as file:
    emotions=[]
    for row in file:
        lines=row.strip().split()
        emotions.append(lines[0])

# 7

path="travel_plans.txt"
with open(path,"r") as file:
    first_chars=file.read(33)

# 8

path="school_prompt.txt"
with open(path,"r")as file:
    p_words=[]
    school_lst=file.read().split()
    for word in school_lst:
        if "p" in word:
            p_words.append(word)
    # with a nested for loop the same
    # for row in file:
    #     schl_prompts=row.strip().split()
    #     for word in schl_prompts:
    #         if "p" in word:
    #             p_words.append(word)
    print(p_words)