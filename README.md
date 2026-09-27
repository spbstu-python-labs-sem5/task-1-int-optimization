# Задача №1. Диапазон оптимизации выделения памяти под объекты int

Известно, что в современной реализации CPython следующий код:

```python
x = 5
y = 5
```
даёт две ссылки x и y на один и тот же объект int(5), то есть:

`id(x) == id(y)`

## Задача
Найти максимальный диапазон целых чисел [-M, N], для которого вышеобозначенное утверждение верно.

## Решение
CPython кэширует малые целые числа (small integer cache). При старте
интерпретатора создаётся массив объектов `int` для чисел из некоторого
непрерывного диапазона `[lo, hi]`, и любое обращение к числу внутри
этого диапазона возвращает ссылку на уже существующий объект.
Достаточно идти от нуля в обе стороны по одному шагу, пока утверждение
`id(x) == id(y)` выполняется. Как только оно перестало выполняться -
мы нашли границу.

## Структура проекта
├── main.py # решение задачи
├── test_main.py # тесты
├── requirements.txt # зависимости
├── .gitignore
└── README.md

## Запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/spbstu-python-labs-sem5/task-1-int-optimization.git
cd task-1-int-optimization
```

### 2. Создать виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate # Linux / macOS
# .venv\Scripts\activate # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```
Файл `requirements.txt` содержит:
```
pytest==8.3.4
```

### 4. Запустить решение
```bash
python3 main.py
```
Ожидаемый вывод:
```
Диапазон: [-5, 256]
M = 5, N = 256
```

### 5. Запустить тесты
```bash
pytest -v
```
Ожидаемый вывод:
```
test_main.py::test_known_range PASSED
test_main.py::test_boundaries PASSED
```