print('This simple code calculate Your BMI - Body Mass Index')
print()
print('Remember to use a dot "." as a separator...')
print()
weight = float(input('What is Your weight in "kg" >> '))
height = float(input('What is Your height in "m" >>'))
bmi = weight / (height ** 2)
print('If You are', height, 'm tall, and weight', weight, 'Your BMI is:', round(bmi, 2))
