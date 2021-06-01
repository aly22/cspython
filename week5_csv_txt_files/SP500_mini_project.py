# [1] for closing price [5] for interest rate
#first i need four accumulator variables
path = "SP500.txt"
mean_SP=0
total_SP=0
max_interest=0
curr_interest=0
with open(path, "r") as  file:
    #I need to split the lines and exclude the heading

    for row in file.readlines()[1:]:
        print(row)
        lines=row.strip().split(',')
        #then i need to extract information on the period given
        if (int(','.join(lines).split('/')[0])>5 and int(','.join(lines).split('/')[2][0:4])==2016) or (int(','.join(lines).split('/')[0])<6 and int(','.join(lines).split('/')[2][0:4])==2017):
            total_SP+=float(lines[1])
            mean_SP=total_SP/12
            # then i need to find the maximum of the long term interest rate
            if float(lines[5])>max_interest:
                max_interest=float(lines[5])
            curr_interest=float(lines[5])
    print(mean_SP)
    print(max_interest)
