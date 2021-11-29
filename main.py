import os
import shutil
import settings

global path
path = settings.pathh
os.chdir(path)

def c_os():
    if os.name in ['nt']: return '\\'
    else: return '/'

def he(): #Сообщение help - Подсказки команд
    print('''af [имя папки] - создание папки
df [имя папки] - удаление папки
if [имя папки] - перейти в папку
of - перейти в папку выше
rnf [имя папки] [новое имя папки] - переименование папки
zip [имя папки] - архивация папки
afi [имя файла] - создание файла
wfi [имя файла] - запись текста в файл (вся следующая введенная строка будет записанна в файл)
rfi [имя файла] - чтение файла (содержимое будет выведено на экран)
dfi [имя файла] - удаление файла
cfi [имя файла] [имя конечной папки] - копирование файла в папку
mfi [имя файла] [имя конечной папки] - перенос файла в папку
rnfi [имя файла] [новое имя файла] - переименование файла
view - просмотр содежимого папки
ext - закрытие программы''')

def add_fold(name): #Создание папки
    if os.path.exists(f"{os.getcwd()}/{name}") == True:
        print("Папка с таким именем уже существет")
    else:
        os.mkdir(f"{os.getcwd()}/{name}")
        print("Папка успешно создана")
        
def del_fold(name): #Удаление папки
    if os.path.exists(f"{os.getcwd()}/{name}") == True:
        os.rmdir(f"{os.getcwd()}/{name}")
        print("Папка успешно удалена")
    else:
        print("Данной папки не существует")
        
def in_fold(name): #Переход в папку
    if os.path.exists(f"{os.getcwd()}/{name}") == True:
        os.chdir(f"{os.getcwd()}/{name}")
        print(f"Переход в папку {name} выполнен")
    else:
        print("Данной папки не существует")

def out_fold(): #Переход в папку выше
    if os.getcwd() == path:
        print("Выход за пределы данной директории невозможен")
    else:
        os.chdir("{0}".format(c_os().join(os.getcwd().split(c_os())[0:-1])))
        print("Переход в папку {0} выполнен".format(os.getcwd().split(c_os())[-1]))

def add_file(name): #Создание файла
    if name in os.listdir():
        print("Файл с таким именем уже существует")
    else:
        open(f"{name}", "w").close()
        print("Файл успешно создан")

def wri_file(name): #Запись в файл
    if name in os.listdir():
        with open(f"{name}", "w+") as f:
            f.write(input())
        print("Текст записан в файл")
    else:
        print("Файл не удалось найти")

def rea_file(name): #Чтение файла
    if name in os.listdir():
        with open(f"{name}", "r") as f:
            for i in f.readlines():
                print(i)
    else:
        print("Файл не удалось найти")

def del_file(name): #Удаление файла
    if name in os.listdir():
        os.remove(f"{os.getcwd()}/{name}")
        print("Файл успешно удален")
    else:
        print("Файл не удалось найти")

def cop_file(name, fold): #Копирование файла
    if name in os.listdir():
        if os.path.exists(f"{path}/{fold}") == True:
            if name in os.listdir(f"{path}/{fold}"):
                print(f"Файл {name} в папке {fold} уже существует")
            else:
                shutil.copyfile(f"{os.getcwd()}/{name}", f"{path}/{fold}/{name}")
                print("Файл успешно скопирован")
        else:
            print("Папка не найдена")
    else:
        print("Файл указан неверно")

def mov_file(name, fold): #Перемещение файла
    if name in os.listdir():
        if os.path.exists(f"{path}/{fold}") == True:
            if name in os.listdir(f"{path}/{fold}"):
                print(f"Файл {name} в папке {fold} уже существует")
            else:
                shutil.move(f"{os.getcwd()}/{name}", f"{path}/{fold}/{name}")
                print("Файл успешно перенесен")
        else:
            print("Папка не найдена")
    else:
        print("Файл указан неверно")

def ren_file(name, newname): #Переименование файла
    if name in os.listdir():
        shutil.move(f"{os.getcwd()}/{name}", f"{os.getcwd()}/{newname}")
        print(f"Файл {name} успешно переименован в {newname}")
    else:
        print("Файл не найден")

def ren_fold(name, newname): #Переименование папки
    if os.path.exists(f"{os.getcwd()}/{name}") == True:
        os.rename(f"{os.getcwd()}/{name}", f"{os.getcwd()}/{newname}")
        print(f"Папка {name} успешна переименована в {newname}")
    else:
        print("Папка не найдена")

def arh(name): #Архивация папки
    if os.path.exists(f"{os.getcwd()}/{name}") == True:
        shutil.make_archive(f"{name}", "zip", f"{os.getcwd()}{c_os()}{name}")
        print("Архив успешно создан")
    else:
        print("Папка не найдена")

def view(): #Просмотр содержимого папки
    for i in os.listdir():
        print(i)

def commands(): #Проверка и выполнение команд
    cmd = input()
    if cmd.split(' ')[0] == 'af': add_fold(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'df': del_fold(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'if': in_fold(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'of': out_fold()
    elif cmd.split(' ')[0] == 'rnf': ren_fold(cmd.split(' ')[1], cmd.split(' ')[2])
    elif cmd.split(' ')[0] == 'afi': add_file(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'wfi': wri_file(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'rfi': rea_file(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'dfi': del_file(cmd.split(' ')[1])
    elif cmd.split(' ')[0] == 'cfi': cop_file(cmd.split(' ')[1], cmd.split(' ')[2])
    elif cmd.split(' ')[0] == 'mfi': mov_file(cmd.split(' ')[1], cmd.split(' ')[2])
    elif cmd.split(' ')[0] == 'rnfi': ren_file(cmd.split(' ')[1], cmd.split(' ')[2])
    elif cmd.split(' ')[0] == 'zip': arh(cmd.split(' ')[1])
    elif cmd == 'view': view()
    elif cmd == 'help': help()
    elif cmd == 'ext': quit()
    else: print('Неизвестная команда \nДля просмотра всех команд введите "help"')

def start(): #Определение пользователя и регистрация нового
    global path
    q1 = input("Здравствуйте! Имеется ли у Вас корневая папка?[Yes/No] ")
    while True:
        if q1.upper() == 'YES':
            q2 = input("Введите Ваше имя. ")
            while True:
                if q2 in os.listdir():
                    path = path + c_os() + q2
                    os.chdir(path)
                    break
                else:
                    print("Данное имя не найдено")
                    q2 = input("Введите ещё раз. ")
            break
        elif q1.upper() == 'NO':
            q2 = input("Давайте её создадим. Введите Ваше имя. ")
            while True:
                if q2 in os.listdir():
                    print("Данное имя уже зарегистрированно")
                    q2 = input("Введите заново. ")
                else:
                    os.mkdir(f"{path}/{q2}")
                    path = path + c_os() + q2
                    os.chdir(path)
                    break
            break
        else:
            print("Введите ответ ещё раз.")
            q1 = input()
        
start()
he()
while True:
    commands()
