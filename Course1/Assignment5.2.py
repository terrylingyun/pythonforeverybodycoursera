largest = None
smallest = None
while True:
    number = input('Enter a number:')
    if number is 'done':
        break
    else :
        try :
            number = int(number)
        except :
            print ('Invalid input')
        if largest is None :
            largest = number
        elif largest < number :
            largest = number
        if smallest is None :
            smallest = number
        elif smallest > number :
            smallest = number
print('Maximum is',largest)
print('Minimum is',smallest)
