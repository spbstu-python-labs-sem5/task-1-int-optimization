"""Задача №1. Диапазон оптимизации выделения памяти под объекты int."""
def same_object(n: int) -> bool:
    """Проверяет, что два независимо созданных числа n - один и тот же объект."""
    a = int(str(n))
    b = int(str(n))
    return id(a) == id(b)

def find_range() -> tuple[int, int]:
    """Возвращает (M, N) - границы диапазона [-M, N], где утверждение верно.
    Как только встречаем число вне кэша - выходим из цикла, а m/n остаются на последнем нужном нам значении."""
    m = n = 0
    while same_object(-(m + 1)):
        m += 1
    while same_object(n + 1):
        n += 1
    return m, n

if __name__ == "__main__":
    m, n = find_range()
    print(f"Диапазон: [{-m}, {n}]")
    print(f"M = {m}, N = {n}")