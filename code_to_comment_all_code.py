with open("your_file.py", "r") as file:
    lines = file.readlines()

with open("your_file.py", "w") as file:
    for line in lines:
        file.write("# " + line)
