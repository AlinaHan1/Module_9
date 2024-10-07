def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        res = func(int_list)
        result[func.__name__] = res
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
