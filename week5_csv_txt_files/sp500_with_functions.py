def open_file(path):
    with open(path) as file:
        lines=[]
        for row in file.readlines()[1:]:
            #lines+=row
            lines.append(row.strip().split(','))
        return lines

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

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d={}
for c in placement:
    if c not in d:
        d[c]=0
    d[c]+=1

min_value=list(d.keys())[0]

for k in d:
    if d[k]<d[min_value]:
        min_value=k