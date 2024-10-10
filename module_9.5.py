class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start  # начало
        self.stop = stop  # конец
        self.step = step  # шаг
        self.pointer = start  # указывает на текущее число = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer * self.step > self.stop * self.step:
            raise StopIteration()
        pos = self.pointer
        self.pointer += self.step
        return pos


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end='')
except StepValueError:
    print('Шаг указан не верно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end='')
print()
for i in iter3:
    print(i, end='')
print()
for i in iter4:
    print(i, end='')
print()
for i in iter5:
    print(i, end='')
print()
