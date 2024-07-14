#Задача №1
def find_sum_elements(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]

def test_task_1():
    tests = (
        ([2, 11, 15, 7], 9),
        ([3, 2, 4], 6),
        ([0, 0, 1], 0),
        ([3, 2, 1], 4),
        ([1, 3, 6, 7, 9], 10),
    )
    num_correct = 0
    for nums, target in tests:
        result = find_sum_elements(nums, target)
        if not isinstance(result, list):
            print(f'find_sum_elements() должна возвращать массив, а не {type(result)} (nums={nums}, target={target})')
            continue
        if len(result) != 2:
            print(f'find_sum_elements() должна возвращать массив из двух элементов (nums={nums}, target={target})')
            continue
        if result[0] == result[1]:
            print(f'find_sum_elements() вернула два одинаковых индекса')
            continue
        if result[0] >= len(nums) or result[1] >= len(nums):
            print(f'Один из индексов выходит за границы nums')
            continue
        if nums[result[0]] + nums[result[1]] != target:
            print(f'Сумма элементов nums={nums} с индексами {result[0]} и {result[1]} не равна {target}')
            continue
        num_correct += 1
    print()
    print(f'Количество правильно решённых тестов: {num_correct} из {len(tests)}')
    if num_correct == len(tests):
        print('Отличный результат!')

test_task_1()


#Задача №2
def is_pangram(s):
    w = s.lower()
    return ( w >= 'a' and w <= 'я' and 'ё' in w)

def test_task_2():
    tests = (
        ('Съешь же ещё этих мягких французских булок да выпей чаю', True),
        ('Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства', True),
        ('В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!', False),
        ('А роза упала на лапу Азора', False),
        ('Мои папа и мама! Я живу хорошо. Просто замечательно. У меня есть свой дом', False),
    )
    num_correct = 0
    for test, correct_answer in tests:
        result = is_pangram(test)
        if result != correct_answer:
            print(f'Проверьте свою функцию на строке "{test}"')
            continue
        num_correct += 1
    print()
    print(f'Количество правильно решённых тестов: {num_correct} из {len(tests)}')
    if num_correct == len(tests):
        print('Отличный результат!')

test_task_2()