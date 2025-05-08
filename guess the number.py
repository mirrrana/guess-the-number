import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Угадай число от 1 до 100 за 10 попыток!")

    while attempts < max_attempts:
        try:
            guess = int(input("Твоя догадка: "))
        except ValueError:
            print("Введи число, а не текст!")
            continue

        attempts += 1

        if guess < number:
            print("Слишком мало!")
        elif guess > number:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Ты угадал за {attempts} попыток!")
            break

    else:
        print(f"Увы, число было {number}. Попробуй ещё раз!")

    if input("Сыграем ещё? (да/нет): ").lower() == "да":
        guess_the_number()

guess_the_number()
