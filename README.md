# Курсовая работа №3

Возвращает 5 транзакций в формате:

<дата перевода> <описание перевода>

<откуда> -> <куда>

<сумма перевода> <валюта>

## Пример вывода для одной операции:

14.10.2018 Перевод организации

Visa Platinum 7000 79** **** 6361 -> Счет **9638

82771.72 руб.

## Требования к работе:

- Последние 5 выполненных (EXECUTED) операций выведены на экран
- Операции разделены пустой строкой
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример, 14.10.2018)
- Сверху списка находятся самые последние операции (по дате)
- Номер карты замаскирован и не отображаться целиком, в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
- Номер счета замаскирован и не отображаться целиком, в формате  **XXXX 
  (видны только последние 4 цифры номера счета)