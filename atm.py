a = int(input("Enter the Account Number :"))
b = int(input("Enter The PIN NO :"))
if a == 48587458965 and b==9846 :
    print("Account details is valid")
    print('''    Enter 1 to withdraw
    Enter 2 to balance enquiry''')
    c=int(input("enter the number :"))
    if c==1:
        d=int(input("enter the amount :"))
        if d>180050:
            print("insuffient balance")
        else:
            c = (180050-d)
            print("Amount Debited")
            print("Balance Amount :",c)
    elif(c==2):
        print(" Balance Amount = 180050")
    else:
        print("Select the Valid Number")
else:
    print("Invalid Account Number / PIN NO :")