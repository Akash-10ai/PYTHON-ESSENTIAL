# copy file to another 




with open('/Example2..txt' , 'r') as readfile:
    with open('/Example3.txt' , 'w') as writefile:
        for line in readfile:
            writefile.write(line)


# verify if the copy is successfully executed 

with open('/Example3.txt', 'r') as testwritefile:
    print(testwritefile.read())


    