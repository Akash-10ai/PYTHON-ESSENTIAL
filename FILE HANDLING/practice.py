rows = [(10001, '2026-3-5', 'yes'),
        (10002, '2026-7-12', 'no'),
        (10003, '2026-1-20', 'yes'),
        (10004, '2026-2-2' , 'no'),
        (10005, '2026-4-9', 'yes')]


def makeFile(name):
    with open(name, 'w') as f:
        f.write('membership no date joined active \n')
        for r in rows:
            f.write("{:^13} {:<11} {:<6}\n".format(*r))

#Task: return how many members are active and how many are inactive.

def countmember(name):
    active = 0
    inactive = 0
    with open(name, 'r') as f:
        lines = f.readlines()
    for line in lines[-1:]:
        if line.splits()[-1] == 'yes':
            active += 1
        else:
            inactive += 1
    return active, inactive

makeFile('members.txt')
print(countmember('members.txt'))


