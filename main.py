import os


own_number = 1

os.system("clear")


while True:
    
    ntc = int(input("Enter the number you want to call: "))

    if ntc != own_number:
        match ntc:
            case 1:
                print("Calling TOD")
            case 2:
                print("Calling cops")
    else: print("Calling yourself is kind of difficult")