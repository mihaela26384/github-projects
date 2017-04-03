text = input("Please input some text:  ")

set_text = set(text.upper())
print(sorted(set_text))

for i in sorted(set_text):
    if i in "AEIOU" or i == " ":
        set_text.discard(i)

print(sorted(set_text))
