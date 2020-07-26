nation = input('Where you from:')
age = input('What is your age:')
age = int(age)
if nation == 'TW' :
    if age >= 18:
        print('You are allow to drive with liences')
    else:
        print('Not for you')
elif nation =='USA':
    if age >= 16:
        print('You are allow to drive with liences')
    else:
        print('Not for you')
else :
    print('Only TW and USA')
