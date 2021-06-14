def open_file(path):
    with open(path) as file:
        return [row.strip().split(',') for row in file.readlines()[1:]]

def calc(lst):
    mean_SP=0
    total=0
    max_i=[]
    for row in lst:
        if (int(''.join(row).split('/')[0])>5 and int(''.join(row).split('/')[2][0:4])==2016) or (int(''.join(row).split('/')[0])<6 and int(''.join(row).split('/')[2][0:4])==2017):
            total+=float(row[1])
            mean_SP=total/12

        max_i.append(float(row[5]))

    max_i=max(max_i)
    return mean_SP,max_i




path="../week5_csv_txt_files/SP500.txt"
lines=open_file(path)
mean_SP,max_interest=calc(lines)
