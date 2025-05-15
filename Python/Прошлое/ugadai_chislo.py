import random as r
number = 7
count_try = 0
number_to_guess = 0
language = int(input('Установите язык/Install the language Для выбора подросткового напишите 1, для матерного 2, для стандартного русского 3. If you want to choose English type 3. '))
if language == 1:
    input('Всем хай! Я - Ивангай. Ахахахахаха, Хай, чел. ')
    input('Чё как?/n')
    player_name = input('Кем будешь? Просто имя напиши./n')
    print(f'{player_name}, так {player_name}. И так, для правил игры нажми по этой табличке ПКМ. Хахаха, шучу (ит из отсылка).')
    input('Так вот правила игры: я какое-то число загадываю, а ты это какое-то число отгадываешь, уяснил? ')
    start = input('Ну шо? Го, не? ')
    if start == 'не':
        print('Я тогда ПаШьЁлЬ, дасвидос.')
    else: 
        prohod = input('Так мы играем? Да, нет? ')
        if prohod == 'Да' or 'да':
            number_to_guess = r.number
            player_number = int(input('Какое число я загадал? ')) 
            count_try += 1
            if player_number == number_to_guess:
                print(f'Йоу, чел ты крут! Победа присуждается {player_name}')
                print(f'Ты потратил {count_try} попыток.')
            if language == 2:
                print()