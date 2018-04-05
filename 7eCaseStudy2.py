userLocation = input("Are you in 7E? (Yes/No) ")
yes = True
no = False

if userLocation == yes:
    print("You're here")
else:
    print("you must be there")

userMoney = int(input("How much money do you have? "))

if userMoney >= 3:
    print("you're eligible to purchase this slurpee")
else:
    print("you have insufficient money to buy slurpe.")

print("To buy a slurpee, the user needs to be near a 7-11 AND have at least $3")
print("have a nice day!")
