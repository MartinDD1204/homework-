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
