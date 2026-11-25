# Запуск, эндпоинты
import keygen
import storage

error = '\nsmthn wrong!'

help = f"""
add - add link to db\nclear - clear all elements in db\nfind - find element with key or link\nshow - show all DB\ndelete - delete pair witn key or link\ndie - exit the program\nhelp - show this help message
"""

print('Welcome to the link storage program! Type "help" to see the list of commands.')

while True: # цикл опроса пользователя
    
    command = input('\n\ninput your command: ')
    if command == 'help': # команда вывода списка команд
        print(help)


    elif command == 'die': # команда выхода из программы
        print('\nbye!')
        break


    elif command == 'add': # команда добавления
        us_link = input('input your link: ')

        func_result = storage.add_link(key = keygen.key_generator(), us_link) # type: ignore # переменная хранит bool функции

        if func_result == True:
            print('Link added successfully')

        else: # если произошла коллизия - будем крутить ключи, пока не найдём уникальный
            while func_result == False:
                new_key = keygen.key_generator()

                func_result = storage.add_link(new_key, us_link) # type: ignore


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
            print(error)


    elif command == 'delete': # найти запись по ключу или ссылке и удалить
        elem = input('Input key or link so I can find and destroy it: ')
        pair = storage.find(elem)

        if storage.delete(elem):
            print(f'{pair} - deleted')
        else:
            print(error)


    else:
        print('Unknown command! Type "help" to see the list of commands.')