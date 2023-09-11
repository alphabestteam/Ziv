with open("testing_file.txt", "r") as reading_file:
    print(reading_file.read())
with open("testing_file.txt", "w") as reading_file:
    reading_file.write("Aye Aye Captain!")
