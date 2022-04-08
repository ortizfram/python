#----------LIST
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

#----------RANGE
for i in range(3):
    print ("hello world")

#----------CALCULATE
a= (((1+2)*3)/4)**5
print (a)

#-----------RAIZ(ratio)
ratio= (1+(5**(1/2)))/2
print("ratio = ", ratio)

#-----------SecondInWeek
day = 86400 #seconds
print(day*7)

#----------PossiblePasswordAmountInLower
oneLetter = 26
number = 6
if (number <= 6):
    print("if pass is 6 letters:")
    print("possibilities are: ", number**26)

#----------sectorsOfADisk
# Most hard drives are divided into sectors
# of 512 bytes each.  Our disk has a
# size of 16 GB. Fill in the blank to
# calculate how many sectors the disk has.

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = (((16*1024*1024*1024)/512))

print(sector_amount)





