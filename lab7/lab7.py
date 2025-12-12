import sys
import functools
import requests
import logging
import io
import math

def logger(func=None, *, handle=sys.stdout):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            start = f"Func: {f.__name__}, Args: {args}"
            try:
                result = f(*args, **kwargs)
                end  = f"Function {str(f)} ended, Res: {str(result)}"
                if handle is sys.stdout or handle is stream:
                    handle.write(start)
                    handle.write(end)
                elif isinstance(handle, logging.Logger):
                    handle.info(start)
                    handle.info(end)
                return result
            except Exception as e:
                mes = f"Exception: {str(e)}, {type(e)}"
                if handle is sys.stdout or handle is stream:
                    handle.write(mes)
                elif isinstance(handle, logging.Logger):
                    handle.error(mes)
                raise
        return wrapper
    if func is not None:
        return decorator(func)
    else:
        return decorator

stream = io.StringIO()
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)
log = logging.getLogger("L1")
@logger(handle=stream)
def get_currencies(currency_codes: list, url:str = "https://www.cbr-xml-daily.ru/daily_json.js")->dict:
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
        response.raise_for_status()
    except ConnectionError as e:
        raise

    try:
        data = response.json()
    except ValueError as e:
        raise

    currencies = {}
    if "Valute" in data:
        for code in currency_codes:
            try:
                currencies[code] = data["Valute"][code]["Value"]
            except KeyError as e:
                raise e
    else:
        raise KeyError("no Valute in data")
    return currencies


logging.basicConfig(
    filename="quadratic.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

@logger()
def solve_quadratic(a, b, c):
    logging.info(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

    # Ошибка типов
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):
            logging.critical(f"Parameter '{name}' must be a number, got: {value}")
            raise TypeError(f"Coefficient '{name}' must be numeric")

    # Ошибка: a == 0
    if a == 0:
        logging.error("Coefficient 'a' cannot be zero")
        raise ValueError("a cannot be zero")

    d = b*b - 4*a*c
    logging.debug(f"Discriminant: {d}")

    if d < 0:
        logging.warning("Discriminant < 0: no real roots")
        return None

    if d == 0:
        x = -b / (2*a)
        logging.info("One real root")
        return (x,)

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    logging.info("Two real roots computed")
    return root1, root2



if __name__ == "__main__":
    currency_list = ['USD`', 'EUR', 'GBP']
    try:
        get_currencies(currency_list, 'https://www.cbr-xml-daily.ru/daily_json.js')
    except:
        print(stream.getvalue())