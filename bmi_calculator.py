def calculate_bmi(weight, height):
    return weight / height**2

def get_bmi_category(bmi):
    if bmi <= 18.5:
        return ('Underweight. ')
    elif bmi > 18.5 and bmi <25:
        return('Normal weight. ')
    elif bmi > 25 and bmi <30:
        return('Overweight. ')

    else:
        return ('Obesity. ')

def bmi_calculator():
    print('Welcome to BMI calculator! ')

    while True:
        try:
            weight = float(input('Enter weight in kg: '))
            height = float(input('Enter height in m: '))

            if weight <= 0 or height <= 0:
                print('Please enter a valid weight and height.')
                continue
        except ValueError:
            print('You must enter the number')
            continue

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f'Your BMI is: {bmi} ')
        print(f'Your category is: {category} ')

        again = input('Do you want to continue? (yes/no): ').lower()
        if again not in ('yes', 'y'):
            print('Thank you for using BMI calculator! ')
            break

bmi_calculator()