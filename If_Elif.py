def introduction (name, age, sex):
    if age > 18 and sex == 'hombre':
        print(f'Hola {name} tienes {age}, tremendo grandulon')
    elif age > 18 and sex == 'mujer':
        print(f'Hola {name} tienes {age}, señora digna de belleza y gracia')
    elif age <= 18 and sex == 'hombre':
        print(f'Hola {name} tienes {age}, queres una chocolatadita?')
    elif age <= 18 and sex == 'mujer':
        print(f'Hola {name} tienes {age}, pequeña, vaya a dormir una siestita')
        
def run():
    name = str(input('Como te llamas?'))
    age = int(input('Cual es tu edad?'))
    sex = str(input('Eres hombre o mujer?'))
    introduction(name, age, sex)
    
if __name__ == '__main__':
    run()
