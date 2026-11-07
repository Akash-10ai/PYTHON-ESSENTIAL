with open("number.txt",  "w") as f:
    for i in range(1, 6):
        f.write(str(i) + "\n")

with open("number.txt", "r") as f:
    print(f.read())