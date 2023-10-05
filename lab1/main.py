while True:
    print("Меню заданий:\n"
          "1 - Задание на упорядоченность натурального числа по убыванию.\n"
          "2 - Задание на подсчёт количества пар верхнего и нижнего регистров.\n"
          "3 - Задание на нахождение суммы положительных элементов списка.\n"
          "4 - Задание со словарём.\n"
          '''5 - Программа "Кондитерская".\n'''
          "6 - Задание с кортежем.\n"
          "Любое другое число - Выход из программы.\n")

    var = int(input("Введите число для выбора задания: "))

    if var == 1:
        num = int(input("Введите натуральное число: "))

        # Преобразуем число в строку и разбиваем на отдельные цифры
        digits = list(str(num))

        # Проверяем, является ли последовательность упорядоченной по убыванию
        is_ordered = True
        for i in range(len(digits) - 1):
            if int(digits[i]) > int(digits[i + 1]):
                is_ordered = False
                break

        if is_ordered == True:
            print("Последовательность цифр справа налево упорядочена по убыванию")
        else:
            print("Последовательность цифр справа налево не упорядочена по убыванию")

        continue

    elif var == 2:
        # Ввод слова от пользователя
        word = input("Введите слово: ")

        # Инициализация счетчиков
        upper_pairs = 0  # количество пар верхнего регистра
        lower_pairs = 0  # количество пар нижнего регистра
        vowels = 0  # количество гласных букв

        # Перебор символов в слове
        for i in range(len(word) - 1):
            if word[i].isupper() and word[i + 1].isupper():
                upper_pairs += 1
            elif word[i].islower() and word[i + 1].islower():
                lower_pairs += 1

            if word[i].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                vowels += 1

        # Вывод результатов
        print("Количество пар верхнего регистра:", upper_pairs)
        print("Количество пар нижнего регистра:", lower_pairs)
        print("Количество гласных букв:", vowels)

        continue

    elif var == 3:
        # Ввод списка от пользователя
        lst = input("Введите список чисел через пробел: ").split()

        # Преобразование элементов списка в целочисленный тип
        lst = [int(num) for num in lst]

        # Инициализация переменных
        positive_sum = 0  # сумма положительных элементов
        after_zero_sum = 0  # сумма элементов после первого нуля
        zero_encountered = False  # флаг для отслеживания первого нуля

        # Перебор элементов списка
        for num in lst:
            if num > 0:
                positive_sum += num

            if zero_encountered == True:
                after_zero_sum += num

            if num == 0 and zero_encountered == False:
                zero_encountered = True

        # Проверка наличия нулей в списке
        if not zero_encountered:
            print("Сумму посчитать нельзя")
        else:
            print("Сумма положительных элементов:", positive_sum)
            print("Сумма элементов после первого нуля:", after_zero_sum)

        # Удаление отрицательных элементов из списка
        lst = [num for num in lst if num >= 0]
        print("Список после удаления отрицательных элементов:", lst)

        continue

    elif var == 4:
        # Пример словаря
        dictionary = {'a': 5, 'b': 2, 'c': 10, 'd': 1}

        # Сортировка словаря по значению в порядке возрастания
        sorted_dict_asc = sorted(dictionary.items(), key=lambda x: x[1])

        # Вывод отсортированного словаря в порядке возрастания
        print("Сортировка по значению в порядке возрастания:")
        for key, value in sorted_dict_asc:
            print(key, ":", value)

        # Сортировка словаря по значению в порядке убывания
        sorted_dict_desc = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        # Вывод отсортированного словаря в порядке убывания
        print("Сортировка по значению в порядке убывания:")
        for key, value in sorted_dict_desc:
            print(key, ":", value)

        continue

    elif var == 5:
        # Словарь с информацией о продукции
        products = {
            'торт': [['слои бисквита, крем, фрукты', 'цена: 200 руб/100гр', 'количество: 500 гр'], 200, 500],
            'пирожное': [['бисквитное тесто, крем, шоколадная глазурь', 'цена: 150 руб/100гр', 'количество: 300 гр'],
                         150, 300],
            'маффин': [['тесто, ягоды, сахарная пудра', 'цена: 100 руб/100гр', 'количество: 200 гр'], 100, 200],
            'печенье': [['тесто, шоколадные капли', 'цена: 50 руб/100гр', 'количество: 400 гр'], 50, 400],
            'эклер': [['воздушное тесто, крем, шоколадная глазурь', 'цена: 120 руб/100гр', 'количество: 250 гр'], 120,
                      250],
            'пончик': [['дрожжевое тесто, сахарная пудра', 'цена: 80 руб/100гр', 'количество: 350 гр'], 80, 350]
        }

        # Главное меню программы
        while True:
            print("Меню:")
            print("1. Просмотр описания")
            print("2. Просмотр цены")
            print("3. Просмотр количества")
            print("4. Вся информация")
            print("5. Покупка")
            print("6. До свидания")

            choice = input("Выберите пункт меню (1-6): ")

            if choice == '1':
                print("Описание продукции:")
                for product, info in products.items():
                    print(product, "-", info[0][0])
            elif choice == '2':
                print("Цены на продукцию:")
                for product, info in products.items():
                    print(product, "-", info[1], "руб/100гр")
            elif choice == '3':
                print("Количество продукции:")
                for product, info in products.items():
                    print(product, "-", info[2], "гр")
            elif choice == '4':
                print("Информация о продукции:")
                for product, info in products.items():
                    print(product)
                    for i in info[0]:
                        print(i)
                    print()
            elif choice == '5':
                total_price = 0
                while True:
                    product = input("Введите название продукции: ")
                    if product not in products:
                        print("Продукция не найдена. Попробуйте еще раз.")
                        continue
                    quantity = int(input("Введите количество (в граммах): "))
                    if quantity > products[product][2]:
                        print("Недостаточное количество продукции.")
                        continue
                    price = products[product][1] * quantity / 100
                    total_price += price
                    products[product][2] -= quantity
                print("Общая цена выбранных товаров:", total_price, "руб.")
                print("Остаток продукции:")
                print("Количество продукции:")
                for product, info in products.items():
                    print(product, "-", info[2], "гр")
            elif choice == '6':
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

    elif var == 6:
        # Кортеж целых чисел
        numbers = (1, 5, 9, 13, 8, 2, 4, 6, 10, 3, 7, 11, 12)
        # Вывод первого и последнего элемента кортежа
        print("Первый элемент:", numbers[0])
        print("Последний элемент:", numbers[-1])

        continue

    else:
        print("До свидания.")
        exit()
