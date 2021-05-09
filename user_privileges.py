################################################################################
# Author: Jose Bucio
# Date: 04/25/2021
# Description: Programs provide the user's profile including name, email, and privs
################################################################################

class Privileges:
    def __init__(self, privs = ['interact', 'post', 'comment', 'edit', 'ban']):
        return
    # sets list of strings 'interact', 'post', 'comment', 'edit', 'ban'
    # takes a string parameter, add that string to set of privs and print granted
    def grant(self):
        print('Granted')
        return
    # takes a string parameter, remove string from set of privs and print revoke
    def revoke(self):
        return
    # takes a string paramets, remove string from set of privs in alph as comma separated
    def get_privs(self):
        return

class User:
    def __init__(self, name, email, privs):
        self.name = name.capitalize()
        self.email = email
        self.privs = privs
        return

    def describe_user(self):
        print('Name: ' + self.name)
        print('Email: ' + self.email)
        print('Privs: ' + self.privs)



def main():



if __name__ == '__main__':
    main()
