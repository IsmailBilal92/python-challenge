import os 
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("C:\\Users\\Fatima\\Boot-camp\\Third-week\\3rd_challenge\\Starter_Code\\Starter_Code\\PyBank\\Resources\\budget_data.csv")
analysis = os.path.join("C:\\Users\\Fatima\\Boot-camp\\Third-week\\3rd_challenge\\python-challenge\\PyBank_1\\analysis\\Financial_Analysis.txt")

number_month=0
total_net=0
net=0
list_net=[]
month_change=[]
net_change=0
greater_increase=[]
greater_decrease=[]
net_change_list=[]
average=0

with open(budget_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

    for row in csvreader:
        number_month+=1

        total_net = total_net + int(row["Profit/Losses"])

        net_change=float(row["Profit/Losses"])-net
        net=float(row["Profit/Losses"])
        net_change_list=net_change_list+[net]
        month_change=[month_change]+[row["Date"]]

        if net_change>greater_increase[1]:
            greater_increase[1]=net_change
            greater_increase[0]=row["Date"]
        
        if net_change<greater_decrease[1]:
           greater_decrease[1]=net_change
           greater_decrease[0]=row["Date"]

    average=sum(net_change_list)/len(net_change_list)

with open(analysis,'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("...................")   
    text_file.write("Total month:" %number_month)
    text_file.write("Totel net"%total_net)
    text_file.write("Averager"%average)
    text_file.write("Greatest Increase in net:" % (greater_increase[0], greater_increase[1]))
    text_file.write("Greatest Decrease in net:" % (greater_decrease[0], greater_decrease[1]))
    
       
        
        

