import random, sys
print('КАМЕНЬ, НОЖНИЦЫ, БУМАГА')
wins = 0
losses = 0
ties = 0

while True: #Главный цикл
    print('%s побед, %s поражений, %s ничьих' % (wins, losses, ties))
    while True: #Цикл выбора хода
        print('Выберите ход: (к)амень, (н)ожницы, (б)умага или ' + '(в)ыход')
        playerMove = input()
        if playerMove == "в":
            sys.exit()
        if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
            break
        print('Введите "к", "н", "б" или "в".')
    if playerMove == "к":
        print("КАМЕНЬ и ...")
    elif playerMove == "н":
        print("НОЖНИЦЫ и ...")
    elif playerMove == "б":
        print("БУМАГА и ...")

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove ="к"
        print('КАМЕНЬ')
    elif randomNumber == 2:
        computerMove = 'н'
        print('НОЖНИЦЫ')
    elif randomNumber == 3:
        computerMove = 'б'
        print('БУМАГА')

    if playerMove == computerMove:
        print('Ничья!')
        ties = ties + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Вы проиграли!')
        losses = losses + 1
