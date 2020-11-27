OUTPUT_FILE = 'name.txt'
out_file = open(OUTPUT_FILE, 'w')
name = input("What's your name?")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
total = number_1 + number_2
print(total)
in_file.close()

in_file = open("numbers.txt")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

