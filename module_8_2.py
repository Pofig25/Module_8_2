def personal_sum(numbers):
    result = 0                                                              # Инициализация суммы
    incorrect_data = 0                                                      # Счетчик некорректных данных
    for item in numbers:                                                    # Перебираем каждый элемент в коллекции
        try:
            result += item                                                  # Пытаемся добавить элемент к сумме
        except TypeError:                                                   # Если возникает TypeError,
            incorrect_data += 1                                             # увеличиваем счетчик и
            print(f'Некорректный тип данных для подсчёта суммы - {item}')   # выводим сообщение
    return result, incorrect_data                                           # Возвращаем сумму и количество
                                                                            # некорректных значений
def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)                   # Проверяем, есть ли некорректные данные
        if incorrect_data > 0:                                              # Проверяем, не является ли коллекция пустой
            return 0

        average = total_sum / len(numbers)                                  # Вычисляем среднее
        return average                                                      # Возвращаем среднее арифметическое

    except ZeroDivisionError:                                               # Обработка деления на 0
        return 0

    except TypeError:                                                       # Обработка ошибки TypeError
        print('В numbers записан некорректный тип данных')
        return 0
# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')                       # Передаем строку
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанная коллекция
print(f'Результат 3: {calculate_average(567)}')                             # Передаем число, не коллекцию
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')                # Корректная коллекция