################################################################################
# Description: This program will ensure that the stored records are of the correct format
################################################################################

# Write function(s) here

def getData(filename):
    userList =[]
    numRecord = 0

    with open(filename) as user:
        for l in user:
            userList.append(l.split(', '))
            numRecord += 1

    #remove \n record
    del userList[numRecord - 1]
    numRecord -= 1

    #strip the hanging \n from the emails
    for record in userList:
        record[len(record) - 1] = record[len(record) - 1].rstrip('\n')

    return userList

def checkNames(userList):

    for record in userList:
        while (len(record[0].split(' ')) != 2):
            #print(record[0].split(' '))
            record[0] = input(f' Record error ({record[0]}) fix: ')

    return userList

def checkGender(userList):

    gender = ['Male', 'Female']

    for record in userList:
        while(record[1] not in gender):
            record[1] = input(f' Record error for user {record[0]} ({record[1]}) fix: ')

    return userList

def checkDateAge(userList):

    day = 30
    month = 3
    year = 2021
    userAge = 0
    birthday = []

    for record in userList:
        birthday = record[2].split('/')

        while (len(birthday) != 3):
            record[2] = input(f' Record error for user {record[0]} ({record[2]}) fix: ')
            birthday = record[2].split('/')

        while (int(birthday[0]) < 1 or int(birthday[0]) > 12 or int(birthday[1]) < 1 or int(birthday[1]) > 31):
            record[2] = input(f' Record error for user {record[0]} ({record[2]}) fix: ')
            birthday = record[2].split('/')

        userAge = year - int(birthday[2])
        if ((int(birthday[0]) - month) > 0) and ((int(birthday[0]) - day) > 0):
            userAge -= 1
        record.append(userAge)

    return userList

def checkEmail(userList):

    for record in userList:
        while (not record[3].endswith('@purdue.edu')):
            record[3] = input(f' Record error for user {record[0]} ({record[3]}) fix: ')

    return userList


def main():
    filename = '3_30_sample_data.txt'

    parsedData = getData(filename)
    parsedData = checkNames(parsedData)
    parsedData = checkGender(parsedData)
    parsedData = checkDateAge(parsedData)
    parsedData = checkEmail(parsedData)

    for record in parsedData:
        print(record)


if __name__ == '__main__':
    main()
