name =   input("Enter your name: ")
branch = input("enter your branch: ")

with open("info.txt", "w") as f:
    f.write("name: " + name + "\n")
    f.write("branch: " + branch + "\n")

with open("info.txt", "r") as f:
    print(f.read())