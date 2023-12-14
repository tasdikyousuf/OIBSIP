def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    elif bmi <= 35:
        return "Obese"
    else:
        return "Morbidly Obese"

def bmi_calculator():
    weight = float(input("Enter body mass in kilograms: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)

    print("BMI:", round(bmi, 2))
    print("Category:", bmi_category)

bmi_calculator()
