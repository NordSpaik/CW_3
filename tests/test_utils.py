import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data("https://wrong.urk.com/")[0] is None
    assert get_data("https://github.com/arhipov-proA/lesson_11_2")[0] is None
    assert get_data("https://github.com/arhipov-proA/lesson_11_3")[0] is None


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]["date"] == '2020-07-03T18:35:29.512364'
    assert len(data) == 4


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организацииMaestro 1596 83** **** 5199 -> Счет **958931957.58 руб.', '03.07.2020 Перевод организации  -> Счет **55608221.37 USD', '30.06.2018 Перевод организацииСчет 7510 68** **** 6952 -> Счет **67029824.07 USD', '23.03.2018 Открытие вклада  -> Счет **243148223.05 руб.', '04.04.2019 Перевод со счета на счетСчет 1970 86** **** 8542 -> Счет **418879114.93 USD']

