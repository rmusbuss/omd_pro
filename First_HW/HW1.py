from keyword import iskeyword
from json import loads
from collections.abc import Iterable
from typing import Any


class JSONParser(dict):
    """
    Класс, который получает на вход json в виде строки
    Преобразовывает его с помощью метода loads в Python объект
    Далее добавляет все элементы по ключам разных уровней вложенности
    в __dict__
    Дополнительно проверяет чтобы атрибут title включался в json
    """

    def __init__(self, mapping):
        """
        конструктор, который принимает на вход json в формате строки
        и преобразовывает его в Python объект,
        а также добавляет в __dict__
        """
        if isinstance(mapping, str):
            mapping = loads(mapping)
            if 'title' not in mapping:
                raise ValueError('title attribute must be present')
        super(JSONParser, self).__init__(mapping)
        for key, value in mapping.items():
            if isinstance(value, dict):
                if iskeyword(key):
                    key = key + '_'
                self.__dict__[key] = JSONParser(value)
            else:
                if iskeyword(key):
                    key = key + '_'
                self.__dict__[key] = value


class ColorizeMixin:
    """
    Mixin, который необходим для смены цвета текста при выводе
    на консоль.
    Цвет в атрибуте класса.
    """

    def __str__(self) -> str:
        """
        магический метод, который необходим для
        текстового представления обьектов класса
        Разукрашивает текст в разные цвета
        """
        result = [f'\033[0;{self.repr_color_code};48m']
        for key, value in self.items():
            if not isinstance(value, Iterable) or isinstance(value, str):
                if key == 'price':
                    result.append(str(value) + ' ₽')
                else:
                    result.append(str(value))
            else:
                result.append(' || '.join([str(iter_value)
                                           for iter_value in value]))
        return f'{result[0] + " | ".join(result[1:])}'


class Advert(ColorizeMixin, JSONParser):
    """
    Основной класс, который наследует методы и атрибуты от
    Миксина, отвечающего за текстовое представление и
    от JSONParser'а - предобработку json'а в Python объект
    """
    repr_color_code = 32

    def __init__(self, mapping):
        """
        конструктор, который вызывает конструктор парсера
        """
        super().__init__(mapping)

    @property
    def price(self) -> Any:
        """
        Свойство, которое проверяет, чтобы атрибут price
        был неотрицательным. В случае отрицательного знака
        выбрасывает ошибку
        В случае, если атрибута price нет, выводит 0
        """
        item = 'price'
        if item not in self.__dict__:
            return 0
        if float(self.__dict__[item]) < 0:
            raise ValueError('must be >= 0')
        else:
            return self.__dict__[item]

    @price.setter
    def price(self, value) -> None:
        """
        сеттер, который принимает на вход значение,
        которое необходимо передать атрибуту price.
        Проверяет на то, что price неотрицательна.
        в случае отрицательного знака - выбрасывает ошибку
        """
        if float(value) < 0:
            raise ValueError('must be >= 0')
        else:
            self.__dict__['price'] = value


if __name__ == '__main__':
    # проверяем, что к полям можно обращаться через точку
    lesson_str = '''{
        "title": "python",
        "price": 0,
        "location": {
    "address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"]
    }
    }'''
    lesson_ad = Advert(lesson_str)
    print(lesson_ad.location)
    print(lesson_ad.location.address)

    # проверяем, что price не может быть отрицательным
    # lesson_str2 = '{"title": "python", "price": -1}'
    # lesson_ad2 = Advert(lesson_str2)
    # print(lesson_ad2.price)

    # проверяем, что price не может быть отрицательным
    lesson_str3 = '{"title": "python", "price": 1}'
    lesson_ad3 = Advert(lesson_str3)
    # lesson_ad3.price = -3
    print(lesson_ad3.price)

    # проверяем, что price по умолчанию 0
    lesson_str4 = '{"title": "python"}'
    lesson_ad4 = Advert(lesson_str4)
    print(lesson_ad4.price)

    # проверяем, текстовое представление объектов и цвета
    test_str = '{"title": "python", "list": [1, 2, 3, 4]}'
    test_ad = Advert(test_str)
    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    iphone_ad.repr_color_code = 34
    print(iphone_ad)
    test_ad.repr_color_code = 35
    print(test_ad)
    lesson_ad3.repr_color_code = 37
    print(lesson_ad3)

    corgi_str = '''{
    "title": "Вельш-корги", "price": 1000,
    "class": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }'''
    corgi = Advert(corgi_str)
    corgi.repr_color_code = 33
    print(corgi)
