printing_mode = False
file_data = ""
with open("config.txt", "r") as reading_file:
    for line in reading_file:
        line_values = line.strip().split(" = ")
        if line_values[0] == "DATA":
            file_data = line_values[1]
        if line_values[0] == "SILENT":
            printing_mode = line_values[1]

if printing_mode:
    print(file_data)

with open("new_file.txt", "w") as writing_file:
    writing_file.write(file_data.upper())
