#This program receives as input a measurement in feet and inches #and ouputs the measurement in centimeters.


#function to take input from the user.
def main():
    feet=input("Enter the number of feet: ")
    inches=input("Enter the number of inches: ")
    return feet_and_inches_to_centimeters(float(feet), float(inches))

#function to convert feet and inches to centimeters.

def feet_and_inches_to_centimeters(feet, inches):
     
    inch_per_foot= 12
    centimeters_per_inch = 2.54
    total_inches = feet * inch_per_foot + inches
    centimeter= total_inches * centimeters_per_inch
    return centimeter

# Main function to execute the program

if __name__ == "__main__":
    centimeters = main()
    print(f"The measurement in centimeters is: {centimeters:.2f} cm")

