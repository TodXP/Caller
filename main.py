import os


os.system("clear")


while True:
    
    ntc = int(input("Enter the number you want to call: "))

    match ntc:
        case 1:
            print("Calling TOD")
        case 2:
            print("Calling cops")