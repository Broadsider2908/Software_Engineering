import datetime


def record_time(filename):
    with open(filename, 'a') as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")
        print("Запись времени успешно добавлена.")


def main():
    filename = 'time.txt'

    while True:
        input("Нажмите Enter для записи текущего времени или 'q' для выхода: ")
        record_time(filename)


if __name__ == "__main__":
    main()