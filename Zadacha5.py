import os
import argparse
from collections import namedtuple

# Определение структуры для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_all_files(filepath):
    # Проверка, что указанный путь существует и является директорией
    if not os.path.isdir(filepath):
        raise ValueError(f"Указанный путь {filepath} не является директорией или не существует.")
    
    # Открываем файл для записи в режиме добавления (append)
    with open('directory_contents.log', 'a', encoding='utf-8') as log_file:
        # Проходим по содержимому директории
        for fil in os.listdir(filepath):
            full_path = os.path.join(filepath, fil)
            
            # Проверяем, является ли элемент директорией или файлом
            if os.path.isdir(full_path):
                file_info = FileInfo(name=fil, extension=None, is_directory=True, parent_directory=filepath)
            else:
                name, extension = os.path.splitext(fil)
                file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=filepath)
            
            # Форматирование строки и запись в лог-файл
            log_message = f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}'
            log_file.write(log_message + '\n')
            print(log_message)  # Отладочный вывод на экран для проверки

def main():
    # Парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description='Получение информации о содержимом каталога')
    parser.add_argument("pathfiles", type=str, help="Путь к файлам")
    argses = parser.parse_args()
    
    # Получаем информацию о содержимом каталога
    try:
        get_all_files(argses.pathfiles)
        print(f'Информация о содержимом директории "{argses.pathfiles}" успешно записана в файл "directory_contents.log".')
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
