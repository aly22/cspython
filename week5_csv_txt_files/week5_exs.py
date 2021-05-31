
#1
path='studentdata.txt'
with open(path,'r') as file:
    for row in file:
        student_score=row.strip().split()

        if len(student_score[1:])>6:
            print(student_score[0])

