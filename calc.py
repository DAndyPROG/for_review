import math

print('''
      Привіт, це програма калькулятор!
      Твоє завдання вводити числа та обирати математичну операцію.
      
      СПИСОК ОПЕРАЦІЙ:
      1. Додавання (+)
      2. Віднімання (-)
      3. Множення (*)
      4. Ділення (/)
      5. Зведення у ступінь (**)
      6. Знаходження квадратного кореня (sqrt)
      7. Знаходження кубічного кореня (cbrt)
      8. Знаходження синусу (sin)
      9. Знаходження косинусу (cos)
      10. Знаходження тангенсу (tan)
      11. Зупинка програми (stop)

      Якщо введеш не ті символи, що є у списку, програма видасть помилку!
      ''')

while True:
    try:
        operation = input('Оберіть операцію або введіть "stop" для завершення: ')
        
        if operation == 'stop':
            break
        
        if operation not in ['+', '-', '*', '/', '**', 'sqrt', 'cbrt', 'sin', 'cos', 'tan']:
            print('Такої операції не існує!')
            continue

        if operation in ['sqrt', 'cbrt', 'sin', 'cos', 'tan']:
            num = float(input('Введіть число: '))
            
            if operation == 'sqrt':
                if num < 0:
                    print('Квадратний корінь з від\'ємного числа - комплексне число.')
                else:
                    result = math.sqrt(num)
            elif operation == 'cbrt':
                result = num ** (1/3)
            elif operation == 'sin':
                
                result = math.radians(num)
                y = math.sin(result)
            elif operation == 'cos':
                result = math.radians(num)
                y=math.cos(result)
            elif operation == 'tan':
                result = math.radians(num)
                y = math.tan(result)

            print(f'Результат: {y}')
        else:
            num1 = float(input('Введіть перше число: '))
            num2 = float(input('Введіть друге число: '))
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print('Ділення на нуль недопустиме.')
                    continue
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2

            print(f'Результат: {result}')
    
    except ValueError:
        print('Некоректне введення числа.')
