################################################################################
#
# Predict the approximate size of population of organisms
# Calculate the average daily population & number of days left
################################################################################

# Input
num_start = float(input("Starting number, in million: "))
rate_daily = float(input("Average daily increase, in percent: "))
days = int(input("Number of days to multiply: "))
rate_daily /= 100
population = num_start

# Calculation
#print("Day", "Approx. Pop", sep="\t")
print("Day   Approx. Pop")
for current_day in range(1, days + 1):
    # print(f"{current_day:3,.0f}", format(population,'15,.4f'), sep="")
    print(f"{current_day:3,.0f}", format(population,'13,.4f'))
    population = population + (rate_daily * population)

# Expected output (from homework example)
# Day       Approx. prop
#   1            2.0000
#   2            2.6000
