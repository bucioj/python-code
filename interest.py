################################################################################
# Calculates the total amount by given interests
################################################################################

#1. Input
print('Please enter the following quantities.')
P = float(input('  How much is the initial deposit? '))
r = float(input('  What is the annual interest rate in percent? '))
n = float(input('  How many times per year is the interest compounded? '))
t = float(input('  How many years will the account be left to earn interest? '))

r /= 100.0

A = float(P * ((1.00 + (r / n))**(n * t)))
#A = "{:,}".format(A, '.2f')
# print('\n')
# message = 'At the end of ' + format(t, '.0f') + ' years, the account will be worth $' + format(A, ',.2f') + '.'
# print(At the end of + format(t, '.0f') + years, the account will be worth $ + format(A, ',.2f'))
print(f'\nAt the end of {t:.1f} years, the account will be worth ${A:,.2f}.')
# print('At the end of {t} years, the account will be worth $ {A}.' )
