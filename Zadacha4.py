# Чтобы запустить этот скрипт, используйте команду:
# python Zadacha4.py <number> "<text>" [--verbose] [--repeat N]
# Например:
# python Zadacha4.py 7 "Привет, о сенсей, проверяющий мой кодЕЦ!" --verbose --repeat 3
import argparse

def main_args():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Процессинг числа и строки')
    
    # Добавляем обязательные аргументы
    parser.add_argument("number", type=int, help="Число для вывода")
    parser.add_argument("text", type=str, help="Текст для вывода")
    
    # Добавляем опции
    parser.add_argument("--verbose", action='store_true', help="Вывод дополнительной информации")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений текста")
    
    # Парсим аргументы
    args = parser.parse_args()

    # Выводим дополнительную информацию, если включен флаг verbose
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')
    
    # Выводим текст, повторенный указанное количество раз
    for _ in range(args.repeat):
        print(f'Число: {args.number} Текст: {args.text}')

if __name__ == "__main__":
    main_args()
