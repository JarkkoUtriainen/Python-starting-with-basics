# user input
cabin_class = str(input('Anna hytti luokka ja paina ENTER: '))

# if statements for different option
if cabin_class == 'LUX' or cabin_class == 'lux':
    print(f'LUX on parvekkeellinen hytti yläkannella.')

elif cabin_class == 'A' or cabin_class == 'a':
    print(f'A on ikkunallinen hytti autokannen yläpuolella.')

elif cabin_class == 'B' or cabin_class == 'b':
    print(f'B on ikkunaton hytti autokannen yläpuolella.')

elif cabin_class == 'C' or cabin_class == 'c':
    print(f'C on ikkunaton hytti autokannen alapuolella.')

# wrong input
else:
    print(f'Virheellinen hyttiluokka')
