from abc import abstractmethod, ABC


class PokemonTrainInterface(ABC):
    """
    Абстрактный класс тренировок покемонов, который ссодержит
    один абстрактный метод increase_experience, и свойство experience
    который обязательны к реализации в классах наследниках
    """

    @abstractmethod
    def increase_experience(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def experience(self) -> int:
        pass


class BasePokemon(PokemonTrainInterface):
    """
    Класс, который создает покемона с атрибутами имя и тип покемона
    А также переопределяет метод строкового представления объекта
    Дополнительно наследуется от абстрактного класса и реализует один
    обязательный метод и одно свойство increase_experience и experience
    """

    def __init__(self, name: str, poketype: str):
        """
        конструктор, инициализирующий имя и тип покемона, а также
        начальный опыт
        """
        self.name = name
        self.poketype = poketype
        self.exp = 100

    def increase_experience(self, value: int) -> None:
        """
        метод, который получает на вход новое значение опыта для покемона
        и присваивает его
        """
        self.exp += 100

    @property
    def experience(self) -> int:
        """
        свойство, которое выводит значение опыта покемона
        """
        return self.exp

    def __str__(self) -> str:
        """
        магический метод для определения строкового представления объекта
        """
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    """
    Миксин, добавляющий доп. функциональность классу в виде
    замены типов покемонов в строковом представлении на смайлики
    """

    def swap_poketype(self, poketype: str) -> str:
        """
        метод который принимает на вход тип покемона и меняет его
        на смайлик
        """
        self.swap = {
            'grass': '🌿',
            'fire': '🔥',
            'water': '🌊',
            'electric': '⚡'
        }
        return self.swap[poketype]

    def __str__(self) -> str:
        """
        переопределенный магический метод для определения строкового
        представления объекта дополнительно меняется тип покемона на смайлик
        """
        return f'{self.name}/{self.swap_poketype(self.poketype)}'


class Pokemon(EmojiMixin, BasePokemon):
    """
    Класс наследник Pokemon, который наследует функциональность
    двух классов родителей, поэтому не содержит дополнительных
    методов и атрибутов, объявленных внутри
    """
    pass


if __name__ == '__main__':
    # 3 Pokemon/магический метод
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    bulbasaur.increase_experience(100)
    assert bulbasaur.experience == 200, 'Try harder, Neeman'
