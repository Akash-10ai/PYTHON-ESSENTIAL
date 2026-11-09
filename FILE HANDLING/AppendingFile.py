# write a new line to text filr 

with open('/Example2.txt', 'a')  as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")


# verify if the new line in the text file

with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# trying a+ mode

with open('/Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line F\n")
    print(testwritefile.read())

    