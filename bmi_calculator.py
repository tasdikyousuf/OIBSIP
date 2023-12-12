# function with necessary conditions and statements 
def bmi_calculator(weight, height):

    bmi = weight / (height ** 2)
    print(round(bmi,2))

    if (bmi > 0):
        if (bmi <= 18.5):
            print("Underweight")
        elif (bmi <= 25):
            print("Normal")
        elif (bmi <= 30):
            print("Overweight")
        elif (bmi <= 35):
            print("Obese")
        else:
            print("Morbidly Obese")
    else:
        print("enter valid details")

#user input
user_weight = float(input("Enter body mass in kilograms: "))
user_height = float(input("Enter height in meters: "))

bmi_calculator(user_weight, user_height) #utilization of function