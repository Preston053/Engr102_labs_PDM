# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Preston Montgomery
# Section:      522
# Assignment:   Lab 11-2
# Date:         11 9 2023

#take as input a filename and a character
user_file = str(input(f'Enter the filename: '))
user_char = str(input(f'Enter a character: '))
user_file_name = user_file[:-4]
with open(user_file,'r+') as pixel_painter:
    art_pixel = []
    csv_sorted = []
    lines = pixel_painter.read()
    sorted_lines = (lines.split('\n'))
    for x in (sorted_lines):
        csv_sorted.append(x.split(','))
    for i in (csv_sorted):
        #grabs numbers from the list
        for num in range(len(i)):
            #space for light pixels 
            if int(num) % 2 == 0:
                art_pixel.append(' ' * int(i[num]))
            #entered character for dark pixels
            else:
                art_pixel.append(user_char * int(i[num]))
        art_pixel.append(f'\n')
    with open(f'{user_file_name}.txt','a') as pixeloutput:
                pixeloutput.write(''.join(art_pixel))
print(f'{user_file_name}.txt created!')