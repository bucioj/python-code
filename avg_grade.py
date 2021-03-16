################################################################################
# 
# Description: Calculate the average and determine the grade from given score
#
###############################################################################
# Input Valid score
def get_valid_score():
    #enter score 1, 2, 3, 4, and 5
    input_score = float(input("Enter a score: "))
    while input_score < 0 or input_score > 100:
        #if input_score < 0 or input_score > 100:
        print("Invalid Input. Please try again.")
        input_score = float(input("Enter a score: "))
    return input_score

# Calculate Average
def calc_average(total):
    #sum = 0
    #for num in range(num_list):
        #sum += num
        #average_score = sum / len(num_list)
    #return total / len(total)
    average_score = total / 5
    return average_score

# Determine grade from input
def determine_grade(input_score):
    #for number in input_score:
    if 90 <= input_score <= 100: grade = "A"
    elif 80 <= input_score < 90: grade = "B"
    elif 70 <= input_score < 80: grade = "C"
    elif 60 <= input_score < 70: grade = "D"
    else: grade = "F"
    return grade

# Main
def main():
    score1 = float(get_valid_score())
    print("The letter grade for {:.1f} is {}.".format(score1, determine_grade(score1)))
    score2 = float(get_valid_score())
    print("The letter grade for {:.1f} is {}.".format(score2, determine_grade(score2)))
    score3 = float(get_valid_score())
    print("The letter grade for {:.1f} is {}.".format(score3, determine_grade(score3)))
    score4 = float(get_valid_score())
    print("The letter grade for {:.1f} is {}.".format(score4, determine_grade(score4)))
    score5 = float(get_valid_score())
    print("The letter grade for {:.1f} is {}.".format(score5, determine_grade(score5)))

    #num_list = [score1, score2, score3, score4, score5]
    total = score1 + score2 + score3 + score4 + score5

    average = calc_average(total)
    print(f"The average score is {average:.2f}.")
    #return

# Don't edit these 2 lines & make sure they're at the end of your program
if __name__ == '__main__':
    main() # calls the main function
