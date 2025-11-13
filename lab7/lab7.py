import sys
import functools
import requests
import io
import unittest
from requests import exceptions

def trace(func=None, *, handle=sys.stdout):
    print(f"decorated func: {func}, {handle}")
    if func is None:
        print('func is None')
        return lambda func: trace(func, handle=handle)
    else:
        print(f'{func.__name__}, {handle}')

    @functools.wraps(func)
    def inner(*args, **kwargs):
        handle.write(f"Using handling output\n")
        # print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    # print('return inner')
    return inner

nonstandardstream = io.StringIO()
@trace(handle=nonstandardstream)
def increm(x):
    """Инкремент"""
    # print("Инкремент")
    return x+1

increm(2)

nonstandardstream.getvalue()

def get_currencies(currency_codes: list, url:str = "https://www.cbr-xml-daily.ru/daily_json.js", handle=sys.stdout)->dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """
    try:

        response = requests.get(url)

        # print(response.status_code)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        # print(data)
        currencies = {}

        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    currencies[code] = f"Код валюты '{code}' не найден."
        return currencies

    except requests.exceptions.RequestException as e:
        # print(f"Ошибка при запросе к API: {e}", file=handle)
        handle.write(f"Ошибка при запросе к API: {e}")
        # raise ValueError('Упали с исключением')
        raise requests.exceptions.RequestException('Упали с исключением')

# Пример использования функции:
currency_list = ['USD', 'EUR', 'GBP', 'NNZ']

currency_data = get_currencies(currency_list, url='https://www.cbr-xml-daily.ru1/daily_json.js')
if currency_data:
     print(currency_data)

MAX_R_VALUE = 1000


# Тесты
class TestGetCurrencies(unittest.TestCase):

  def test_currency_usd(self):
    """
      Проверяет наличие ключа в словаре и значения этого ключа
    """
    currency_list = ['USD']
    currency_data = get_currencies(currency_list)

    self.assertIn(currency_list[0], currency_data)
    self.assertIsInstance(currency_data['USD'], float)
    self.assertGreaterEqual(currency_data['USD'], 0)
    self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)

  def test_nonexist_code(self):
    self.assertIn("Код валюты", get_currencies(['XYZ'])['XYZ'])
    self.assertIn("XYZ", get_currencies(['XYZ'])['XYZ'])
    self.assertIn("не найден", get_currencies(['XYZ'])['XYZ'])

  def test_get_currency_error(self):
    error_phrase_regex = "Ошибка при запросе к API"
    currency_list = ['USD']

    with self.assertRaises(requests.exceptions.RequestException):
      currency_data = get_currencies(currency_list, url="https://")




  #   # Найти каким образом проверить содержание фразы error_phase_regex в
  #   # потоке вывода

  #   # Дополнить тест, который должен проверять что в потоке, куда пишет функция
  #   # get_currencies содержится error_phrase_regex /
  #   # для использования assertStartsWith или assertRegex





# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)