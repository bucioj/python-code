################################################################################
# Author: Jose Bucio
# Date: 04/04/2021
# Description: Programs to quiz the user by enter the capital from a particular
# state of the United States
################################################################################
import random

def main():
    dictionary = get_state_data()
    #state = random.choice(list(dictionary.keys()))
    #all_states = list(state_dict.keys())
    #user = input(f'What is the capital of {state} (enter 0 to quit)? ')
    total = 0
    correct = 0
    states = list(dictionary.keys())
    while(True):
        #state, user = dictionary.popitem()
        #state = random.choice(list(dictionary.keys()))
        #response = ""
        #state = states[random.randint(0, len(states)-1)]
        state = random.choice(list(states))
        user = input(f'What is the capital of {state} (enter 0 to quit)? ')
        #response = input()
        if user == '0':
            break
        total += 1

        if dictionary.get(state).lower() == user.lower():
        #if dictionary[state].lower() == user.lower():
            correct += 1
            #dictionary.pop(state, None)
            #dictionary.popitem()
            print('That is correct!')
        else:
            print('That is incorrect.')
            #dictionary.popitem(state)
            print(f'The capital of {state} is {dictionary.get(state)}.')
    print(f'You answered {correct} out of {total} questions correctly.')

def get_state_data():
    #states = []
    with open('state_capitals.txt', 'r') as foo:
        lines = foo.read().splitlines()
        #lines = foo.read().splitlines()
        dict = {}
        for line in lines:
            capital, state = line.split(",")
            dict[state.strip()] = capital.strip()
            #line = line.strip('\n')
            #capitals = line.split(',')
            #states.append(capitals)
            #capital, state = line.split(',')
            #states[state.strip()] = capital.strip()
    foo.close()
    return dict

if __name__ == '__main__':
    main()
