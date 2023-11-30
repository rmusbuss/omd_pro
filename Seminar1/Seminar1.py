from abc import abstractmethod
from abc import ABC


# Задание 1-5
class Color:
    """
    Класс, который получает на вход три параметра - насыщенность света,
    каждый от 0 до 255. Выводит точку заданного цвета
    Умеет сранивать два цвета
    Может смешивать цвета
    Определяет уникальные цвета
    И может уменьшать контраст
    """
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_lvl: int, green_lvl: int, blue_lvl: int) -> None:
        """
        конструктор, в котором происходит инициализация насыщенности цветов
        и проверка на то, чтобы интенсивность каналов не выходила за 0 и 255
        """
        self.check_color(red_lvl)
        self.check_color(green_lvl)
        self.check_color(blue_lvl)
        self._red_level = red_lvl
        self._green_level = green_lvl
        self._blue_level = blue_lvl

    def __repr__(self) -> str:
        """
        магический метод, который, который выводит точку необходимого цвета
        в режиме отладки
        """
        return f'{self.START};{self._red_level};{self._green_level};' \
               f'{self._blue_level}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other: object) -> bool:
        """
        магический метод, которому на вход подается объект,
        с которым будет происходит сравнение
        """
        if not isinstance(other, Color):
            raise ValueError('Object of different type')
        if all([self.red == other.red,
                self.green == other.green,
                self.blue == other.blue]):
            return True
        return False

    def __add__(self, other: object) -> object:
        """
        магический метод, который реализует сложение двух
        объектов
        """
        if not isinstance(other, Color):
            raise ValueError('Object of different type')
        new_object = Color(self.red + other.red,
                           self.green + other.green,
                           self.blue + other.blue)
        return new_object

    def __hash__(self) -> int:
        """
        магический метод, считающий хеш для каждого объекта
        """
        return hash((self.red, self.green, self.blue))

    @staticmethod
    def fewer_contrast(c: float, color: int) -> int:
        """
        статический метод, считающий значение интенсивности цветов после
        изменения контраста. На вход подаются константа c для подсчета
        нового значения интенсивности и старое значение интенсивности
        """
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        return int(F * (color - 128) + 128)

    def __mul__(self, c: float) -> object:
        """
        Магический метод, переопределяющий умножение для объекта класса.
        Теперь при умножении на число будет меняться контраст
        Порядок таков: сначала обьект потом other
        """
        if not isinstance(c, float):
            raise ValueError('Object not of num type')
        c = float(c)
        red_level = self.fewer_contrast(c, self.red)
        blue_level = self.fewer_contrast(c, self.blue)
        green_level = self.fewer_contrast(c, self.green)

        new_object = Color(red_level,
                           green_level,
                           blue_level)
        return new_object

    def __rmul__(self, c: float) -> object:
        """
        Магический метод, переопределяющий умножение для объекта класса.
        Теперь при умножении на число будет меняться контраст
        Порядок таков: сначала other потом объект
        """
        return self.__mul__(c)

    @staticmethod
    def check_color(color: int) -> bool:
        """
        статический метод, который проверяет, чтобы интенсивность
        каждого канала не выходила за 255 или не опускалась ниже 0
        возвращает ошибку, если так
        """
        if color < 0 or color > 255:
            raise ValueError('Color parameters should be in [0; 255]')
        else:
            return True

    @property
    def red(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._red_level

    @red.setter
    def red(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._red_level = color

    @property
    def green(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._green_level

    @green.setter
    def green(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._green_level = color

    @property
    def blue(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._blue_level

    @blue.setter
    def blue(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._blue_level = color


# Задание 6

class ComputerColor(ABC):
    """
    Абстрактный класс - шаблон для определения структуры других классов
    Обязательные к определению методы __repr__, __mul__, __rmul__
    в классах наследниках
    """

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class NewColor(ComputerColor):
    """
    Тот же класс Color, просто для следующего задания
    Класс, который получает на вход три параметра - насыщенность света,
    каждый от 0 до 255. Выводит точку заданного цвета
    Умеет сранивать два цвета
    Может смешивать цвета
    Определяет уникальные цвета
    И может уменьшать контраст
    """
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_lvl: int, green_lvl: int, blue_lvl: int) -> None:
        """
        конструктор, в котором происходит инициализация насыщенности цветов
        и проверка на то, чтобы интенсивность каналов не выходила за 0 и 255
        """
        self.check_color(red_lvl)
        self.check_color(green_lvl)
        self.check_color(blue_lvl)
        self._red_level = red_lvl
        self._green_level = green_lvl
        self._blue_level = blue_lvl

    def __repr__(self) -> str:
        """
        магический метод, который, который выводит точку необходимого цвета
        в режиме отладки
        """
        return f'{self.START};{self._red_level};{self._green_level};' \
               f'{self._blue_level}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other: object) -> bool:
        """
        магический метод, которому на вход подается объект,
        с которым будет происходит сравнение
        """
        if not isinstance(other, Color):
            raise ValueError('Object of different type')
        if all([self.red == other.red,
                self.green == other.green,
                self.blue == other.blue]):
            return True
        return False

    def __add__(self, other: object) -> object:
        """
        магический метод, который реализует сложение двух
        объектов
        """
        if not isinstance(other, Color):
            raise ValueError('Object of different type')
        new_object = Color(self.red + other.red,
                           self.green + other.green,
                           self.blue + other.blue)
        return new_object

    def __hash__(self) -> int:
        """
        магический метод, считающий хеш для каждого объекта
        """
        return hash((self.red, self.green, self.blue))

    @staticmethod
    def fewer_contrast(c: float, color: int) -> int:
        """
        статический метод, считающий значение интенсивности цветов после
        изменения контраста. На вход подаются константа c для подсчета
        нового значения интенсивности и старое значение интенсивности
        """
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        return int(F * (color - 128) + 128)

    def __mul__(self, c: float) -> object:
        """
        Магический метод, переопределяющий умножение для объекта класса.
        Теперь при умножении на число будет меняться контраст
        Порядок таков: сначала обьект потом other
        """
        if not isinstance(c, float):
            raise ValueError('Object not of num type')
        c = float(c)
        red_level = self.fewer_contrast(c, self.red)
        blue_level = self.fewer_contrast(c, self.blue)
        green_level = self.fewer_contrast(c, self.green)

        new_object = Color(red_level,
                           green_level,
                           blue_level)
        return new_object

    def __rmul__(self, c: float) -> object:
        """
        Магический метод, переопределяющий умножение для объекта класса.
        Теперь при умножении на число будет меняться контраст
        Порядок таков: сначала other потом объект
        """
        return self.__mul__(c)

    @staticmethod
    def check_color(color: int) -> bool:
        """
        статический метод, который проверяет, чтобы интенсивность
        каждого канала не выходила за 255 или не опускалась ниже 0
        возвращает ошибку, если так
        """
        if color < 0 or color > 255:
            raise ValueError('Color parameters should be in [0; 255]')
        else:
            return True

    @property
    def red(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._red_level

    @red.setter
    def red(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._red_level = color

    @property
    def green(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._green_level

    @green.setter
    def green(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._green_level = color

    @property
    def blue(self) -> int:
        """
        свойство, которое выводит приватный атрибут цвета
        """
        return self._blue_level

    @blue.setter
    def blue(self, color: int) -> None:
        """
        сеттер, который выполняет проверку интенсивности цвета и присваивает
        переданное значение интенсивности
        """
        self.check_color(color)
        self._blue_level = color


def print_a(color: ComputerColor):
    """
    функция принимает на вход объект color абстрактного класса ComputerColor
    или его потомков с необходимыми определенными методами
    выводит на экран символ ААА
    """
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [
            bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [
            bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [
            bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [
            bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix: print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    # 1 вывод цвета
    red = Color(255, 0, 0)
    print(red)
    red.red = 100
    print(red)

    # 2 сравнение цветов
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(green == red)
    print(red == Color(255, 0, 0))

    # 3 смешивание цветов
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(green + red)

    # 4 уникальные цвета
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]

    print(set(color_list))

    # 5 уменьшение контраста
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print('rmul', 0.5 * red)
    print('mul', red * 0.5)

    # 6 Абстрактные классы
    red = NewColor(255, 10, 10)
    print_a(red)
