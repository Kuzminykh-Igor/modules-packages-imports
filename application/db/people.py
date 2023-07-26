import time
from progress.bar import IncrementalBar


def get_employees():
    bar = IncrementalBar('Выполняется функция get_employees', max=100, suffix='%(percent)d%%')
    for i in range(100):
        bar.next()
        time.sleep(0.015)
    bar.finish()
    print('Функция выполнена')