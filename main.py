"""Задача №1. Диапазон оптимизации выделения памяти под объекты int."""
def same_object(n: int) -> bool:
    """Проверяет, что два независимо созданных числа n - один и тот же объект."""
    a = int(str(n))
    b = int(str(n))
    return id(a) == id(b)

def find_range() -> tuple[int, int]:
    """Возвращает (M, N) - границы диапазона [-M, N], где утверждение верно.
    Как только встречаем число вне кэша - break, а m/n остаются на последнем нужном нам значении."""
    m = n = 0
    for i in range(1, 1000):
        if not same_object(-i):
            break
        m = i
    for j in range(1, 1000):
        if not same_object(j):
            break
        n = j
    return m, n

if __name__ == "__main__":
    m, n = find_range()
    print(f"Диапазон: [{-m}, {n}]")
    print(f"M = {m}, N = {n}")