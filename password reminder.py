name = "Freddie"
user_name = input("Please enter you user name: ").title()

if user_name == name:
    print("Hello Freddie! The password is: Mercury")
else:
    print("Hello {}! See you later.".format(user_name))
