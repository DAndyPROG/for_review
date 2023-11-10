import string

user_feedback = input('Введіть свої враження про курорт «Морська зірка»:').lower()
keywords = ['меню', 'спортзал', 'обслуговування']
discount = 0

user_feedback = user_feedback.translate(str.maketrans('', '', string.punctuation))

for keyword in keywords:
    if keyword in user_feedback:
        discount += 0.05
if len(user_feedback) > 60:
    discount += 0.15

total = min(1, discount)
if total > 0:
    print(user_feedback)
    print(f'Дякуємо за відгук! Ви отримали знижку на наступне відвідування - {discount * 100}%')
else:
    print('''
    Дякуємо за Ваш відгук!
    Заробляйте знижку на наступне відвідування:
    Зробіть відгук більше ніж 60 символів і гарантовано отримаєте знижку!
    ''')
