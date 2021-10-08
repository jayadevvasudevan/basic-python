# Health management system

def getdate():
    import datetime
    return datetime.datetime.now()

# Condition Checker
def con(s):
    if(s.lower() == "y"):
        return True
    else:
        return False

condition = True
while(condition != False):
    # To log Data
    data = int(input('''You want to retrieve data or log data
Press!!(1) to log data and Press!!(2) to retrieve data : '''))
    if(data == 1):
        option = int(input("Enter 1 for writing log of exercise and 2 for diet : "))
        if(option == 1):
            name = input("Enter Your name : ")
            namefile = name.lower()+"_exercise.txt"
            try:
                with open(namefile,"a",) as f:
                    f.write(str(getdate()))
                    f.write("\n")
                    n = int(input("How many exercises you did : "))
                    while(n != 0):
                        s = input("Enter your exercise name : ")
                        f.write(s)
                        f.write("\n")
                        n = n - 1
                    statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
                    condition = con(statement)
            except:
                with open(namefile,"x",) as f:
                    f.write(str(getdate()))
                    f.write("\n")
                    n = int(input("How many exercises you did : "))
                    while(n != 0):
                        s = input("Enter your exercise name : ")
                        f.write(s)
                        f.write("\n")
                        n = n - 1
                    statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
                    condition = con(statement)

        else:
            name = input("Enter Your name : ")
            namefile = name+"_diet.txt"
            try:
                with open(namefile,"a",) as f:
                    f.write(str(getdate()))
                    f.write("\n")
                    n = int(input("How many meals do you want to log : "))
                    while(n != 0):
                        s = input("Enter your meal : ")
                        f.write(s)
                        f.write("\n")
                        n = n - 1
                    statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
                    condition = con(statement)

            except:
                with open(namefile,"x",) as f:
                    f.write(str(getdate()))
                    f.write("\n")
                    n = int(input("How many meals do you want to log : "))
                    while(n != 0):
                        s = input("Enter your meal : ")
                        f.write(s)
                        f.write("\n")
                        n = n - 1
                    statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
                    condition = con(statement)

# To retrieve Information     
    else:
        name = input("Enter Your name : ")
        ext = input("Enter which data you want to retrieve e (for exercise) and d (for diet) : ")
        namefile = ""
        if(ext == "e"):
            namefile = name+"_exercise.txt"
        else:
            namefile = name+"_diet.txt"
        
        try:
            with open(namefile,"r",) as f:
                for line in f:
                    print(line,end="")
                statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
                condition = con(statement)
        
        except:
            print("You need to log data first in order to retrieve it ")
            statement = input("Do you want to continue! or exit! (y) for continue and (n) for exit) : ")
            condition = con(statement)



        