from random import randint as rnd

fee = ('yes', 'no')

def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as writeFile:
        with open(exMem, 'a+') as appendFile:
            # get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            # remove header
            header = members[0]
            members.pop(0)

            inactive = [member for member in members if ('no' in member)]

            # go to the beginning of the write file
            writeFile.seek(0)
            writeFile.write(header)
            for member in members:
                if member in inactive:
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()


memReg = 'members.txt'
exReg = 'inactive.txt'

genFiles(memReg, exReg)     # 1. create the files first
cleanFiles(memReg, exReg)   # 2. then clean them

# code to help you see the files
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())