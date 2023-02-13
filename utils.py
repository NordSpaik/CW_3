import requests

from datetime import datetime


def get_data(url):
# Функция получения адреса с совершенными транзакциями.
# В случае неверного или несуществующего адреса, или отсутствия данных, функция формирует сообщение об ошибке.
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "УСПЕХ: Данные получены успешно\n"
        return None, f"ОШИБКА: Неверный статус-код {response.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "ОШИБКА: Ошибка соединения\n"
    except requests.exceptions.JSONDecodeError:
        return None, "ОШИБКА: Ошибка получения данных\n"


def get_filtered_data(data, filtered_empty_from=False):
# Функция выбора совершенных транзакций с полными параметрами сделки.
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data):
# Функция сортировки последних 5 транзакций в порядке убывания.
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def get_formatted_data(data):
# Функция подготовки вывода данных в требуемом формате.
    formatted_data = []
    for count in data:
        date = datetime.strptime(count["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = count["description"]
        from_who, from_card = "", ""
        if "from" in count:
            sender = count["from"].split()
            from_card = sender.pop(-1)
            from_who = " ".join(sender)
            if "Счет" in from_who:
                from_card = f"**{from_card[-4:]}"
            else:
                from_card = f"{from_card[:4]} {from_card[4:6]}** **** {from_card[-4:]}"
        to = f"{count['to'].split()[0]} **{count['to'][-4:]}"
        operation_amount = f"{count['operationAmount']['amount']} {count['operationAmount']['currency']['name']}"

        formatted_data.append(f"""
{date} {description}
{from_who} {from_card} -> {to}
{operation_amount}""")
    return formatted_data
