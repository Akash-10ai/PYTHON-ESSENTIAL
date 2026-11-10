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

#Task: copy only the active members, with the header, into a new file.


def saveActive(src, dest):
    with open(src, 'r') as f:
        lines = f.readlines()
    with open(dest, 'w') as out:
        out.write(lines[0])                        # header first
        for line in lines[1:]:
            if line.split()[-1] == 'yes':
                out.write(line)                    # write the whole line unchanged

makeFile('members.txt')
saveActive('members.txt', 'activeOnly.txt')
print(open('activeOnly.txt').read())