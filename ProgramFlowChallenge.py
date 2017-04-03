address = input("Please enter the address separated by . : ")
count = 1
length = 0
substring = ''

for i in range(0, len(address)):
    if address[i] in {"."}:
        count += 1
        print("The segment number {0} is {1}".format(count-1, substring))
        print("The segment has {} digits".format(len(substring)))
        substring = ''
    else:
        substring += address[i]
print("The segment number {0} is {1}".format(count, substring))
print("The segment has {} digits".format(len(substring)))
print("Total number of segments is {}".format(count))
