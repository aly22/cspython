#[1] sp cp [5] for interest rate
#first I need to read in the contents
#then I need 3 accumulator variables
max_interest=[]
total_SP=0
mean_SP=0
with open("../week5_csv_txt_files/SP500.txt","r") as file:

    for row in file.readlines()[1:]:
        lines=row.strip().split(',')
        #i need to extract the information found in the year given
        #this method works for almost any date if not sh** happens
        if (int(''.join(lines).split('/')[0])>5 and int("".join(lines).split('/')[2][0:4])==2016) or (int(''.join(lines).split('/')[0])<6 and int("".join(lines).split('/')[2][0:4])==2017):
            total_SP+=float(lines[1])
            mean_SP=total_SP/12
        interest=float(lines[5])
        max_interest.append(interest)
    max_interest=max(max_interest)
    print(mean_SP)
    print(max_interest)