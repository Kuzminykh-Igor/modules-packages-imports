import time
from progress.bar import IncrementalBar


def calculate_salary():
    bar = IncrementalBar('Выполняется функция calculate_salary', max=100, suffix='%(percent)d%%')
    for i in range(100):
        bar.next()
        time.sleep(0.015)
    bar.finish()
    print('Функция выполнена')