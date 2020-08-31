demrt = 0
g = 5
while True:
    speed = int(input('enter speed '))
    speed_checker = 70
    k =0
    if int(speed) >= int(speed_checker) :
        demrt = demrt + 1
        k = demrt
        if demrt >= g:
            print('your license is cancelled')
            l = str(input('Enter a number '))
            m = input('Enter driver name ')
            print (f"driver name is {m} vehicle number is {l}..."
                   f"Driver's license is suspended for 5 years ")
            break
        elif g > demrt:
            print('demirit point is ', k)
    else:
        print('you are safe')




