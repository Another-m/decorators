from time import time, ctime

def parametrized_decor(parameter):
    def decor(func):
        def nested_func(*args, **kwargs):
            dt = ctime(time())
            t = time()
            result = func(args[0])
            print("Запуск функции ", func.__name__, "с аргументом ", args[0])
            print("Дата и время запуска: ", dt)
            print("Время работы фунции: ", time() - t, " секунд")
            logger = {"Дата и время запуска: ": dt,
                      "Время работы фунции: ": time() - t,
                      "Имя функции: ": func.__name__,
                      "Аргументы функции: ": args,
                      "Путь к файлу логов: ": parameter
                      }
            upload_file(logger)
            return result

        return nested_func
    return decor


def upload_file(logger):
    with open(logger["Путь к файлу логов: "], "a", encoding="utf-8") as file:
        file.write(str(logger) + "\n")
        print("Запись в файл logger.txt успешно завершена\n")


@parametrized_decor(parameter="logger.txt")
def gen_range(x):
    for i in range(x):
        for y in range(i * 100):
            z = y / 10
    return "Функция завершила работу\n"


gen_range(100)
gen_range(1000)
