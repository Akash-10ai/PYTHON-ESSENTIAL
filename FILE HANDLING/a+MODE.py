with open('/Example2.txt', 'a+') as testwritefile:
    print("INitial Location: {}" .format(testwritefile.tell()))

data = testwritefile.read()
if not data: # empty  string return false in python 
    print('Read Nothing')

else:
    print(testwritefile.read())

testwritefile.seek(0, 0) # move 0 bytes from beginning of the file

print("\nNew Location: {}" .format(testwritefile.tell()))

data = testwritefile.read()
if not data:
    print("Reading Nothing")
else:
    print(data)

print("Location after read: {}".format(testwritefile.tell()))