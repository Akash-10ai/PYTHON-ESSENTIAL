rows = [(10001, '2016-3-5',  'yes'),
        (10002, '2018-7-12', 'no'),
        (10003, '2017-1-20', 'yes'),
        (10004, '2019-11-2', 'no'),
        (10005, '2015-6-9',  'yes')]

def makeFile(name):
    with open(name, 'w') as f:                       # 'w' creates or overwrites
        f.write('Membership No  Date Joined  Active  \n')
        for r in rows:
            f.write("{:^13}  {:<11}  {:<6}\n".format(*r))

#Task: add a new member to the end of the register without touching the existing rows


def addMember(name, number, date):
    with open(name, 'a') as f:
        f.write("{:^13}  {:<11}  {:<6}\n".format(number, date, 'yes'))

makeFile('members.txt')
addMember('members.txt', 10006, '2026-11-10')
print(open('members.txt').read())


#Task: change one member’s status from no to yes. This is the same read, seek(0), rewrite, truncate() pattern as your assignment.

def reactivate(name, number):
    with open(name, 'r+') as f:
        lines = f.readlines()           # 1. read everything
        f.seek(0)                       # 2. go back to the start
        f.write(lines[0])               # 3. write the header back
        for line in lines[1:]:
            parts = line.split()
            if parts[0] == str(number): # membership number is column 1
                line = "{:^13}  {:<11}  {:<6}\n".format(parts[0], parts[1], 'yes')
            f.write(line)
        f.truncate()                    # 4. cut leftover old text

makeFile('members.txt')
reactivate('members.txt', 10002)
print(open('members.txt').read())

#Task: find a member’s join date and return None if they aren’t found.

def findMember(name, number):
    with open(name, 'r') as f:
        next(f)                          # skip the header line
        for line in f:                   # reads one line at a time
            parts = line.split()
            if parts[0] == str(number):
                return parts[1]          # date joined
    return None

makeFile('members.txt')
print(findMember('members.txt', 10003))  # 2017-1-20
print(findMember('members.txt', 99999))  # None