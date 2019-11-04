# -*- coding: utf-8 -*-


def isFunnyFunction(data):
    """
    Возвращает 1, если передана последовательность одинаковых элементов
    или арифметическая прогрессия с шагом 1 или -1
    Если последовательность не удовлетворяет этим условиям ничего не возвращает (None)
    :param data: list, tuple
    :return:
    """
    if data != None:
        i = data[0]
        for j in range(1, len(data)):  # проверка все элементы равны первому
            if data[j] != i:
                i = 0
                break
        if i == 0:  # если не все элеметы равны то
            i = int(data[0])
            for j in range(1, len(data)):  # проверка, что все элемнты возрастают на один подряд
                if int(data[j]) == i + 1:
                    i += 1
                else:
                    i = 0
                    break
            if i != 0:  # если все элемнты возрастают на один подряд
                return 1
        else:  # если все элементы равны
            return 1
        i = int(data[len(data) - 1])  # последний элемент
        for j in range(len(data) - 2, -1, -1):  # итерируем в обратном порядке
            if int(data[j]) != i + 1:  # проверка на то, что возрастает на 1 с конца
                i = 0
                break
            else:
                i += 1
        if i != 0:  # если возрастает на один с конца
            return 1
    else:
        raise ValueError("data is None")


#  повторяющийся функционал вынес отдельно
def is_increase_for_1(data):
    it_increase_for_1 = True
    try:
        before = int(data[0])
        for current in data[1:]:
            current = int(current)
            if current - before != 1:
                it_increase_for_1 = False
                break
            before = current
    except (ValueError, IndexError) as e:
        print(e)
        it_increase_for_1 = False
    return it_increase_for_1


# is в названии предполагает, что функция что то проверяет и возвращает bool или другой бинарный результат
# названия функций snake case-ом
def good_funny_function(data):
    if data is None:
        raise ValueError("data is None")
    if len(data) < 1:
        raise ValueError("data is too short")
    all_same = all(x == data[0] for x in data)
    revers_data = data[::-1]
    if all_same or is_increase_for_1(data) or is_increase_for_1(revers_data):
        return 1


if __name__ == '__main__':
    # Улучшеную версию реализовал так, чтобы выводы обоих версий всегда совпадали, за исключением обработки ошибок
    data = [1, '2', 'jk', 3] #['1']
    print('Good: ', good_funny_function(data))
    print('Bad: ', isFunnyFunction(data))
