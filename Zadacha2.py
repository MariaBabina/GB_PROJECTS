from datetime import datetime

def main_datetime():
    # Получаем текущее время и дату
    now = datetime.now()
    
    # Форматируем дату и время
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Дата и время: {formatted_date}")
    
    # День недели
    day_of_week = now.strftime('%A')
    print(f"День недели: {day_of_week}")
    
    # Номер недели
    week_number = now.isocalendar()[1]
    print(f"Номер недели: {week_number}")

if __name__ == "__main__":
    main_datetime()
