# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Preston Montgomery
# Section:      522
# Assignment:   Lab 11-1
# Date:         11 5 2023

user_file = str(input(f'Enter the name of the file: '))
with open(user_file,'r+') as barcodefile:
    all_lines = list(barcodefile)
    valid = 0
    for nextline in all_lines:
        #adds up the first group
        evens = int(nextline[0])+int(nextline[2])+int(nextline[4])+int(nextline[6])+int(nextline[8])+int(nextline[10])
        #adds up the second group
        odds = int(nextline[1])+int(nextline[3])+int(nextline[5])+int(nextline[7])+int(nextline[9])+int(nextline[11])
        odds*=3
        evens+=odds
        last_digit = 10 - (evens%10)
        #last digit in a barcode
        if int(last_digit) == int(nextline[12]):
            valid+=1
            with open('valid_barcodes.txt','a') as validbarcodes:
                validbarcodes.write(f'{nextline}')
    print(f'There are {valid} valid barcodes')