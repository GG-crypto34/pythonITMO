import unittest

import requests
from requests import exceptions

from lab7 import lab7 as l7

MAX_R_VALUE = 1000


# Тесты
class TestGetCurrencies(unittest.TestCase):

  def test_currency_usd(self):
    """
      Проверяет наличие ключа в словаре и значения этого ключа
    """
    currency_list = ['USD', 'EUR']
    currency_data = l7.get_currencies(currency_list)
    print(currency_data)
    print(currency_data['USD'])
    print(type(currency_data['USD']))
    self.assertIn(currency_list[0], currency_data['Values'])
    self.assertIsInstance(currency_data['USD'], float)
    self.assertGreaterEqual(currency_data['USD'], 0)

  def test_nonexist_code(self):
      with self.assertRaises(KeyError):
          l7.get_currencies(['XYZ','XYZ'])

  def test_get_currency_error(self):
    error_phrase_regex = "Ошибка при запросе к API"
    currency_list = ['USD']

    with self.assertRaises(requests.exceptions.RequestException):
      currency_data = l7.get_currencies(currency_list, url="https://")




  #   # Найти каким образом проверить содержание фразы error_phase_regex в
  #   # потоке вывода

  #   # Дополнить тест, который должен проверять что в потоке, куда пишет функция
  #   # get_currencies содержится error_phrase_regex /
  #   # для использования assertStartsWith или assertRegex





# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
