# read the example.txt
example1 = "example.txt"
file1 = open(example1, "r")

# print the path of file 

file1.name

# print the mode of files, either 'r' or 'w'

file1.mode

# read the file

FileContent = file1.read()
FileContent

# print  the filr with '\n' as a new line

print("FileContent")

# type of file content 

type(FileContent)

# close file after finish 

file1.close()


