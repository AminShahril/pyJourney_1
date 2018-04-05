check_bag = int(input("How many bags do you have? "))

if check_bag <=1:
    print("okay.")
else:
    print("That's plenty")

howManyKG = input("Do you have that bags over 50 lb? (YES/NO) ")
yes = True
no = False

if howManyKG==yes:
    print("we need to check your bag")
else:
    print("Proceed to the gate. Thank you!")
