command = ""
started = False

while True:
    command = input("> ")
    if command == "start":
        if started:
           print("car is already started...")
        else :
              started = True
              print('car started....')
    elif command == "stop":
         if not started:
           print('car is already stopped')
         else :
            started = False
            print('stoped car...')
    elif command == "help":
        print('''
start - start car
stop - stop the car 
quit - to quit
        ''')
    elif command == "quit":
        break
    else :
        print("sorry....don't understand")
