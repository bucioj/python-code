###############################################################################
# Programs to do has hash patterns & Range by prefer number of row hashes
###############################################################################

row = int(input("Enter the number of lines: "))

#number of rows
for rows in range(row):
    print("#", end="", sep="")
    #print(" ", end="", sep="")
    for spaces in range(rows):
        #print( "#", end="")
        print(" ", end="")
    print("#", sep="")
