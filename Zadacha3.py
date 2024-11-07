from datetime import datetime, timedelta

def main_future_date(days):
    # Получаем текущую дату
    current_date = datetime.now()
    
    # Вычисляем будущую дату, добавляя указанное количество дней
    future_date = current_date + timedelta(days=days)
    
    # Форматируем будущую дату
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    print(f"Дата через {days} дней: {formatted_future_date}")

if __name__ == "__main__":
    # Вводим количество дней с клавиатуры
    days = int(input("Введите количество дней: "))
    main_future_date(days)
