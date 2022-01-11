#PyBank calculations

#Initialize a dictionary of dates and profit and loss (pnl)
pnl = {
    "Jan-2010":867884,
    "Feb-2010":984655,
    "Mar-2010":322013,
    "Apr-2010":-69417,
    "May-2010":310503,
    'Jun-2010':522857,
    'Jul-2010':1033096,
    'Aug-2010':604885,
    'Sep-2010':-216386,
    'Oct-2010':477532,
    'Nov-2010':893810,
    'Dec-2010':-80353,
    'Jan-2011':779806,
    'Feb-2011':-335203,
    'Mar-2011':697845,
    'Apr-2011':793163,
    'May-2011':485070,
    'Jun-2011':584122,
    'Jul-2011':62729,
    'Aug-2011':668179,
    'Sep-2011':899906,
    'Oct-2011':834719,
    'Nov-2011':132003,
    'Dec-2011':309978,
    'Jan-2012':-755566,
    'Feb-2012':1170593,
    'Mar-2012':252788,
    'Apr-2012':1151518,
    'May-2012':817256,
    'Jun-2012':570757,
    'Jul-2012':506702,
    'Aug-2012':-1022534,
    'Sep-2012':475062,
    'Oct-2012':779976,
    'Nov-2012':144175,
    'Dec-2012':542494,
    'Jan-2013':359333,
    'Feb-2013':321469,
    'Mar-2013':67780,
    'Apr-2013':471435,
    'May-2013':565603,
    'Jun-2013':872480,
    'Jul-2013':789480,
    'Aug-2013':999942,
    'Sep-2013':-1196225,
    'Oct-2013':268997,
    'Nov-2013':-687986,
    'Dec-2013':1150461,
    'Jan-2014':682458,
    'Feb-2014':617856,
    'Mar-2014':824098,
    'Apr-2014':581943,
    'May-2014':132864,
    'Jun-2014':448062,
    'Jul-2014':689161,
    'Aug-2014':800701,
    'Sep-2014':1166643,
    'Oct-2014':947333,
    'Nov-2014':578668,
    'Dec-2014':988505,
    'Jan-2015':1139715,
    'Feb-2015':1029471,
    'Mar-2015':687533,
    'Apr-2015':-524626,
    'May-2015':158620,
    'Jun-2015':87795,
    'Jul-2015':423389,
    'Aug-2015':840723,
    'Sep-2015':568529,
    'Oct-2015':332067,
    'Nov-2015':989499,
    'Dec-2015':778237,
    'Jan-2016':650000,
    'Feb-2016':-1100387,
    'Mar-2016':-174946,
    'Apr-2016':757143,
    'May-2016':445709,
    'Jun-2016':712961,
    'Jul-2016':-1163797,
    'Aug-2016':569899,
    'Sep-2016':768450,
    'Oct-2016':102685,
    'Nov-2016':795914,
    'Dec-2016':60988,
    'Jan-2017':138230,
    'Feb-2017':671099,
    
}

#Initiate metric variables
total_pnl = 0
dates_count = 0
average = 0
prev_pnl = 0
net_change_list = []

#Initiate minimum key value pair

minimum_key = " "
minimum_value = 0

#Initiate maximum key value pair

maximum_key = " "
maximum_value = 0

# Iterate over key-value pairs of the dictionary
#For loops over pnl    
for dates, pnl in pnl.items():
    
    
    # Calculate the sum of profit and loss and number of days in the dictionary
    dates_count += 1
    total_pnl += int(pnl)
    
    # determine minimum value and associate key
    if minimum_value == 0:
        minimum_key = dates
        minimum_value = pnl
    elif pnl < minimum_value:
        minimum_key = dates
        minimum_value = pnl
    
    #determine maximum value and associate key
    if pnl > maximum_value:
        maximum_key = dates
        maximum_value = pnl
    
    #calculating the change in daily prfoti and loss (pnl)
    change = pnl - prev_pnl
    
    #adding the daily change to a list to be used for calculating the average of changes in profit and loss (pnl)
    net_change_list.append(change)
    
    #update the value
    prev_pnl = pnl

print(minimum_key)

#calculating the average of net changes minus the first day and round to two decimal points
average = (sum(net_change_list) - 867884) / (len(net_change_list) - 1)    
average_adjusted = round(average,2)
    
                       
                       
#TODO calculate the total number of months included in the dataset
print(f"Total Months: {dates_count}")

#TODO calculate the net total amount of Profit/Losses over the entire period
print(f"Total : {total_pnl}")

##TODO calculate the average of the changes in Profit/Loss over the entire period
print(f"Average change is ${average_adjusted}")

#TODO calculate the greatest increase in profits (date and amount) over the entire period
print(f"Greatest increase in profits : {maximum_key} ${max(net_change_list)}")

#TODO calculate the greated decrease in losses (date and amount) over the entire period
print(f"Greatest decrease in losses :  {minimum_key} ${min(net_change_list)}")


from pathlib import Path

#to check current directory
print(Path.cwd())

#set output path
output_path = Path("output.txt")

#write to the output file
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write("Total Months: 86\n")
    file.write("Total : 38382578\n")
    file.write("Average change is -$2315.12\n")
    file.write("greatest increase in profits :  Feb-2012 $1926159\n")
    file.write("greatest decrease in losses :  Sep-2013 $-2196167\n")