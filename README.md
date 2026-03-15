# Cinema Kafka Streaming

Лабораторная работа №1
Потоковая обработка данных с использованием Apache Kafka.

## Тема
Кинотеатр (офлайн)

Моделируются события продажи билетов на сеансы.

## Формат данных

JSON сообщение:

```json
{
  "cinema_event": "ticket_sale",
  "film": "Oppenheimer",
  "hall": 2,
  "seat_row": 5,
  "seat_number": 12,
  "session_time": "2025-03-15 18:30:00",
  "ticket_price": 550,
  "timestamp": "2025-03-15T15:30:00.123Z"
}
```

## Файлы проекта

- `producer.py` — отправляет сообщения в Kafka
- `consumer.py` — получает и проверяет сообщения
- `generator.py` — генерирует случайные данные
- `validator.py` — проверяет корректность данных
- `requirements.txt` — список зависимостей

## Установка

```bash
# Создать виртуальное окружение
python -m venv .venv

# Активировать (Windows)
.venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt
```

## Запуск Kafka

```bash
# Терминал 1 - ZooKeeper
cd C:\kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

# Терминал 2 - Kafka
cd C:\kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

## Запуск приложения

```bash
# Терминал 3 - Consumer
python consumer.py

# Терминал 4 - Producer
python producer.py
```

## Валидация

Consumer проверяет:
- наличие всех полей
- положительную цену билета
- положительные номера ряда и места

## Зависимости

```
kafka-python
```
ticket_price  

## Запуск

1. Запустить Kafka
2. Запустить consumer

python consumer.py

3. Запустить producer

python producer.py
