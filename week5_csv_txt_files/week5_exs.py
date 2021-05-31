# 1
path = 'studentdata.txt'
with open(path, 'r') as file:
    for row in file:
        student_score = row.strip().split()

        if len(student_score[1:]) > 6:
            print(student_score[0])

# 2
path = "travel_plans.txt"
destination = []
with open(path, "r") as file:
    for row in file:
        travel = row.split()
        if travel[0][-1] == ":":
            destination.append(row)
# 3
path = "emotion_words.txt"
j_emotions = []
with open(path, "r") as file:
    file_ = file.read()
    file_lst = file_.split()
    for word in file_lst:
        if word[0] == "j":
            j_emotions.append(word)
print(j_emotions)
