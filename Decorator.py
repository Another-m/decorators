from time import time, ctime

def gen_range(x):
    for i in range(x):
        for y in range(i * 100):
             z = y / 10
    return "Функция завершила работу\n"

def decor(func):
    def nested_func(x):
        dt = ctime(time())
        t = time()
        result = func(x)
        print("Запуск функции ", func, "с аргументом ", x)
        print("Дата и время запуска: ", dt)
        print("Время работы фунции: ", time() - t, " секунд")
        logger = {"Дата и время запуска: ": dt, "Время работы фунции: ": time() - t, "Имя функции: ": func, "Аргументы функции: ": x}
        upload_file(logger)
        return result
    return nested_func

def upload_file(logger):
    with open("logger.txt", "a", encoding="utf-8") as file:
        file.write(str(logger) + "\n")
        print("Запись в файл logger.txt успешно завершена\n")


datatime = decor(gen_range)
datatime(100)
datatime(1000)

