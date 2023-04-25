try:
    with open('/etc/hosts.allow', 'r') as myFile:
        print('File exists!')
except IOError:
    print("File does not exist!")
