# Function to convert feet to the selected unit
def convert(feet, choice):
    conversions = [
        feet * 12,        
        feet / 3,         
        feet / 5280,      
        feet * 304.8,     
        feet * 0.3048,    
        feet / 3280.84,
    ]
    return conversions[choice - 1]
def main():
    feet = float(input("Enter a length in feet: "))
    print("\nSelect a conversion option:")
    print("1. Inches")
    print("2. Yards")
    print("3. Miles")
    print("4. Millimeters")
    print("5. Centimeters")
    print("6. Meters")
    print("7. Kilometers")
    choice = int(input("Enter the number corresponding to your choice: "))
    if 1 <= choice <= 7:
        result = convert(feet, choice)
        units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
        print(f"{feet} feet is equal to {result:.2f} {units[choice - 1]}.")
    else:
        print("Invalid choice. Please select a number between 1 and 7.")

# Run the program
main()

