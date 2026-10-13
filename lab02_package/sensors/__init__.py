# файл sensors/__init__.py
# забезпечує використання модулів у складі пакета sensors

from .stats_module import (
    get_average,
    get_min,
    get_max,
    get_median,
    find_jumps,
    show_table
)

__all__ = [
    "get_average",
    "get_min",
    "get_max",
    "get_median",
    "find_jumps",
    "show_table"
]