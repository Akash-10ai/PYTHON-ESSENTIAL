# write line to file 

exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file

with open(exmp2, 'w' ) as testwritefile:
    print(testwritefile.read())


# Wtite lines to file 

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A \n")
    writefile.write("This is line B \n")

# cheak wheather wtite to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# sample list of text 

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# write the string in the list to text file

with open('/Example2.txt', 'r') as teatwritefile:
    print(teatwritefile.read())

with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")

with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

    