class StepValueError(ValueError):
    pass


class Iterator():
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        elif (step > 0 and start > stop) or (step < 0 and start < stop):
            self.start, self.stop, self.step = start, stop, -step  # -step адаптирует направление итерации к диапазону
        else:
            self.start, self.stop, self.step = start, stop, step

    def __next__(self):
        res = self.pointer
        self.pointer += self.step
        if (self.step>0 and self.stop<res) or (self.step<0 and self.stop>res):
            raise StopIteration()
        else:return round(res,1)


    def __iter__(self):
        self.pointer = self.start
        return self

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
        print('Шаг указан неверно')

iter2 = Iterator(-5, 1,)
iter3 = Iterator(6, 15, 0.9)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()