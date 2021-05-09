################################################################################
# Description: This program calculates the Reynolds number given temp, diameter, velocity
################################################################################

velocity = float(input("Enter the velocity of water in the pipe: "))
diameter = float(input("Enter the pipe's diameter: "))
temp = float(input("Enter the temperature in °C as 5, 10, or 15: "))
# message = ""

if temp == 5:
    # 1.49 × 10−6
    v = 0.00000149
    Re = float((velocity * diameter) / v)
    #print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is", format(Re,'.2e'), ".")
    print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is ", format(Re,'.2e'), ".", sep="")

elif temp == 10:
    # 1.31 × 10−6
    v = 0.00000131
    Re = float((velocity * diameter) / v)
    #print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is", format(Re,'.2e'), ".")
    print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is ", format(Re,'.2e'), ".", sep="")

elif temp == 15:
    # 1.15 × 10−6
    v = 0.00000115
    Re = float((velocity * diameter) / v)
    #print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is", format(Re,'.2e'), ".")
    print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}°C is ", format(Re,'.2e'), ".", sep="")

#else:
    #print message = "Error, please enter the temperature °C as 5, 10, or 15. Try again. "
