"""
  Автор: Бурлак Станислав Вячеславович. группа №З41551
  Ссылка на сайт-портфолио: http://ikonostasik.ru

"""


def find_sum(list, target):
    for outer_index, outer_value in enumerate(list):
        for inner_index, inner_value in enumerate(list):
            if inner_index == outer_index:
                continue
            if outer_value + inner_value == target:
                return [outer_index, inner_index]
    return -1


# Tests
assert find_sum([1, 2, 3, 4], 3) == [0, 1], 'ошибка в тестовом примере 1'
assert find_sum([23, 48, 12, 42, 52, 67, 89], 100) == [1, 4], 'ошибка в тестовом примере 2'
assert find_sum([11, 22, 33, 44, 55], 22) == -1, 'ошибка в тестовом примере 3'
assert find_sum([1, 1, 2, 3, 5, 8, 13, 21], 2) == [0, 1], 'ошибка в тестовом примере 4'
assert find_sum([1, 3, -5, 7, -9, 11, -13, 15], 6) == [2, 5], 'ошибка в тестовом примере 5'

