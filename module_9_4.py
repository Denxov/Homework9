
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y:x==y,first,second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'w',encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i)+'\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random

class MysticBall:
    def __call__(self):
        return random.choice(self.words)

    def __init__(self,*strings):
        self.words=[]
        for i in strings:
            self.words.append(i)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



