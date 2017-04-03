with open("sample.txt", 'r') as jabber:
    for line in jabber:
        print(line, end='')

with open("sample.txt", 'a') as sample_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:>2} times {1:>2} is {2:>3}".format(j, i, i*j), file=sample_file)
        print("=" * 40, file=sample_file)
