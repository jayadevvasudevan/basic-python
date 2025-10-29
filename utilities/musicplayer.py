from pygame import mixer 
mixer.init()
mixer.music.set_volume(4)

while(True):
    print("1. Ranjha")
    print("2. Raataan Lambiyaa")
    print("3. Sakhiyaan")
    print("4. Stay")
    print("5. Exit")

    user_choice = int(input("Enter ur choice : "))
    if user_choice not in [1,2,3,4,5]:
        print("please enter valid choice")
        continue
    if user_choice == 1:
        mixer.music.load("Ranjha - Shershaah.mp3")
        mixer.music.play()
    elif user_choice == 2:
        mixer.music.load("Raataan Lambiyan - Shershaah.mp3")
        mixer.music.play()
    elif user_choice == 3:
        mixer.music.load("Sakhiyan 2 - Bell Bottom.mp3")
        mixer.music.play()
    elif user_choice == 4:
        mixer.music.load("Stay.mp3")
        mixer.music.play()
    elif user_choice == 5:
        exit(0)

    print("press c to continue | q to quit")
    choice = ""
    while(choice != "c" and choice != "q"):
        choice = input()
        if choice == "q":
            exit()
        elif choice == "c":
            continue
       
