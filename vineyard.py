################################################################################
# Description: This program calculates the area for a vineyard
################################################################################

#1. Input
print('Enter the following quantities in feet.')
# print('How long is this row? ')
# row = input()
row = float(input('  How long is this row? '))

# print('How wide is the end-post assembly? ')
end = float(input('  How wide is the end-post assembly? '))
#end = input('How wide is the end-post assembly? ')

# print('How much space should be between the vines? ')
space = float(input('  How much space should be between the vines? '))
#space = input('How much space should be between the vines? ')

#2. Calculation
V = int((row - (2 * end)) / space)

#3. Results
#print('\n')
#message = 'This row has enough space for ' + format(V, '.0f') + ' vine(s).'
#print(message)
print(f'\nThis row has enough space for {V:.0f} vine(s).')
