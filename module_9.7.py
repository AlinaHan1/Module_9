def is_prim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        summa = sum(args)
        i = 0
        for j in range(2, summa // 2 + 1):
            if summa % j == 0:
                i = i + 1
        if i <= 0:
            print(f'Суммы трех : {result} - простое число')
        else:
            print(f'Суммы трех : {result} - составное число')
        return result

    return wrapper


def sum_three(*args):
    return sum(args)


sum_three = is_prim(sum_three)
# n_1 = int(input('Введите первое число:'))
# n_2 = int(input('Введите первое число:'))
# n_3 = int(input('Введите первое число:'))
# result = sum_three(n_1, n_2, n_3)
result = sum_three(2, 3, 6)
print(result)
