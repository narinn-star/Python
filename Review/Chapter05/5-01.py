def myBMI(weight, height):
    bmi = (weight * 703) / (height*height)
    if bmi < 18.5:
        print('Underweight')
    elif bmi >=18.5 and bmi <=25:
        print('Normal')
    elif bmi > 25:
        print('Overweight')

myBMI(190,75)
myBMI(140,75)