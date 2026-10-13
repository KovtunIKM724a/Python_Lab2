# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників

import statistics

def get_average(data_dict):
    """Повертає середнє значення."""
    if not data_dict:
        return None
    try:
        values = list(data_dict.values())
        return round(statistics.mean(values), 2)
    except (TypeError, ValueError):
        return None


def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None
    try:
        return min(data_dict.values())
    except (TypeError, ValueError):
        return None


def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None
    try:
        return max(data_dict.values())
    except (TypeError, ValueError):
        return None


def get_median(data_dict):
    """Повертає медіану."""
    if not data_dict:
        return None
    try:
        values = list(data_dict.values())
        return round(statistics.median(values), 2)
    except (TypeError, ValueError):
        return None


def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями. Повертає список рядків із вказаними мітками часу та різницею."""
    jumps = []
    if not data_dict or len(data_dict) < 2:
        return jumps
    
    items = list(data_dict.items())
    for i in range(len(items) - 1):
        t1, val1 = items[i]
        t2, val2 = items[i+1]
        diff = abs(val2 - val1)
        if diff > threshold:
            jumps.append((t1, t2, round(diff, 2)))
            
    return jumps


def show_table(data_dict, title):
    """Виводить таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<15} | {'Значення'}")
    print("-" * 30)
    for timestamp, value in data_dict.items():
        print(f"{timestamp:<15} | {value}")