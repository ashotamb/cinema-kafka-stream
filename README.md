# Cinema Kafka Streaming

Лабораторная работа №1  
Потоковая обработка данных с использованием Apache Kafka.

## Тема
Кинотеатр (офлайн)

Моделируются события продажи билетов на сеансы.

## Архитектура

Producer → Kafka → Consumer

## Формат данных

JSON сообщение:

film  
hall  
seat_row  
seat_number  
ticket_price  

## Запуск

1. Запустить Kafka
2. Запустить consumer

python consumer.py

3. Запустить producer

python producer.py