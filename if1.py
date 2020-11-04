#ask user to enter dish and print which cuisine is that dish#
indian =['samosa', 'daal', 'naan']
chinese = ['egg roll', 'fried rice']
italian = ['pizza', 'pasta','risotto']

dish = input('Enter a dish name:')

if dish in indian :
    print('Indian')
elif dish in chinese :
    print('Chinese')
elif dish in italian :
    print('Italian')
else:
    print('I dont know the cuisine')