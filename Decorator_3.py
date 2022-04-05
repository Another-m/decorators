from time import time, ctime


def flat_generator(nested_list):
    new_list = []
    for i in nested_list:
        if type(i) == list:
            value = flat_generator(i)
            new_list += value
        else:
            value = i
            new_list += [value]
    return new_list


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

nested_list_2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', ['...', 'x', 'y', 'z', '\n']],
    [1, 2, None, False, [1245, 850, 3, 56, ["python", "windows", "PyCharm"]]]
]


def decor(func):
    def nested_func(x, path):
        dt = ctime(time())
        t = time()
        result = func(x)
        print("Запуск функции ", func, "\nс аргументом ", x)
        print("Дата и время запуска: ", dt)
        print("Время работы фунции: ", time() - t, " секунд")
        logger = {"Дата и время запуска: ": dt, "Время работы фунции: ": time() - t, "Имя функции: ": func,
                  "Аргументы функции: ": x, "Путь к файлу логов: ": path}
        upload_file(logger, path)
        return result

    return nested_func


def upload_file(logger, path):
    with open(path, "a", encoding="utf-8") as file:
        file.write(str(logger) + "\n")
        print("Запись в файл logger.txt успешно завершена\n")


datatime = decor(flat_generator)

datatime(nested_list, "logger.txt")
datatime(nested_list_2, "logger.txt")

for elem in datatime(nested_list_2, "logger.txt"):
    print(elem)
