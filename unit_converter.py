################################################################################
# This program converts from imperial units (inch, feet, miles)
# to metric units (mm, cm, m, km)
################################################################################

# The total of 1 miles, 2 feet, and 2 inches is: 3km, 0m, 2cm, 2mm


#input
inches = int(input('Please enter a length in inches: '))
feet = int(input('Please enter a length in feet: '))
miles = int(input('Please enter a length in miles: '))

#length conversion values
feetPI = 12 #feet per mile
milesPI = 5280 * feetPI

mmPI = 25.4

cmm = 10 # mm in 1 cm
mm = 100 * cmm
kmm = 1000 * mm


totalMM = int((inches + feet * feetPI + miles * milesPI) * mmPI)

#calculate total metric measurements
KM = totalMM // kmm
M = (totalMM % kmm) // mm
CM = (totalMM % mm) // cmm
MM = totalMM & cmm


#output
print('The total of ', end='')
if miles:
    print(f'{miles} mile(s)', end='')
if feet:
    if miles:
        if inches:
            print(', ', end='')
        else:
            print(' and ', end='')
        if feet > 1:
            print(f'{feet} feet', end='')
        else:
            print(f'{feet} foot', end='')
if inches:
    if feet or miles:
        print(' and ', end='')
    print(f'{inches} inch(es)', end='')
print(' is: ', end='')


if KM:
    print(f'{KM}km', end='')
if M:
    if KM:
        if CM or MM:
            print(', ', end='')
        else:
            print(' and ', end='')
    print(f'{M}m', end='')
if CM:
    if KM or M:
        if MM:
            print(', ', end='')
        else:
            print(' and ', end='')
    print(f'{CM}cm', end='')
if MM:
    if KM or M or CM:
        print(' and ', end='')
    print(f'{MM}mm', end='')
print('.')
