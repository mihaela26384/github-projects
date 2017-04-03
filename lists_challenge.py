menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["spam", "sausage", "bacon", "spam"])
menu.append(["spam", "sausage", "bacon", "egg"])
menu.append(["sausage", "cheese", "egg", "milk"])
menu.append(["milk", "spam", "bacon", "spam"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
