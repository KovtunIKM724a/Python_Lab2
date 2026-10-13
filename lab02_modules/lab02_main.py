# lab02_main.py
# Основна програма для обробки показників системи "розумний будинок"

import stats_module as sm  # підключення модулю

def parse_input(input_str):
    """Перетворює введений рядок на список дійсних чисел (з перевіркою)."""
    numbers = []
    for item in input_str.split():
        try:
            num = float(item)
            numbers.append(num)
        except ValueError:
            print(f"Некоректне значення '{item}' проігноровано.")
    return numbers


def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник даних з мітками часу."""
    data = {}
    
    max_len = max(len(temp_list), len(hum_list), len(pres_list))
    
    temp_dict, hum_dict, pres_dict = {}, {}, {}
    
    for i in range(max_len):
        label = f"T{i+1}"
        if i < len(temp_list):
            temp_dict[label] = temp_list[i]
        if i < len(hum_list):
            hum_dict[label] = hum_list[i]
        if i < len(pres_list):
            pres_dict[label] = pres_list[i]
            
    data["temperature"] = temp_dict
    data["humidity"] = hum_dict
    data["pressure"] = pres_dict
    
    return data


def process_measurements(title, data_dict, threshold, unit=""):
    """Виводить таблицю та статистику для заданого виду даних."""
    if not data_dict:
        print(f"\nНемає даних для показника: {title}")
        return

    # Виводимо таблицю
    sm.show_table(data_dict, title)
    
    # Обчислюємо статистику
    avg = sm.get_average(data_dict)
    minimum = sm.get_min(data_dict)
    maximum = sm.get_max(data_dict)
    median = sm.get_median(data_dict)
    jumps = sm.find_jumps(data_dict, threshold)
    
    print(f"Середнє значення: {avg}")
    print(f"Мінімум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Медіана: {median}")
    
    if jumps:
        jumps_str = ", ".join([f"між {j[0]} → {j[1]} ({j[2]}{unit})" for j in jumps])
        print(f"Різкі перепади: {jumps_str}")
    else:
        print("Різких перепадів не виявлено.")


def main():
    print("=== Обробка показів системи 'Розумний будинок' ===")

    # 1) Запит значень у користувача
    raw_temp = input("Введіть температури (°C): ")
    raw_hum = input("Введіть вологість (%): ")
    raw_pres = input("Введіть тиск (Па): ")

    # 2) Обробка отриманих показників
    temp_list = parse_input(raw_temp)
    hum_list = parse_input(raw_hum)
    pres_list = parse_input(raw_pres)

    # 3) Створення загального словника
    data = create_data_dict(temp_list, hum_list, pres_list)

    # 4) Обробка та виведення результатів для кожного параметра
    process_measurements("Temperature", data.get("temperature", {}), threshold=7.0, unit="°C")
    process_measurements("Humidity", data.get("humidity", {}), threshold=20.0, unit="%")
    process_measurements("Pressure", data.get("pressure", {}), threshold=5000.0, unit="Па")


if __name__ == "__main__":
    main()