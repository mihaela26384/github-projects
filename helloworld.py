name = input("Please type your name:")
age = int(input("Please type your age:"))
if name and age:
    if 17 < age < 31:
        print("Welcome {0} to your holiday!".format(name))
    else:
        print("I'm sorry {0} but you cannot enter".format(name))
else:
    print("One or more requirements are not fulfilled")

print("################################################################")