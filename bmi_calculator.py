system = input ("Which measurements system do you prefer:metric or imperial?").lower().strip()
if system == "metric":
    height = input("What is your height in meters?")
    if height.find(".") != -1 and float(height) >= 3:
        height = (float(height)/100)
    elif float(height) >=3: 
        height = (float(height)/100)
    
    weight = input("What is your weight in kilograms?")
elif system == "imperial":
    height = input("What is your height in inches?")
    weight = input("What is your weight in pounds?")
else:
    print ("Unfamiliar measurement system")

if system == "metric":
    bmi = float(weight)/(float(height)**2)
elif system == "imperial":
    bmi = (float(weight)*703)/(float(height)*float(height))

bmi=round(bmi,2)

if bmi < 16:
    category = "severely underweight"    
elif bmi <=18.4:
    category = "underweight"
elif bmi <=24.9:
    category = "normal"
elif bmi <=29.9:
    category = "overweight"
elif bmi <=34.9:
    category = "moderately obese"
elif bmi <39.9:
    category = "severely obese"
else:
    category = "morbidly obese"
print (f"Your BMI is {bmi}. It means you are {category}")
