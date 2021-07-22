user_weight = float ( input ("What is your weight? "))
user_height = float ( input ("What is your height? "))

bmi = user_weight / pow(user_height,2)

print ( "You BMI is: ", round (bmi, 2) )

if ( bmi <= 18.5 ):
    print ("Under user_weight")
elif ( bmi > 18.5 and bmi <= 24.9 ):
    print ("Normal weight")
elif ( bmi > 24.9 and bmi <= 29.9 ):
    print ("Over weight")
else:
    print ("Obesity")
