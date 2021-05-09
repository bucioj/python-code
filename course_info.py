################################################################################
# Author: Jose Bucio
# Date: 04/04/2021
# Description: Programs to display the course information including room,
# instructor, and time based on the user's input
################################################################################

def main():
    data = get_course_data() # declares get course data function
    #data = course_available.keys()

    # input the course number
    course = input('Enter a course number: ')
    # checks to see if course number is valid
    count = 0
    # checks the keys from data
    for key in data:
        if (key != course):
            count += 1
    # checks to see user input enters valid course number from fake course data
    if (count == len(data)):
        print(f'{course} is an invalid course number.')
    else:
    #if course == 'CS101' or course == 'CS102' or course == 'CS103' or course == 'NT110' or course == '1411':
        # prints information for valid course number
        print(f'The details for course {course} are:')
        print('  Instructor:', data[course]['instructor'])
        print('        Room:', data[course]['room'])
        print('        Time:', data[course]['time'])
    # print invalid otherwise
    #else:
        #print(f'{course} is an invalid course number.')


# collection of course data function
def get_course_data():
    # fake course data inputs given
    course_data = {'CS101': {'room': '3004', 'instructor': 'Haynes', 'time': '8:00 a.m.'}, 'CM241' : {'room': '1411', 'instructor': 'Lee', 'time': '1:00 p.m.'}, 'CS102' : {'room': '4501', 'instructor' : 'Alvarado', 'time': '9:00 a.m.'}, 'CS103' : {'room': '6755', 'instructor': 'Rich', 'time': '10:00 a.m.'}, 'NT110' : {'room': '1244', 'instructor': 'Burke', 'time': '11:00 a.m.'}}
    return course_data

if __name__ == '__main__':
    main()
