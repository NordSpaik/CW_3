import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data("https://wrong.com/")[0] is None
    assert get_data("https://disk.yandex.ru/client/disk")[0] is None
    assert get_data("https://disk.yandex.ru/client/wrongdisk")[0] is None


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data)
    assert data[0]["date"] == '2020-07-03T18:35:29.512364'
    assert len(data) == 5


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.', '\n03.07.2020 Перевод организации\n  -> Счет **5560\n8221.37 USD', '\n30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD', '\n23.03.2018 Открытие вклада\n  -> Счет **2431\n48223.05 руб.', '\n04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD']