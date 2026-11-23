# Запуск, эндпоинты
import keygen
import storage

help = print(f'add - add link to db\nclear - clear all elements in db\nfind - find element with key or link\nshow - show all DB')

while True: # цикл опроса пользователя
    
    command = input('\n\ninput your command: ')
    if command == 'help': # команда вывода списка команд
        print(help)

    elif command == 'add': # команда добавления
        link = input('\ninput your link: ')
        key = keygen.key_generator()

        if storage.add_link(key, link):
            print('\nlink added succesfully!')
        else:
            print('\nsmthn wrong!')

    elif command == 'find': # Команда поиска по ключу или ссылке
        elem = input ('Введите значение ключа или ссылки, чтобы я мог их найти:\n')
        result = storage.find(elem)

        if result:
            print(f'Результат поиска: {result}')
        else:
            print(f'Результат поиска: нет подходящих элементов')

    elif command == 'show': # показать содержимое БД
        for i in storage.show():
            print(i)

    elif command == 'clear': # Очистить всю БД
        whiped_elements = len(storage.show())
        if storage.clear():
            print(f'DB whiped out! Deleted {whiped_elements}!')
        else:
            print('\nsmthn wrong!')