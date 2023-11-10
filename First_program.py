print('''
      Hello I'm Garvis! Today i will be yours personal helper!
      Let's play a game! And i will told you some few things about this game!
      First thing: I'll ask you some questions and you must to answer.
      Second thing: You can get points if get write answer if not you'll loose the points.
      So, that's all you need to know about our game!
      
      Let's start and keep your best!
      
      P.S. Write answers only on English!
      ''')

points = 0

start_question = input('So, are you ready to start?')
if start_question == 'yes':
    first_question = input('Who is a founder of Python? ')
    if first_question == 'Gvido Van Rossum':
        print('Correct!')
        points += 1
    else:
        print('no, it is Gvido Van Rossum')
        points -= 1
    second_question = int(input('''
    Why Gvido Van Rossum call this language  Python?
    1 - He was a fan of the British comedy TV show 
    2 - He loved snakes
    3 - That's is cool name
    '''))

    if second_question == 2:
        print("Wow that's cool! + 1 point to you!")
        points += 1
    else:
        print('No, He was a fan of the British comedy TV show Monty Python')
        points -= 1

    print('Now, time to: something about math')
    third_question = int(input('Write 1st number:'))
    third_question1 = int(input('Write 2nd number:'))
    operation = input('Write  operation:')
    if operation == '+':
        print(third_question1+third_question1)
        points += 1
    else:
        if operation == '-':
            print(third_question1-third_question1)
            points += 1
        else:
            if operation == '*':
                print(third_question1 * third_question1)
                points += 1
            else:
                if operation == '/':
                    print(third_question1 / third_question1)
                    points += 1

    fourth_question = input('How many months in the year has 28 days?')
    if fourth_question == ' In each months has 28 days' or fourth_question == '12':
        print('Okey, on this time you know the answer. Next will be harder!')
        points += 1
    else:
        print('All months in the year have at least 28 days.')

    final_question = input('What answer can you never answer yes to?')
    if final_question == 'Are you asleep now?':
        print("EXLNT! You pass all questions! So, you're smart, let's play again later!")
        points += 1
    else:
        print('No. Answer is: Are you asleep now? ')
else:
    print('Ohhh, okey lets play later!')

print('So, game is over!Thanks for game!See you soon!')
print('Your score is :', points)

