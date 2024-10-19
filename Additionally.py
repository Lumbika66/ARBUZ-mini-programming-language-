#paste the code into python
import random

def show_WE():
    is_running = True

    while is_running:
        print("### НАШ ПРОЕКТ И КОД")
        print("Выберите пункт меню : ")
        print(" 1 - НАШ СОФТ")
        print(" 2 - ОПИСАНИЕ")
        print(" 0 - Выход")

        choice = input("Введите номер пункта: ")

        if choice == '1':
            print("Вы выбрали: НАШ ЯЗЫК")
            print("Ссылка на проект: https://github.com/Lumbika66/ARBUZ-mini-programming-language-")
        elif choice == '2':
            print("Вы выбрали: ОПИСАНИЕ")
            print("Этот скрипт представляет собой небольшой проект, который включает в себя несколько различных технологий и концепций программирования. Он разбит на основные части, каждая из которых отвечает за свою задачу.")
        elif choice == '0':
            is_running = False
            print("Выход из программы.")
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск функции
show_WE()
      
