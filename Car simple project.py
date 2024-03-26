command = ''
i = 0
o = 0
print("Type help to begin")
while command != "QUIT":
    command = input("> ").upper()
    if command == "HELP":
        print("""
Help - Instructions
Start - Start car
Stop - Stop car
Quit - Quit program""")
    if command == "START" and i == 0:
        print("Car has started")
        i += 1
        o = 0
    elif command == "START" and i != 0:
        print("Car has already started")
    elif command == "STOP" and i == 0:
        print("Car has not started yet")
    elif command == "STOP" and i != 0:
        print("Car has stopped")
        i = 0
    elif command == "STOP" and o != 0:
        print("Car has already stopped")
        o += 1
        i = 0
    elif command == "QUIT":
        break
    else:
        print("I don't understand")