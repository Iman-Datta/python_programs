def bmi_cal():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.")
    
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            if height <= 0:
                print("Height must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for height.")
    
    height_m = height / 100
    return weight / (height_m ** 2)

    
def classify_bmi():
    bmi = bmi_cal()
    print(f"Your BMI is: {bmi}")
    while True:
        try:
            gen = int(input("Enter 1 for male or 2 for female: "))
            if gen not in [1, 2]:
                print("Invalid choice. Please enter 1 for male or 2 for female.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
    
    while True:
        try:
            age = int(input("Enter your age in years: "))
            if age <= 0:
                print("Age must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")
    
    if age < 18:
        if bmi < 5:
            return "Underweight"
        elif 5 <= bmi < 85:
            return "Normal weight"
        elif 85 <= bmi < 95:
            return "Overweight"
        else:
            return "Obese"
    else:
        if gen == 1:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 25:
                return "Normal weight"
            elif 25 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
        elif gen == 2:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 24:
                return "Normal weight"
            elif 24 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
            


if __name__ == "__main__":
    classification = classify_bmi()
    print(f"You are classified as: {classification}")