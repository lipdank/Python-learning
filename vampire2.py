import random
secret_number = (random.randint(1, 20))
print('Я загадал число от 1 до 20')
#Игроку даётся 6 попыток
for guessesTaken in range(1, 7):
    print('Угадайте число')
    guess = int(input())
    if guess < secret_number:
        print('Бери больше')
    elif guess > secret_number:
        print('Бери меньше')
    else:
        break   #Число угадано!
if guess == secret_number:
    print('Мега хорош! Кол-во попыток: ' + str(guessesTaken) + '.')
else:
    print('Вы лох. Я загадал число ' + str(secret_number))